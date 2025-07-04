---
url: https://supabase.com/blog/authentication-in-ionic-angular
scraped_at: 2025-05-25T08:39:50.509439
title: Authentication in Ionic Angular with Supabase
---

  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=256&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
  * Product 
  * Developers 
  * [Enterprise](https://supabase.com/enterprise)
  * [Pricing](https://supabase.com/pricing)
  * [Docs](https://supabase.com/docs)
  * [Blog](https://supabase.com/blog)


[83.3K](https://github.com/supabase/supabase)[Sign in](https://supabase.com/dashboard)[Start your project](https://supabase.com/dashboard)
Open main menu
[Back](https://supabase.com/blog)
[Blog](https://supabase.com/blog)
# Authentication in Ionic Angular with Supabase
08 Nov 2022
•
55 minute read
[![Simon Grimm avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaimon24.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Simon GrimmGuest Author](https://twitter.com/schlimmson)
![Authentication in Ionic Angular with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fionic-angular-supabase.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Authentication of your apps is one of the most important topics, and by combining Angular logic with [Supabase authentication](https://supabase.com/docs/guides/auth) functionality we can build powerful and secure applications in no time.
In this tutorial, we will create an [Ionic Angular application with Supabase](https://supabase.com/docs/guides/with-ionic-angular) backend to build a simple realtime messaging app.
![Ionic Angular Authentication with Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fionic-angular-authentication-supabase.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Along the way we will dive into:
  * User **registration and login** with email/password
  * Adding [Row Level Security](https://supabase.com/docs/guides/auth/row-level-security) to protect our database
  * Angular **guards** and token handling logic
  * **Magic link** authentication for both web and **native mobile apps**


After going through this tutorial you will be able to create your own user authentication and secure your Ionic Angular app.
If you are not yet familiar with Ionic you can check out the [Ionic Quickstart guide of the Ionic Academy](https://ionicacademy.com/ionic-quickstart-guide/) or check out the [Ionic Supabase integration video](https://www.youtube.com/watch?v=pl9XfIWutKE) if you prefer video.
However, most of the logic is Angular based and therefore applies to any Angular web project as well.
You can [find the full code of this tutorial on Github](https://github.com/saimon24/supa-chat) where you just need to insert your own Supabase instance and then create the tables with the included SQL file.
But before we dive into the app, let's set up our Supabase project!
## Creating the Supabase Project[#](https://supabase.com/blog/authentication-in-ionic-angular#creating-the-supabase-project)
First of all, we need a new Supabase project. If you don't have a Supabase account yet, you can [get started for free](https://supabase.com/)!
In your dashboard, click "New Project" and leave it to the default settings, but make sure you keep a copy of your database password!
By default Supabase has the standard email/password authentication enabled, which you can find under the menu element **Authentication** and by scrolling down to the **Auth Provider** section.
![Supabase Auth Provider](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fsupabase-auth-provider.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Need to add another provider in the future? No problem!
Supabase offers a ton of providers that you can easily integrate so your users can sign up with their favorite provider.
On top of that, you can customize the auth settings and also the **email templates** that users see when they need to confirm their account, get a magic link or want to reset their password.
![Supabase Email Templates](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fsupabase-email-templates.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Feel free to play around with the settings, and once you're done let's continue with our database.
## Defining your Tables with SQL[#](https://supabase.com/blog/authentication-in-ionic-angular#defining-your-tables-with-sql)
Supabase uses Postgres for the database, so we need to write some SQL to define our tables upfront (although you can easily change them later through the Supabase Web UI as well!)
We want to build a simple messaging app, so what we need is:
  * `users`: A table to keep track of all registered users
  * `groups`: Keep track of user-created chat groups
  * `messages`: All messages of our app


To create the tables, simply navigate to the **SQL Editor** menu item and click on **+ New query** , paste in the SQL and hit **RUN** which hopefully executes without issues:
`
1
create table users (
2
 id uuid not null primary key,
3
 email text
4
);
56
create table groups (
7
 id bigint generated by default as identity primary key,
8
 creator uuid references public.users not null default auth.uid(),
9
 title text not null,
10
 created_at timestamp with time zone default timezone('utc'::text, now()) not null
11
);
1213
create table messages (
14
 id bigint generated by default as identity primary key,
15
 user_id uuid references public.users not null default auth.uid(),
16
 text text check (char_length(text) > 0),
17
 group_id bigint references groups on delete cascade not null,
18
 created_at timestamp with time zone default timezone('utc'::text, now()) not null
19
);
`
After creating the tables we need to define **policies** to prevent unauthorized access to some of our data.
In this scenario **we allow unauthenticated users to read group data** - everything else like creating a group, or anything related to messages is only allowed for authenticated users.
Go ahead and also run the following query in the editor:
`
1
-- Secure tables
2
alter table users enable row level security;
3
alter table groups enable row level security;
4
alter table messages enable row level security;
56
-- User Policies
7
create policy "Users can read the user email." on users
8
 for select using (true);
910
-- Group Policies
11
create policy "Groups are viewable by everyone." on groups
12
 for select using (true);
1314
create policy "Authenticated users can create groups." on groups for
15
 insert to authenticated with check (true);
1617
create policy "The owner can delete a group." on groups for
18
  delete using ((select auth.uid()) = creator);
1920
-- Message Policies
21
create policy "Authenticated users can read messages." on messages
22
 for select to authenticated using (true);
2324
create policy "Authenticated users can create messages." on messages
25
 for insert to authenticated with check (true);
`
Now we also add a cool function that will automatically add user data after registration into our table. This is necessary if you want to keep track of some user information, because the Supabase auth table is an internal table that we can't access that easily.
Go ahead and run another SQL query in the editor now to create our trigger:
`
1
-- Function for handling new users
2
create or replace function public.handle_new_user()
3
returns trigger as $$
4
begin
5
 insert into public.users (id, email)
6
 values (new.id, new.email);
7
 return new;
8
end;
9
$$ language plpgsql security definer;
1011
create trigger on_auth_user_created
12
 after insert on auth.users
13
 for each row execute procedure public.handle_new_user();
`
To wrap this up we want to enable **realtime functionality** of our database so we can get new messages instantly without another query.
For this we can activate the publication for our messages table by running one last query:
`
1
begin;
2
 -- remove the supabase_realtime publication
3
 drop publication if exists supabase_realtime;
45
 -- re-create the supabase_realtime publication with no tables and only for insert
6
 create publication supabase_realtime with (publish = 'insert');
7
commit;
89
-- add a table to the publication
10
alter publication supabase_realtime add table messages;
`
If you now open the **Table Editor** menu item you should see your three tables, and you can also check their RLS policies right from the web!
But enough SQL for today, let's write some Angular code.
## Creating the Ionic Angular App[#](https://supabase.com/blog/authentication-in-ionic-angular#creating-the-ionic-angular-app)
To get started with our Ionic app we can create a blank app without any additional pages and then install the [Supabase Javascript client](https://github.com/supabase/supabase-js).
Besides that, we need some pages in our app for the different views, and services to keep our logic separated from the views. Finally we can also already generate a **guard** which we will use to protect internal pages later.
Go ahead now and run the following on your command line:
`
1
ionic start supaAuth blank --type=angular
2
npm install @supabase/supabase-js
34
# Add some pages
5
ionic g page pages/login
6
ionic g page pages/register
7
ionic g page pages/groups
8
ionic g page pages/messages
910
# Generate services
11
ionic g service services/auth
12
ionic g service services/data
1314
# Add a guard to protect routes
15
ionic g guard guards/auth --implements=CanActivate
`
Ionic (or the Angular CLI under the hood) will now create the routing entries for us, but we gonna fine tune them a bit.
First of all we want to pass a **groupid** to our messages page, and we also want to make sure that page is protected by the guard we created before.
Therefore bring up the **src/app/app-routing.module.ts** and change it to:
`
1
import { AuthGuard } from './guards/auth.guard'
2
import { NgModule } from '@angular/core'
3
import { PreloadAllModules, RouterModule, Routes } from '@angular/router'
45
const routes: Routes = [
6
 {
7
  path: '',
8
  loadChildren: () => import('./pages/login/login.module').then((m) => m.LoginPageModule),
9
 },
10
 {
11
  path: 'register',
12
  loadChildren: () =>
13
   import('./pages/register/register.module').then((m) => m.RegisterPageModule),
14
 },
15
 {
16
  path: 'groups',
17
  loadChildren: () => import('./pages/groups/groups.module').then((m) => m.GroupsPageModule),
18
 },
19
 {
20
  path: 'groups/:groupid',
21
  loadChildren: () =>
22
   import('./pages/messages/messages.module').then((m) => m.MessagesPageModule),
23
  canActivate: [AuthGuard],
24
 },
25
 {
26
  path: '',
27
  redirectTo: 'home',
28
  pathMatch: 'full',
29
 },
30
]
3132
@NgModule({
33
 imports: [RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })],
34
 exports: [RouterModule],
35
})
36
export class AppRoutingModule {}
`
Now all paths are correct and the app starts on the login page, and the messages page can only be activated if that guard returns true - which it does by default, so we will take care of its implementation later.
To connect our app properly to Supabase we now need to grab the **project URL** and the **public anon key** from the settings page of your Supabase project.
You can find those values in your Supabase project by clicking on the **Settings** icon and then navigating to **API** where it shows your **Project API keys**.
This information now goes straight into the **src/environments/environment.ts** of our Ionic project:
`
1
export const environment = {
2
 production: false,
3
 supabaseUrl: 'https://YOUR-APP.supabase.co',
4
 supabaseKey: 'YOUR-ANON-KEY',
5
}
`
By the way: The `anon` key is safe to use in a frontend project since we have enabled RLS on our database tables!
## Building the Public Pages of our App[#](https://supabase.com/blog/authentication-in-ionic-angular#building-the-public-pages-of-our-app)
The big first step is to create the "outside" pages which allow a user to perform different operations:
![Ionic Login Page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fionic-login-page.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Before we dive into the UI of these pages we should define all the required logic in a service to easily inject it into our pages.
### Preparing our Supabase authentication service[#](https://supabase.com/blog/authentication-in-ionic-angular#preparing-our-supabase-authentication-service)
Our service should call expose all the functions for registration and login but also handle the state of the current user with a **BehaviorSubject** so we can easily emit new values later when the user session changes.
We are also loading the session once "by hand" using `getUser()` since the `onAuthStateChange` event is usually not broadcasted when the app loads, and we want to load a stored session right when the app starts.
The relevant functions for our user authentication are all part of the `supabase.auth` object, which makes it easy to find all relevant (_and even some unknown_) features.
Additionally, we expose our current user as an `Observable` to the outside and add some helper functions to get the current user ID synchronously.
Now move on by changing the **src/app/services/auth.service.ts** to this:
`
1
/* eslint-disable @typescript-eslint/naming-convention */
2
import { Injectable } from '@angular/core'
3
import { Router } from '@angular/router'
4
import { isPlatform } from '@ionic/angular'
5
import { createClient, SupabaseClient, User } from '@supabase/supabase-js'
6
import { BehaviorSubject, Observable } from 'rxjs'
7
import { environment } from '../../environments/environment'
89
@Injectable({
10
 providedIn: 'root',
11
})
12
export class AuthService {
13
 private supabase: SupabaseClient
14
 private currentUser: BehaviorSubject<User | boolean> = new BehaviorSubject(null)
1516
 constructor(private router: Router) {
17
  this.supabase = createClient(environment.supabaseUrl, environment.supabaseKey)
1819
  this.supabase.auth.onAuthStateChange((event, sess) => {
20
   if (event === 'SIGNED_IN' || event === 'TOKEN_REFRESHED') {
21
    console.log('SET USER')
2223
    this.currentUser.next(sess.user)
24
   } else {
25
    this.currentUser.next(false)
26
   }
27
  })
2829
  // Trigger initial session load
30
  this.loadUser()
31
 }
3233
 async loadUser() {
34
  if (this.currentUser.value) {
35
   // User is already set, no need to do anything else
36
   return
37
  }
38
  const user = await this.supabase.auth.getUser()
3940
  if (user.data.user) {
41
   this.currentUser.next(user.data.user)
42
  } else {
43
   this.currentUser.next(false)
44
  }
45
 }
4647
 signUp(credentials: { email; password }) {
48
  return this.supabase.auth.signUp(credentials)
49
 }
5051
 signIn(credentials: { email; password }) {
52
  return this.supabase.auth.signInWithPassword(credentials)
53
 }
5455
 sendPwReset(email) {
56
  return this.supabase.auth.resetPasswordForEmail(email)
57
 }
5859
 async signOut() {
60
  await this.supabase.auth.signOut()
61
  this.router.navigateByUrl('/', { replaceUrl: true })
62
 }
6364
 getCurrentUser(): Observable<User | boolean> {
65
  return this.currentUser.asObservable()
66
 }
6768
 getCurrentUserId(): string {
69
  if (this.currentUser.value) {
70
   return (this.currentUser.value as User).id
71
  } else {
72
   return null
73
  }
74
 }
7576
 signInWithEmail(email: string) {
77
  return this.supabase.auth.signInWithOtp({ email })
78
 }
79
}
`
That's enough logic for our pages, so let's put that code to use.
### Creating the Login Page[#](https://supabase.com/blog/authentication-in-ionic-angular#creating-the-login-page)
Although we first need to register a user, we begin with the login page. We can even "register" a user from here since we will offer the easiest sign-in option with **magic link** authentication that only requires an email, and a user entry will be added to our `users` table thanks to our trigger function.
To create a decent UX we will add a **reactive form** with Angular, for which we first need to import the `ReactiveFormsModule` into the **src/app/pages/login/login.module.ts** :
`
1
import { NgModule } from '@angular/core'
2
import { CommonModule } from '@angular/common'
3
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
45
import { IonicModule } from '@ionic/angular'
67
import { LoginPageRoutingModule } from './login-routing.module'
89
import { LoginPage } from './login.page'
1011
@NgModule({
12
 imports: [CommonModule, FormsModule, IonicModule, LoginPageRoutingModule, ReactiveFormsModule],
13
 declarations: [LoginPage],
14
})
15
export class LoginPageModule {}
`
Now we can define the form from code and add all required functions to our page, which becomes super easy thanks to our previous implementation of the service.
Right inside the constructor of the login page, we will also subscribe to the `getCurrentUser()` Observable and if we do have a valid user token, we can directly route the user forward to the groups overview page.
On login, we now only need to show some loading spinner and call the according function of our service, and since we already listen to the user in our constructor we don't even need to add any more logic for routing at this point and only show an alert in case something goes wrong.
Go ahead by changing the **src/app/pages/login/login.page.ts** to this now:
`
1
import { AuthService } from './../../services/auth.service'
2
import { Component } from '@angular/core'
3
import { FormBuilder, Validators } from '@angular/forms'
4
import { Router } from '@angular/router'
5
import { LoadingController, AlertController } from '@ionic/angular'
67
@Component({
8
 selector: 'app-login',
9
 templateUrl: './login.page.html',
10
 styleUrls: ['./login.page.scss'],
11
})
12
export class LoginPage {
13
 credentials = this.fb.nonNullable.group({
14
  email: ['', Validators.required],
15
  password: ['', Validators.required],
16
 })
1718
 constructor(
19
  private fb: FormBuilder,
20
  private authService: AuthService,
21
  private loadingController: LoadingController,
22
  private alertController: AlertController,
23
  private router: Router
24
 ) {
25
  this.authService.getCurrentUser().subscribe((user) => {
26
   if (user) {
27
    this.router.navigateByUrl('/groups', { replaceUrl: true })
28
   }
29
  })
30
 }
3132
 get email() {
33
  return this.credentials.controls.email
34
 }
3536
 get password() {
37
  return this.credentials.controls.password
38
 }
3940
 async login() {
41
  const loading = await this.loadingController.create()
42
  await loading.present()
4344
  this.authService.signIn(this.credentials.getRawValue()).then(async (data) => {
45
   await loading.dismiss()
4647
   if (data.error) {
48
    this.showAlert('Login failed', data.error.message)
49
   }
50
  })
51
 }
5253
 async showAlert(title, msg) {
54
  const alert = await this.alertController.create({
55
   header: title,
56
   message: msg,
57
   buttons: ['OK'],
58
  })
59
  await alert.present()
60
 }
61
}
`
Additionally, we need a function to reset the password and trigger the magic link authentication.
In both cases, we can use an Ionic alert with one input field. This field can be accessed inside the handler of a button, and so we pass the value to the according function of our service and show another message after successfully submitting the request.
Go ahead with our login page and now also add these two functions:
`
1
 async forgotPw() {
2
  const alert = await this.alertController.create({
3
   header: "Receive a new password",
4
   message: "Please insert your email",
5
   inputs: [
6
    {
7
     type: "email",
8
     name: "email",
9
    },
10
   ],
11
   buttons: [
12
    {
13
     text: "Cancel",
14
     role: "cancel",
15
    },
16
    {
17
     text: "Reset password",
18
     handler: async (result) => {
19
      const loading = await this.loadingController.create();
20
      await loading.present();
21
      const { data, error } = await this.authService.sendPwReset(
22
       result.email
23
      );
24
      await loading.dismiss();
2526
      if (error) {
27
       this.showAlert("Failed", error.message);
28
      } else {
29
       this.showAlert(
30
        "Success",
31
        "Please check your emails for further instructions!"
32
       );
33
      }
34
     },
35
    },
36
   ],
37
  });
38
  await alert.present();
39
 }
4041
 async getMagicLink() {
42
  const alert = await this.alertController.create({
43
   header: "Get a Magic Link",
44
   message: "We will send you a link to magically log in!",
45
   inputs: [
46
    {
47
     type: "email",
48
     name: "email",
49
    },
50
   ],
51
   buttons: [
52
    {
53
     text: "Cancel",
54
     role: "cancel",
55
    },
56
    {
57
     text: "Get Magic Link",
58
     handler: async (result) => {
59
      const loading = await this.loadingController.create();
60
      await loading.present();
61
      const { data, error } = await this.authService.signInWithEmail(
62
       result.email
63
      );
64
      await loading.dismiss();
6566
      if (error) {
67
       this.showAlert("Failed", error.message);
68
      } else {
69
       this.showAlert(
70
        "Success",
71
        "Please check your emails for further instructions!"
72
       );
73
      }
74
     },
75
    },
76
   ],
77
  });
78
  await alert.present();
79
 }
`
That's enough to handle everything, so now we just need a simple UI for our form and buttons.
Since recent Ionic versions, we can use the new **error slot** of the Ionic item, which we can use to present specific error messages in case one field of our reactive form is invalid.
We can easily access the `email` and `password` control since we exposed them with their own `get` function in our class before!
Below the form, we simply stack all of our buttons to trigger the actions and give them different colors.
Bring up the **src/app/pages/login/login.page.html** now and change it to:
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-title>Supa Chat</ion-title>
4
 </ion-toolbar>
5
</ion-header>
67
<ion-content scrollY="false">
8
 <ion-card>
9
  <ion-card-content>
10
   <form (ngSubmit)="login()" [formGroup]="credentials">
11
    <ion-item>
12
     <ion-label position="stacked">Your Email</ion-label>
13
     <ion-input
14
      type="email"
15
      inputmode="email"
16
      placeholder="Email"
17
      formControlName="email"
18
     ></ion-input>
19
     <ion-note slot="error" *ngIf="(email.dirty || email.touched) && email.errors"
20
      >Please insert your email</ion-note
21
     >
22
    </ion-item>
23
    <ion-item>
24
     <ion-label position="stacked">Password</ion-label>
25
     <ion-input type="password" placeholder="Password" formControlName="password"></ion-input>
26
     <ion-note slot="error" *ngIf="(password.dirty || password.touched) && password.errors"
27
      >Please insert your password</ion-note
28
     >
29
    </ion-item>
30
    <ion-button type="submit" expand="block" strong="true" [disabled]="!credentials.valid"
31
     >Sign in</ion-button
32
    >
3334
    <div class="ion-margin-top">
35
     <ion-button
36
      type="button"
37
      expand="block"
38
      color="primary"
39
      fill="outline"
40
      routerLink="register"
41
     >
42
      <ion-icon name="person-outline" slot="start"></ion-icon>
43
      Create Account
44
     </ion-button>
4546
     <ion-button type="button" expand="block" color="secondary" (click)="forgotPw()">
47
      <ion-icon name="key-outline" slot="start"></ion-icon>
48
      Forgot password?
49
     </ion-button>
5051
     <ion-button type="button" expand="block" color="tertiary" (click)="getMagicLink()">
52
      <ion-icon name="mail-outline" slot="start"></ion-icon>
53
      Get a Magic Link
54
     </ion-button>
55
     <ion-button type="button" expand="block" color="warning" routerLink="groups">
56
      <ion-icon name="arrow-forward" slot="start"></ion-icon>
57
      Start without account
58
     </ion-button>
59
    </div>
60
   </form>
61
  </ion-card-content>
62
 </ion-card>
63
</ion-content>
`
To give our login a bit nicer touch, let's also add a background image and some additional padding by adding the following to the **src/app/pages/login/login.page.scss** :
`
1
ion-content {
2
 --padding-top: 20%;
3
 --padding-start: 5%;
4
 --padding-end: 5%;
5
 --background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.7)),
6
  url('https://images.unsplash.com/photo-1508964942454-1a56651d54ac?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1035&q=80')
7
   no-repeat;
8
}
`
At this point you can already try our authentication by using the magic link button, so run the Ionic app with `ionic serve` for the web preview and then enter your email.
![Magic Link Alert](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fmagic-link-input.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Make sure you use a valid email since you do need to click on the link in the email. If everything works correctly you should receive an email like this quickly:
![Magic Link Email](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fmagic-link-email.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Keep in mind that you can easily change those email templates inside the settings of your Supabase project.
If you now inspect the link and copy the URL, you should see an URL that points to your Supabase project and after some tokens there is a query param `&redirect_to=http://localhost:8100` which directly brings a user back into our local running app!
This will be even more important later when we implement **magic link authentication for native apps** so stick around until the end.
### Creating the Registration Page[#](https://supabase.com/blog/authentication-in-ionic-angular#creating-the-registration-page)
Some users will still prefer the good old registration, so let's provide them with a decent page for that.
The setup is almost the same as for the login, so we start again by adding the `ReactiveFormsModule` to the **src/app/pages/register/register.module.ts** :
`
1
import { NgModule } from '@angular/core'
2
import { CommonModule } from '@angular/common'
3
import { FormsModule, ReactiveFormsModule } from '@angular/forms'
45
import { IonicModule } from '@ionic/angular'
67
import { RegisterPageRoutingModule } from './register-routing.module'
89
import { RegisterPage } from './register.page'
1011
@NgModule({
12
 imports: [CommonModule, FormsModule, IonicModule, RegisterPageRoutingModule, ReactiveFormsModule],
13
 declarations: [RegisterPage],
14
})
15
export class RegisterPageModule {}
`
Now we define our form just like before, and in the `createAccount()` we use the functionality of our initially created service to sign up a user.
Bring up the **src/app/pages/register/register.page.ts** and change it to:
`
1
import { Component } from '@angular/core'
2
import { Validators, FormBuilder } from '@angular/forms'
3
import { LoadingController, AlertController, NavController } from '@ionic/angular'
4
import { AuthService } from 'src/app/services/auth.service'
56
@Component({
7
 selector: 'app-register',
8
 templateUrl: './register.page.html',
9
 styleUrls: ['./register.page.scss'],
10
})
11
export class RegisterPage {
12
 credentials = this.fb.nonNullable.group({
13
  email: ['', [Validators.required, Validators.email]],
14
  password: ['', [Validators.required, Validators.minLength(6)]],
15
 })
1617
 constructor(
18
  private fb: FormBuilder,
19
  private authService: AuthService,
20
  private loadingController: LoadingController,
21
  private alertController: AlertController,
22
  private navCtrl: NavController
23
 ) {}
2425
 get email() {
26
  return this.credentials.controls.email
27
 }
2829
 get password() {
30
  return this.credentials.controls.password
31
 }
3233
 async createAccount() {
34
  const loading = await this.loadingController.create()
35
  await loading.present()
3637
  this.authService.signUp(this.credentials.getRawValue()).then(async (data) => {
38
   await loading.dismiss()
3940
   if (data.error) {
41
    this.showAlert('Registration failed', data.error.message)
42
   } else {
43
    this.showAlert('Signup success', 'Please confirm your email now!')
44
    this.navCtrl.navigateBack('')
45
   }
46
  })
47
 }
4849
 async showAlert(title, msg) {
50
  const alert = await this.alertController.create({
51
   header: title,
52
   message: msg,
53
   buttons: ['OK'],
54
  })
55
  await alert.present()
56
 }
57
}
`
The view for that page follows the same structure as the login, so let's continue with the **src/app/pages/register/register.page.html** now:
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-buttons slot="start">
4
   <ion-back-button defaultHref="/"></ion-back-button>
5
  </ion-buttons>
6
  <ion-title>Supa Chat</ion-title>
7
 </ion-toolbar>
8
</ion-header>
910
<ion-content scrollY="false">
11
 <ion-card>
12
  <ion-card-content>
13
   <form (ngSubmit)="createAccount()" [formGroup]="credentials">
14
    <ion-item>
15
     <ion-label position="stacked">Your Email</ion-label>
16
     <ion-input
17
      type="email"
18
      inputmode="email"
19
      placeholder="Email"
20
      formControlName="email"
21
     ></ion-input>
22
     <ion-note slot="error" *ngIf="(email.dirty || email.touched) && email.errors"
23
      >Please insert a valid email</ion-note
24
     >
25
    </ion-item>
26
    <ion-item>
27
     <ion-label position="stacked">Password</ion-label>
28
     <ion-input type="password" placeholder="Password" formControlName="password"></ion-input>
29
     <ion-note
30
      slot="error"
31
      *ngIf="(password.dirty || password.touched) && password.errors?.required"
32
      >Please insert a password</ion-note
33
     >
34
     <ion-note
35
      slot="error"
36
      *ngIf="(password.dirty || password.touched) && password.errors?.minlength"
37
      >Minlength 6 characters</ion-note
38
     >
39
    </ion-item>
40
    <ion-button type="submit" expand="block" strong="true" [disabled]="!credentials.valid"
41
     >Create my account</ion-button
42
    >
43
   </form>
44
  </ion-card-content>
45
 </ion-card>
46
</ion-content>
`
And just like before we want to have the background image so also bring in the same snippet for styling the page into the **src/app/pages/register/register.page.scss** :
`
1
ion-content {
2
 --padding-top: 20%;
3
 --padding-start: 5%;
4
 --padding-end: 5%;
5
 --background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.7)),
6
  url('https://images.unsplash.com/photo-1508964942454-1a56651d54ac?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1035&q=80')
7
   no-repeat;
8
}
`
As a result, we have a clean registration page with decent error messages!
![Ionic Registration Page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fionic-registration-page.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Give the default registration process a try with another email, and you should see another user inside the **Authentication** area of your Supabase project as well as inside the `users` table inside the **Table Editor**.
Before we make the magic link authentication work on mobile devices, let's focus on the internal pages and functionality of our app.
## Implementing the Groups Page[#](https://supabase.com/blog/authentication-in-ionic-angular#implementing-the-groups-page)
The groups screen is the first "inside" screen, but it's not protected by default: On the login page we have the option to start without an account, so unauthorized users can enter this page - but they should only be allowed to see the chat groups, nothing more.
![App Groups Page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fionic-groups-page.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Authenticated users should have controls to create a new group and to sign out, but before we get to the UI we need a way to interact with our Supabase tables.
### Adding a Data Service[#](https://supabase.com/blog/authentication-in-ionic-angular#adding-a-data-service)
We already generated a service in the beginning, and here we can add the logic to create a connection to Supabase and a first function to create a new row in our `groups` table and to load all groups.
Creating a group requires just a title, and we can gather the user ID from our authentication service to then call the `insert()` function from the Supabase client to create a new record that we then return to the caller.
When we want to get a list of groups, we can use `select()` but since we have a [foreign key that references the users table](https://supabase.com/docs/reference/javascript/select?example=query-referenced-tables), we need to join that information so instead of just having the `creator` field we end up getting the actual email for that ID instead!
Go ahead now and start the **src/app/services/data.service.ts** like this:
`
1
/* eslint-disable @typescript-eslint/naming-convention */
2
import { Injectable } from '@angular/core'
3
import { SupabaseClient, createClient } from '@supabase/supabase-js'
4
import { Subject } from 'rxjs'
5
import { environment } from 'src/environments/environment'
67
const GROUPS_DB = 'groups'
8
const MESSAGES_DB = 'messages'
910
export interface Message {
11
 created_at: string
12
 group_id: number
13
 id: number
14
 text: string
15
 user_id: string
16
}
1718
@Injectable({
19
 providedIn: 'root',
20
})
21
export class DataService {
22
 private supabase: SupabaseClient
2324
 constructor() {
25
  this.supabase = createClient(environment.supabaseUrl, environment.supabaseKey)
26
 }
2728
 getGroups() {
29
  return this.supabase
30
   .from(GROUPS_DB)
31
   .select(`title,id, users:creator ( email )`)
32
   .then((result) => result.data)
33
 }
3435
 async createGroup(title) {
36
  const newgroup = {
37
   creator: (await this.supabase.auth.getUser()).data.user.id,
38
   title,
39
  }
4041
  return this.supabase.from(GROUPS_DB).insert(newgroup).select().single()
42
 }
43
}
`
Nothing fancy, so let's move on to the UI of the groups page.
### Creating the Groups Page[#](https://supabase.com/blog/authentication-in-ionic-angular#creating-the-groups-page)
When we enter our page, we first load all groups through our service using the `ionViewWillEnter` Ionic lifecycle event.
The function to create a group follows the same logic as our alerts before where we have one input field that can be accessed in the handler of a button.
At that point, we will create a new group with the information, but also reload our list of groups and then navigate a user directly into the new group by using the ID of that created record.
This will then bring a user to the messages page since we defined the route "/groups/:groupid" initially in our routing!
Now go ahead and bring up the **src/app/pages/groups/groups.page.ts** and change it to:
`
1
import { Router } from '@angular/router'
2
import { AuthService } from './../../services/auth.service'
3
import { AlertController, NavController, LoadingController } from '@ionic/angular'
4
import { DataService } from './../../services/data.service'
5
import { Component, OnInit } from '@angular/core'
67
@Component({
8
 selector: 'app-groups',
9
 templateUrl: './groups.page.html',
10
 styleUrls: ['./groups.page.scss'],
11
})
12
export class GroupsPage implements OnInit {
13
 user = this.authService.getCurrentUser()
14
 groups = []
1516
 constructor(
17
  private authService: AuthService,
18
  private data: DataService,
19
  private alertController: AlertController,
20
  private loadingController: LoadingController,
21
  private navController: NavController,
22
  private router: Router
23
 ) {}
2425
 ngOnInit() {}
2627
 async ionViewWillEnter() {
28
  this.groups = await this.data.getGroups()
29
 }
3031
 async createGroup() {
32
  const alert = await this.alertController.create({
33
   header: 'Start Chat Group',
34
   message: 'Enter a name for your group. Note that all groups are public in this app!',
35
   inputs: [
36
    {
37
     type: 'text',
38
     name: 'title',
39
     placeholder: 'My cool group',
40
    },
41
   ],
42
   buttons: [
43
    {
44
     text: 'Cancel',
45
     role: 'cancel',
46
    },
47
    {
48
     text: 'Create group',
49
     handler: async (data) => {
50
      const loading = await this.loadingController.create()
51
      await loading.present()
5253
      const newGroup = await this.data.createGroup(data.title)
54
      if (newGroup) {
55
       this.groups = await this.data.getGroups()
56
       await loading.dismiss()
5758
       this.router.navigateByUrl(`/groups/${newGroup.data.id}`)
59
      }
60
     },
61
    },
62
   ],
63
  })
6465
  await alert.present()
66
 }
6768
 signOut() {
69
  this.authService.signOut()
70
 }
7172
 openLogin() {
73
  this.navController.navigateBack('/')
74
 }
75
}
`
The UI of that page is rather simple since we can iterate those groups in a list and create an item with their title and the creator email easily.
Because unauthenticated users can enter this page as well we add checks to the `user` Observable to the buttons so only authenticated users see the FAB at the bottom and have the option to sign out!
Remember that protecting the UI of our page is just one piece of the puzzle, **real security is implemented at the server level**!
In our case, we did this through the RLS we defined in the beginning.
Continue with the **src/app/pages/groups/groups.page.html** now and change it to:
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-title>Supa Chat Groups</ion-title>
4
  <ion-buttons slot="end">
5
   <ion-button (click)="signOut()" *ngIf="user | async">
6
    <ion-icon name="log-out-outline" slot="icon-only"></ion-icon>
7
   </ion-button>
89
   <ion-button (click)="openLogin()" *ngIf="(user | async) === false"> Sign in </ion-button>
10
  </ion-buttons>
11
 </ion-toolbar>
12
</ion-header>
1314
<ion-content>
15
 <ion-list>
16
  <ion-item *ngFor="let group of groups" [routerLink]="[group.id]" button>
17
   <ion-label
18
    >{{group.title }}
19
    <p>By {{group.users.email}}</p>
20
   </ion-label>
21
  </ion-item>
22
 </ion-list>
23
 <ion-fab vertical="bottom" horizontal="end" slot="fixed" *ngIf="user | async">
24
  <ion-fab-button (click)="createGroup()">
25
   <ion-icon name="add"></ion-icon>
26
  </ion-fab-button>
27
 </ion-fab>
28
</ion-content>
`
At this point, you should be able to create your own chat groups, and you should be brought to the page automatically or also enter it from the list manually afterward.
Inside the ULR you should see the ID of that group - and that's all we need to retrieve information about it and build a powerful chat view now!
## Building the Chat Page with Realtime Feature[#](https://supabase.com/blog/authentication-in-ionic-angular#building-the-chat-page-with-realtime-feature)
We left out realtime features on the groups page so we manually need to load the lists again, but only to keep the tutorial a bit shorter.
Because now on our messages page we want to have that functionality, and because **we enabled the publication** for the `messages` table through SQL in the beginning we are already prepared.
To get started we need some more functions in our service, and we add another `realtimeChannel` variable.
Additionally, we now want to retrieve group information by ID (_from the URL!_), add messages to the `messages` table and retrieve the last 25 messages.
All of that is pretty straightforward, and the only fancy function is `listenToGroup()` which returns an Observable of changes.
We can create this on our own by handling `postgres_changes` events `on` the `messages` table. Inside the callback function, we can handle all CRUD events, but in our case, we will (for simplicity) only handle the case of an added record.
That means when a message is added to the table, we want to return that new record to whoever is subscribed to this channel - but because a message has the user as a foreign key we first need to make another call to the `messages` table to retrieve the right information and then **emit the new value on our Subject**.
For all of that bring up the **src/app/services/data.service.ts** and change it to:
`
1
/* eslint-disable @typescript-eslint/naming-convention */
2
import { Injectable } from '@angular/core'
3
import { SupabaseClient, createClient, RealtimeChannel } from '@supabase/supabase-js'
4
import { Subject } from 'rxjs'
5
import { environment } from 'src/environments/environment'
67
const GROUPS_DB = 'groups'
8
const MESSAGES_DB = 'messages'
910
export interface Message {
11
 created_at: string
12
 group_id: number
13
 id: number
14
 text: string
15
 user_id: string
16
}
1718
@Injectable({
19
 providedIn: 'root',
20
})
21
export class DataService {
22
 private supabase: SupabaseClient
23
 // ADD
24
 private realtimeChannel: RealtimeChannel
2526
 constructor() {
27
  this.supabase = createClient(environment.supabaseUrl, environment.supabaseKey)
28
 }
2930
 getGroups() {
31
  return this.supabase
32
   .from(GROUPS_DB)
33
   .select(`title,id, users:creator ( email )`)
34
   .then((result) => result.data)
35
 }
3637
 async createGroup(title) {
38
  const newgroup = {
39
   creator: (await this.supabase.auth.getUser()).data.user.id,
40
   title,
41
  }
4243
  return this.supabase.from(GROUPS_DB).insert(newgroup).select().single()
44
 }
4546
 // ADD NEW FUNCTIONS
47
 getGroupById(id) {
48
  return this.supabase
49
   .from(GROUPS_DB)
50
   .select(`created_at, title, id, users:creator ( email, id )`)
51
   .match({ id })
52
   .single()
53
   .then((result) => result.data)
54
 }
5556
 async addGroupMessage(groupId, message) {
57
  const newMessage = {
58
   text: message,
59
   user_id: (await this.supabase.auth.getUser()).data.user.id,
60
   group_id: groupId,
61
  }
6263
  return this.supabase.from(MESSAGES_DB).insert(newMessage)
64
 }
6566
 getGroupMessages(groupId) {
67
  return this.supabase
68
   .from(MESSAGES_DB)
69
   .select(`created_at, text, id, users:user_id ( email, id )`)
70
   .match({ group_id: groupId })
71
   .limit(25) // Limit to 25 messages for our app
72
   .then((result) => result.data)
73
 }
7475
 listenToGroup(groupId) {
76
  const changes = new Subject()
7778
  this.realtimeChannel = this.supabase
79
   .channel('public:messages')
80
   .on(
81
    'postgres_changes',
82
    { event: '*', schema: 'public', table: 'messages' },
83
    async (payload) => {
84
     console.log('DB CHANGE: ', payload)
8586
     if (payload.new && (payload.new as Message).group_id === +groupId) {
87
      const msgId = (payload.new as any).id
8889
      const msg = await this.supabase
90
       .from(MESSAGES_DB)
91
       .select(`created_at, text, id, users:user_id ( email, id )`)
92
       .match({ id: msgId })
93
       .single()
94
       .then((result) => result.data)
95
      changes.next(msg)
96
     }
97
    }
98
   )
99
   .subscribe()
100101
  return changes.asObservable()
102
 }
103104
 unsubscribeGroupChanges() {
105
  if (this.realtimeChannel) {
106
   this.supabase.removeChannel(this.realtimeChannel)
107
  }
108
 }
109
}
`
By handling the realtime logic here and only returning an Observable we make it super easy for our view.
The next step is to load the group information by accessing the `groupid` from the URL, then getting the last 25 messages and finally subscribing to `listenToGroup()` and pushing every new message into our local `messages` array.
After the view is initialized we can also scroll to the bottom of our `ion-content` to show the latest message.
Finally, we need to make sure we end our realtime listening when we leave the page or the page is destroyed.
Bring up the **src/app/pages/messages/messages.page.ts** and change it to:
`
1
import { AuthService } from './../../services/auth.service'
2
import { DataService } from './../../services/data.service'
3
import { AfterViewInit, Component, OnDestroy, OnInit, ViewChild } from '@angular/core'
4
import { ActivatedRoute } from '@angular/router'
5
import { IonContent } from '@ionic/angular'
67
@Component({
8
 selector: 'app-messages',
9
 templateUrl: './messages.page.html',
10
 styleUrls: ['./messages.page.scss'],
11
})
12
export class MessagesPage implements OnInit, AfterViewInit, OnDestroy {
13
 @ViewChild(IonContent) content: IonContent
14
 group = null
15
 messages = []
16
 currentUserId = null
17
 messageText = ''
1819
 constructor(
20
  private route: ActivatedRoute,
21
  private data: DataService,
22
  private authService: AuthService
23
 ) {}
2425
 async ngOnInit() {
26
  const groupid = this.route.snapshot.paramMap.get('groupid')
27
  this.group = await this.data.getGroupById(groupid)
28
  this.currentUserId = this.authService.getCurrentUserId()
29
  this.messages = await this.data.getGroupMessages(groupid)
30
  this.data.listenToGroup(groupid).subscribe((msg) => {
31
   this.messages.push(msg)
32
   setTimeout(() => {
33
    this.content.scrollToBottom(200)
34
   }, 100)
35
  })
36
 }
3738
 ngAfterViewInit(): void {
39
  setTimeout(() => {
40
   this.content.scrollToBottom(200)
41
  }, 300)
42
 }
4344
 loadMessages() {}
4546
 async sendMessage() {
47
  await this.data.addGroupMessage(this.group.id, this.messageText)
48
  this.messageText = ''
49
 }
5051
 ngOnDestroy(): void {
52
  this.data.unsubscribeGroupChanges()
53
 }
54
}
`
That's all we need to handle realtime logic and add new messages to our Supabase table!
Sometimes life can be that easy.
For the view of that page, we need to distinguish between messages we sent, and messages sent from other users.
We can achieve this by comparing the user ID of a message with our currently authenticated user id, and we position our messages with an `offset` of 2 so they appear on the right hand side of the screen with a slightly different styling.
For this, open up the **src/app/pages/messages/messages.page.html** and change it to:
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-buttons slot="start">
4
   <ion-back-button defaultHref="/groups"></ion-back-button>
5
  </ion-buttons>
6
  <ion-title>{{ group?.title}}</ion-title>
7
 </ion-toolbar>
8
</ion-header>
910
<ion-content class="ion-padding">
11
 <ion-row *ngFor="let message of messages">
12
  <ion-col size="10" *ngIf="message.users.id !== currentUserId" class="message other-message">
13
   <span>{{ message.text }} </span>
1415
   <div class="time ion-text-right"><br />{{ message.created_at | date:'shortTime' }}</div>
16
  </ion-col>
1718
  <ion-col
19
   offset="2"
20
   size="10"
21
   *ngIf="message.users.id === currentUserId"
22
   class="message my-message"
23
  >
24
   <span>{{ message.text }} </span>
25
   <div class="time ion-text-right"><br />{{ message.created_at | date:'shortTime' }}</div>
26
  </ion-col>
27
 </ion-row>
28
</ion-content>
2930
<ion-footer>
31
 <ion-toolbar color="light">
32
  <ion-row class="ion-align-items-center">
33
   <ion-col size="10">
34
    <ion-textarea
35
     class="message-input"
36
     autoGrow="true"
37
     rows="1"
38
     [(ngModel)]="messageText"
39
    ></ion-textarea>
40
   </ion-col>
41
   <ion-col size="2" class="ion-text-center">
42
    <ion-button fill="clear" (click)="sendMessage()">
43
     <ion-icon slot="icon-only" name="send-outline" color="primary" size="large"></ion-icon>
44
    </ion-button>
45
   </ion-col>
46
  </ion-row>
47
 </ion-toolbar>
48
</ion-footer>
`
For an even more advanced chat UI chat out the examples of [Built with Ionic](https://builtwithionic.com/)!
Now we can add the finishing touches to that screen with some CSS to give the page a background pattern image and styling for the messages inside the **src/app/pages/messages/messages.page.scss** :
`
1
ion-content {
2
 --background: url('../../../assets/pattern.png') no-repeat;
3
}
45
.message-input {
6
 border: 1px solid #c3c3c3;
7
 border-radius: 20px;
8
 background: #fff;
9
 box-shadow: 2px 2px 5px 0px rgb(0 0 0 / 5%);
10
}
1112
ion-textarea {
13
 --padding-start: 20px;
14
 --padding-top: 4px;
15
 --padding-bottom: 4px;
1617
 min-height: 30px;
18
}
1920
.message {
21
 padding: 10px !important;
22
 border-radius: 10px !important;
23
 margin-bottom: 8px !important;
2425
 img {
26
  width: 100%;
27
 }
28
}
2930
.my-message {
31
 background: #dbf7c5;
32
 color: #000;
33
}
3435
.other-message {
36
 background: #fff;
37
 color: #000;
38
}
3940
.time {
41
 color: #cacaca;
42
 float: right;
43
 font-size: small;
44
}
`
You can [find the full code of this tutorial on Github](https://github.com/saimon24/supa-chat) including the file for that pattern so your page looks almost like WhatsApp!
![Ionic Supabase Chat Page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fionic-supabase-chat-page.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Now we have a well-working Ionic app with Supabase authentication and database integration, but there are two small but important additions we still need to make.
## Protecting internal Pages[#](https://supabase.com/blog/authentication-in-ionic-angular#protecting-internal-pages)
Right now everyone could access the messages page, but we wanted to make this page only available for authenticated users.
To protect the page (and all other pages you might want to protect) we now implement the **guard** that we generated in the beginning.
That guard will check the Observable of our service, filter out the initial state and then see if a user is allowed to access a page or not.
Bring up our **src/app/guards/auth.guard.ts** and change it to this:
`
1
import { AuthService } from './../services/auth.service'
2
import { Injectable } from '@angular/core'
3
import { ActivatedRouteSnapshot, CanActivate, Router, UrlTree } from '@angular/router'
4
import { Observable } from 'rxjs'
5
import { filter, map, take } from 'rxjs/operators'
6
import { ToastController } from '@ionic/angular'
78
@Injectable({
9
 providedIn: 'root',
10
})
11
export class AuthGuard implements CanActivate {
12
 constructor(
13
  private auth: AuthService,
14
  private router: Router,
15
  private toastController: ToastController
16
 ) {}
1718
 canActivate(route: ActivatedRouteSnapshot): Observable<boolean | UrlTree> {
19
  return this.auth.getCurrentUser().pipe(
20
   filter((val) => val !== null), // Filter out initial Behavior subject value
21
   take(1), // Otherwise the Observable doesn't complete!
22
   map((isAuthenticated) => {
23
    if (isAuthenticated) {
24
     return true
25
    } else {
26
     this.toastController
27
      .create({
28
       message: 'You are not allowed to access this!',
29
       duration: 2000,
30
      })
31
      .then((toast) => toast.present())
3233
     return this.router.createUrlTree(['/groups'])
34
    }
35
   })
36
  )
37
 }
38
}
`
In case the user is not allowed to activate a page, we display a toast and at the same time route to the groups page since that page is visible to everyone. Normally you might even bring users simply back to the login screen if you wanted to protect all internal pages of your Ionic app.
![Ionic unauthorized message](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fionic-supabase-unauthorized.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
We already applied this guard to our routing in the beginning, but now it finally serves the real purpose!
## Magic Links for Native Apps[#](https://supabase.com/blog/authentication-in-ionic-angular#magic-links-for-native-apps)
At last, we come to a challenging topic, which is handling the magic link on a mobile phone.
The problem is, that the link that a user receives has a callback to a URL, but if you open that link in your email client on a phone it's not opening your native app!
But we can change this by defining a **custom URL scheme** for our app like "supachat://", and then use that URL as the callback URL for magic link authentication.
First, make sure you add the native platforms with [Capacitor](https://capacitorjs.com/) to your project:
`
1
ionic build
2
ionic cap add ios
3
ionic cap add android
`
Inside the new native projects we need to define the URL scheme, so for iOS bring up the **ios/App/App/Info.plist** and insert another block:
`
1
	<key>CFBundleURLTypes</key>
2
		<array>
3
			<dict>
4
				<key>CFBundleURLSchemes</key>
5
				<array>
6
					<string>supachat</string>
7
				</array>
8
			</dict>
9
		</array>
`
For Android, we first define a new string inside the **android/app/src/main/res/values/strings.xml** :
`
1
<string name="custom_url_scheme">supachat</string>
`
Now we can update the **android/app/src/main/AndroidManifest.xml** and add an `intent-filter` inside which uses the `custom_url_scheme` value:
`
1
<intent-filter android:autoVerify="true">
2
  <action android:name="android.intent.action.VIEW" />
3
  <category android:name="android.intent.category.DEFAULT" />
4
  <category android:name="android.intent.category.BROWSABLE" />
5
  <data android:scheme="@string/custom_url_scheme" />
6
</intent-filter>
`
By default, Supabase will use the host for the redirect URL, which works great if the request comes from a website.
That means we only want to change the behavior for native apps, so we can use the `isPlatform()` check in our app and use `"supachat://login"`as the redirect URL instead.
For this, bring up the **src/app/services/auth.service.ts** and update our `signInWithEmail` and add another new function:
`
1
 signInWithEmail(email: string) {
2
  const redirectTo = isPlatform("capacitor")
3
   ? "supachat://login"
4
   : `${window.location.origin}/groups`;
56
  return this.supabase.auth.signInWithOtp({
7
   email,
8
   options: { emailRedirectTo: redirectTo },
9
  });
10
 }
1112
 async setSession(access_token, refresh_token) {
13
  return this.supabase.auth.setSession({ access_token, refresh_token });
14
 }
`
This second function is required since we need to manually set our session based on the other tokens of the magic link URL.
If we now click on the link in an email, it will open the browser the first time but then asks if we want to open our native app.
This is cool, but it's not loading the user information correctly, but we can easily do this manually!
Eventually, our app is opened with an URL that looks like this:
`
1
supachat://login#access_token=A-TOKEN&expires_in=3600&refresh_token=REF-TOKEN&token_type=bearer&type=magiclink
`
To set our session we now simply need to extract the `access_token` and `refresh_token` from that URL, and we can do this by adding a listener to the `appUrlOpen` event of the [Capacitor app plugin](https://capacitorjs.com/docs/apis/app).
Once we got that information we can call the `setSession` function that we just added to our service, and then route the user forward to the groups page!
To achieve this, bring up the **src/app/app.component.ts** and change it to:
`
1
import { AuthService } from 'src/app/services/auth.service'
2
import { Router } from '@angular/router'
3
import { Component, NgZone } from '@angular/core'
4
import { App, URLOpenListenerEvent } from '@capacitor/app'
56
@Component({
7
 selector: 'app-root',
8
 templateUrl: 'app.component.html',
9
 styleUrls: ['app.component.scss'],
10
})
11
export class AppComponent {
12
 constructor(
13
  private zone: NgZone,
14
  private router: Router,
15
  private authService: AuthService
16
 ) {
17
  this.setupListener()
18
 }
1920
 setupListener() {
21
  App.addListener('appUrlOpen', async (data: URLOpenListenerEvent) => {
22
   console.log('app opened with URL: ', data)
2324
   const openUrl = data.url
25
   const access = openUrl.split('#access_token=').pop().split('&')[0]
26
   const refresh = openUrl.split('&refresh_token=').pop().split('&')[0]
2728
   await this.authService.setSession(access, refresh)
2930
   this.zone.run(() => {
31
    this.router.navigateByUrl('/groups', { replaceUrl: true })
32
   })
33
  })
34
 }
35
}
`
If you would run the app now it still wouldn't work, because we haven't added our custom URL scheme as an allowed URL for redirecting to!
To finish this open your Supabase project again and go to the **Settings** of the **Authentication** menu entry where you can add a domain under **Redirect URLs** :
![Supabase Auth Redirect URL](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fsimmon-grim-ionic-angular-authentication%2Fsupabase-auth-redirect-url.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
This was the last missing piece, and now you even got seamless Supabase authentication with magic links working inside your iOS and Android app!
## Conclusion[#](https://supabase.com/blog/authentication-in-ionic-angular#conclusion)
We've come a long way and covered everything from setting up tables, to defining policies to protect data, and handling authentication in Ionic Angular applications.
You can [find the full code of this tutorial on Github](https://github.com/saimon24/supa-chat) where you just need to insert your own Supabase instance and then create the tables with the included SQL file, plus updating the authentication settings as we did in the tutorial
Although we can now use magic link auth, something probably even better fitting for native apps would be [phone auth with Twilio](https://supabase.com/docs/guides/auth/phone-login/twilio) that's also easily possible with Supabase - just like tons of other authentication providers!
Protecting your Ionic Angular app with Supabase is a breeze, and through the security rules, you can make sure your data and tables are protected in the best possible way.
If you enjoyed the tutorial, you can [find many more tutorials on my YouTube channel](https://www.youtube.com/simongrimmdev_) where I help web developers build awesome mobile apps.
Until next time and happy coding with Supabase!
Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fauthentication-in-ionic-angular&text=Authentication%20in%20Ionic%20Angular%20with%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fauthentication-in-ionic-angular&text=Authentication%20in%20Ionic%20Angular%20with%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fauthentication-in-ionic-angular&t=Authentication%20in%20Ionic%20Angular%20with%20Supabase)
[Last postFetching and caching Supabase data in Next.js 13 Server Components17 November 2022](https://supabase.com/blog/fetching-and-caching-supabase-data-in-next-js-server-components)
[Next postSupabase Beta October 20222 November 2022](https://supabase.com/blog/supabase-beta-update-october-2022)
[ionic](https://supabase.com/blog/tags/ionic)[angular](https://supabase.com/blog/tags/angular)[community](https://supabase.com/blog/tags/community)
On this page
  * [Creating the Supabase Project](https://supabase.com/blog/authentication-in-ionic-angular#creating-the-supabase-project)
  * [Defining your Tables with SQL](https://supabase.com/blog/authentication-in-ionic-angular#defining-your-tables-with-sql)
  * [Creating the Ionic Angular App](https://supabase.com/blog/authentication-in-ionic-angular#creating-the-ionic-angular-app)
  * [Building the Public Pages of our App](https://supabase.com/blog/authentication-in-ionic-angular#building-the-public-pages-of-our-app)
  * [Implementing the Groups Page](https://supabase.com/blog/authentication-in-ionic-angular#implementing-the-groups-page)
  * [Building the Chat Page with Realtime Feature](https://supabase.com/blog/authentication-in-ionic-angular#building-the-chat-page-with-realtime-feature)
  * [Protecting internal Pages](https://supabase.com/blog/authentication-in-ionic-angular#protecting-internal-pages)
  * [Magic Links for Native Apps](https://supabase.com/blog/authentication-in-ionic-angular#magic-links-for-native-apps)
  * [Conclusion](https://supabase.com/blog/authentication-in-ionic-angular#conclusion)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fauthentication-in-ionic-angular&text=Authentication%20in%20Ionic%20Angular%20with%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fauthentication-in-ionic-angular&text=Authentication%20in%20Ionic%20Angular%20with%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fauthentication-in-ionic-angular&t=Authentication%20in%20Ionic%20Angular%20with%20Supabase)
## Build in a weekend, scale to millions
[Start your project](https://supabase.com/dashboard)[Request a demo](https://supabase.com/contact/sales)
## Footer
We protect your data.[More on Security](https://supabase.com/security)
  * SOC2 Type 2 Certified
  * HIPAA Compliant


[![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--light.daaeffd3.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)![Supabase Logo](https://supabase.com/_next/image?url=https%3A%2F%2Ffrontend-assets.supabase.com%2Fwww%2Fd218d9190b87%2F_next%2Fstatic%2Fmedia%2Fsupabase-logo-wordmark--dark.b36ebb5f.png&w=384&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)](https://supabase.com/)
[Twitter](https://twitter.com/supabase)[GitHub](https://github.com/supabase)[Discord](https://discord.supabase.com/)[Youtube](https://youtube.com/c/supabase)
###### Product
  * [Database](https://supabase.com/database)
  * [Auth](https://supabase.com/auth)
  * [Functions](https://supabase.com/edge-functions)
  * [Realtime](https://supabase.com/realtime)
  * [Storage](https://supabase.com/storage)
  * [Vector](https://supabase.com/modules/vector)
  * [Cron](https://supabase.com/modules/cron)
  * [Pricing](https://supabase.com/pricing)
  * [Launch Week](https://supabase.com/launch-week)
  * [AI Builders](https://supabase.com/solutions/ai-builders)


###### Resources
  * [Support](https://supabase.com/support)
  * [System Status](https://status.supabase.com/)
  * [Become a Partner](https://supabase.com/partners)
  * [Integrations](https://supabase.com/partners/integrations)
  * [Brand Assets / Logos](https://supabase.com/brand-assets)
  * [Security and Compliance](https://supabase.com/security)
  * [DPA](https://supabase.com/legal/dpa)
  * [SOC2](https://supabase.com/security)
  * [HIPAA](https://forms.supabase.com/hipaa2)


###### Developers
  * [Documentation](https://supabase.com/docs)
  * [Supabase UI](https://supabase.com/ui)
  * [Changelog](https://supabase.com/changelog)
  * [Contributing](https://github.com/supabase/supabase/blob/master/CONTRIBUTING.md)
  * [Open Source](https://supabase.com/open-source)
  * [SupaSquad](https://supabase.com/supasquad)
  * [DevTo](https://dev.to/supabase)
  * [RSS](https://supabase.com/rss.xml)


###### Company
  * [Blog](https://supabase.com/blog)
  * [Customer Stories](https://supabase.com/customers)
  * [Careers](https://supabase.com/careers)
  * [Company](https://supabase.com/company)
  * [Events & Webinars](https://supabase.com/events)
  * [General Availability](https://supabase.com/ga)
  * [Terms of Service](https://supabase.com/terms)
  * [Privacy Policy](https://supabase.com/privacy)
  * Privacy Settings
  * [Acceptable Use Policy](https://supabase.com/aup)
  * [Support Policy](https://supabase.com/support-policy)
  * [Service Level Agreement](https://supabase.com/sla)
  * [Humans.txt](https://supabase.com/humans.txt)
  * [Lawyers.txt](https://supabase.com/lawyers.txt)
  * [Security.txt](https://supabase.com/.well-known/security.txt)


© Supabase Inc
Toggle theme

