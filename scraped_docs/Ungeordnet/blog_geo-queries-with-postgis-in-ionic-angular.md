---
url: https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular
scraped_at: 2025-05-25T09:13:45.726039
title: Geo Queries with PostGIS in Ionic Angular
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
# Geo Queries with PostGIS in Ionic Angular
01 Mar 2023
•
32 minute read
[![Simon Grimm avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaimon24.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Simon GrimmGuest Author](https://twitter.com/schlimmson)
![Geo Queries with PostGIS in Ionic Angular](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-28-geoqueries-postgis%2Fpostgis-ionic-angular.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Does your app need to handle geo data like latitude, longitude, or distance between geographic locations?
Then Supabase got you covered again as you can unlock all of this with the **PostGIS** extension!
![Supabase Postgis app Ionic](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-28-geoqueries-postgis%2Fsupabase-gis.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
In this tutorial you will learn to:
  * Enable and use PostGIS extension with Supabase
  * Store and retrieve geolocation data
  * Use [database functions](https://supabase.com/docs/guides/database/functions) for geo-queries with PostGIS
  * Display a [Capacitor Google Map](https://capacitorjs.com/docs/apis/google-maps) with a marker
  * Upload files to Supabase Storage and use [image transformations](https://supabase.com/docs/guides/storage/serving/image-transformations)


Since there are quite some code snippets we need I've put together the [full source code on Github](https://github.com/saimon24/supabase-postgis-ionic-angular) so you can easily run the project yourself!
Ready for some action?
Let's start within Supabase.
## Creating the Supabase Project[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#creating-the-supabase-project)
To get started we need a new Supabase project. If you don't have a Supabase account yet, you can [get started for free](https://supabase.com/)!
In your dashboard, click "New Project" and leave it to the default settings, but make sure you keep a copy o your Database password!
![Supabase new project](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-28-geoqueries-postgis%2Fsupabase-project-setup.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
After a minute your project should be ready, and we can configure our tables and extensions with SQL.
## Why PostGIS Extension?[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#why-postgis-extension)
Why do we actually need the [PostGIS](https://postgis.net/) extension for our Postgres database?
Turns out storing lat/long coordinates and querying them isn't very effective and doesn't scale well.
By enabling this extension, we get access to additional data types like `Point` or `Polygon`, and we can easily add an index to our data that makes retrieving locations within certain bounds super simpler.
It's super easy to use [PostGIS with Supabase](https://supabase.com/docs/guides/database/extensions/postgis) as we just need to enable the extension - which is just one of many other Postgres extensions that you can toggle on with just a click!
## Defining your Tables with SQL[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#defining-your-tables-with-sql)
### Adding the PostGIS Extensions[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#adding-the-postgis-extensions)
We could enable PostGIS from the Supabase project UI but we can actually do it with `SQL` as well, so let's navigate to the **SQL Editor** from the menu and run the following:
`
1
-- enable the PostGIS extension
2
create extension postgis with schema extensions;
`
You can now find this and many other extensions under **Database** -> **Extensions** :
![Supabase extensions](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-28-geoqueries-postgis%2Fsupabase-extensions.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
It's as easy as that, and we can now create the rest of our table structure.
### Creating the SQL Tables[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#creating-the-sql-tables)
For our example, we need one `Stores` table so we can add stores with some text and their location.
Additionally, we create a [spartial index](https://postgis.net/docs/using_postgis_dbmanagement.html#build-indexes) on the location of our store to make our queries more performant.
Finally, we can also create a new storage bucket for file upload, so go ahead and run the following in the **SQL Editor** :
`
1
-- create our table
2
create table if not exists public.stores (
3
	id int generated by default as identity primary key,
4
	name text not null,
5
 description text,
6
	location geography(POINT) not null
7
);
89
-- add the spatial index
10
create index stores_geo_index
11
 on public.stores
12
 using GIST (location);
1314
-- create a storage bucket and allow file upload/download
15
insert into storage.buckets (id, name)
16
values ('stores', 'stores');
1718
CREATE POLICY "Select images" ON storage.objects FOR SELECT TO public USING (bucket_id = 'stores');
19
CREATE POLICY "Upload images" ON storage.objects FOR INSERT TO public WITH CHECK (bucket_id = 'stores');
`
For our tests, I also added some dummy data. Feel free to use mine or use coordinates closer to you:
`
1
-- add some dummy data
2
insert into public.stores
3
 (name, description, location)
4
values
5
 (
6
  'The Galaxies.dev Shop',
7
  'Galaxies.dev - your favourite place to learn',
8
  st_point(7.6005702, 51.8807174)
9
 ),
10
 ('The Local Dev', 'Local people, always best', st_point(7.614454, 51.876565)),
11
 ('City Store', 'Get the supplies a dev needs', st_point(7.642581, 51.945606)),
12
 ('MEGA Store', 'Everything you need', st_point(13.404315, 52.511640));
`
To wrap this up we define 2 database functions:
  * `nearby_stores` will return a list of all stores and their distance to a lat/long place
  * `stores_in_view` uses more functions like `ST_MakeBox2D` to find all locations in a specific box of coordinates


Those are some powerful calculations, and we can easily use them through the PostGIS extension and by defining database functions like this:
`
1
-- create database function to find nearby stores
2
create or replace function nearby_stores(lat float, long float)
3
returns table (id public.stores.id%TYPE, name public.stores.name%TYPE, description public.stores.description%TYPE, lat float, long float, dist_meters float)
4
language sql
5
as $$
6
 select id, name, description, st_y(location::geometry) as lat, st_x(location::geometry) as long, st_distance(location, st_point(long, lat)::geography) as dist_meters
7
 from public.stores
8
 order by location <-> st_point(long, lat)::geography;
9
$$;
101112
-- create database function to find stores in a specific box
13
create or replace function stores_in_view(min_lat float, min_long float, max_lat float, max_long float)
14
returns table (id public.stores.id%TYPE, name public.stores.name%TYPE, lat float, long float)
15
language sql
16
as $$
17
	select id, name, ST_Y(location::geometry) as lat, ST_X(location::geometry) as long
18
	from public.stores
19
	where location && ST_SetSRID(ST_MakeBox2D(ST_Point(min_long, min_lat), ST_Point(max_long, max_lat)),4326)
20
$$;
`
With all of that in place we are ready to build a powerful app with geo-queries based on our Supabase geolocation data!
## Working with Geo Queries in Ionic Angular[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#working-with-geo-queries-in-ionic-angular)
### Setting up the Project[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#setting-up-the-project)
We are not bound to any framework, but in this article, we are using [Ionic Angular](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular) to build a cross-platform application.
Additionally we use [Capacitor](https://capacitorjs.com/) to include a [native Google Maps](https://capacitorjs.com/docs/apis/google-maps) component and to retrieve the user location.
Get started by bringing up a new Ionic project, then add two pages and a service and run the first build so we can generate the native platforms with Capacitor.
Finally we can install the [Supabase JS package](https://github.com/supabase/supabase-js), so go ahead and run:
`
1
ionic start supaMap blank --type=angular
2
cd ./supaMap
34
ionic g page store
5
ionic g page nearby
6
ionic g service services/stores
78
ionic build
9
ionic cap add ios
10
ionic cap add android
111213
# Add Maps and Geolocation plugins
14
npm install @capacitor/google-maps
15
npm install @capacitor/geolocation
1617
# Install Supabase
18
npm install @supabase/supabase-js
1920
# Ionic 7 wasn't released so I installed the next version
21
# not required if you are already on Ionic 7
22
npm install @ionic/core@next @ionic/angular@next
`
Within the new project we need to add our Supabase credentials and a key for the Google Maps API to the **src/environments/environment.ts** like this:
`
1
export const environment = {
2
 production: false,
3
 mapsKey: 'YOUR-GOOGLE-MAPS-KEY',
4
 supabaseUrl: 'YOUR-URL',
5
 supabaseKey: 'YOUR-ANON-KEY',
6
}
`
You can find those values in your Supabase project by clicking on the **Settings** icon and then navigating to **API** where it shows your **Project API keys**.
The Google Maps API key can be obtained from the [Google Cloud Platform](https://console.cloud.google.com/) where you can add a new project and then create credentials for the Maps Javascript API.
### Native Project Configuration[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#native-project-configuration)
To use the Capacitor plugin we also need to update the permissions of our native projects, so within the **ios/App/App/Info.plist** we need to include these:
`
1
	<key>NSLocationAlwaysUsageDescription</key>
2
		<string>We want to show your nearby places</string>
3
	<key>NSLocationWhenInUseUsageDescription</key>
4
		<string>We want to show your nearby places</string>
5
	<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
6
	 <string>To show your location</string>
`
Additionally, we need to add our Maps Key to the **android/app/src/main/AndroidManifest.xml** :
`
1
<meta-data android:name="com.google.android.geo.API_KEY" android:value="YOUR_API_KEY_HERE"/>
`
Finally also add the required permissions for Android in the **android/app/src/main/AndroidManifest.xml** at the bottom:
`
1
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
2
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
3
<uses-feature android:name="android.hardware.location.gps" />
`
You can also find more information about using [Capacitor maps with Ionic in my Ionic Academy](https://ionicacademy.com/capacitor-google-maps-plugin/)!
### Finding Nearby Places with Database Functions[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#finding-nearby-places-with-database-functions)
Now the fun begins, and we can start by adding a function to our **src/app/services/stores.service.ts** that calls the database function (Remote Procedure Call) that we defined in the beginning:
`
1
import { Injectable } from '@angular/core'
2
import { DomSanitizer, SafeUrl } from '@angular/platform-browser'
3
import { SupabaseClient, User, createClient } from '@supabase/supabase-js'
4
import { environment } from 'src/environments/environment'
56
export interface StoreEntry {
7
 lat?: number
8
 long?: number
9
 name: string
10
 description: string
11
 image?: File
12
}
13
export interface StoreResult {
14
 id: number
15
 lat: number
16
 long: number
17
 name: string
18
 description: string
19
 image?: SafeUrl
20
 dist_meters?: number
21
}
22
@Injectable({
23
 providedIn: 'root',
24
})
25
export class StoresService {
26
 private supabase: SupabaseClient
2728
 constructor(private sanitizer: DomSanitizer) {
29
  this.supabase = createClient(environment.supabaseUrl, environment.supabaseKey)
30
 }
3132
 // Get all places with calculated distance
33
 async getNearbyStores(lat: number, long: number) {
34
  const { data, error } = await this.supabase.rpc('nearby_stores', {
35
   lat,
36
   long,
37
  })
38
  return data
39
 }
40
}
`
This should return a nice list of `StoreResult` items that we can render in a list.
For that, let's display a modal from our **src/app/home/home.page.ts** :
`
1
import { Component } from '@angular/core'
2
import { ModalController } from '@ionic/angular'
3
import { NearbyPage } from '../nearby/nearby.page'
45
export interface StoreMarker {
6
 markerId: string
7
 storeId: number
8
}
910
@Component({
11
 selector: 'app-home',
12
 templateUrl: 'home.page.html',
13
 styleUrls: ['home.page.scss'],
14
})
15
export class HomePage {
16
 constructor(private modalCtrl: ModalController) {}
1718
 async showNearby() {
19
  const modal = await this.modalCtrl.create({
20
   component: NearbyPage,
21
  })
22
  modal.present()
23
 }
24
}
`
We also need a button to present that modal, so change the **src/app/home/home.page.html** to include one:
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-buttons slot="start">
4
   <ion-button (click)="showNearby()">
5
    <ion-icon name="location" slot="start"></ion-icon> Nearby</ion-button
6
   >
7
  </ion-buttons>
89
  <ion-title> Supa Stores </ion-title>
10
 </ion-toolbar>
11
</ion-header>
1213
<ion-content> </ion-content>
`
Now we are able to use the `getNearbyStores` from our service on that modal page, and we also load the current user location using Capacitor.
Once we got the user coordinates, we pass them to our function and PostGIS will do its magic to calculate the distance between us and the stores of our database!
Go ahead and change the **src/app/nearby/nearby.page.ts** to this now:
`
1
import { Component, OnInit } from '@angular/core'
2
import { Geolocation } from '@capacitor/geolocation'
3
import { StoresService, StoreResult } from '../services/stores.service'
4
import { LoadingController, ModalController } from '@ionic/angular'
56
@Component({
7
 selector: 'app-nearby',
8
 templateUrl: './nearby.page.html',
9
 styleUrls: ['./nearby.page.scss'],
10
})
11
export class NearbyPage implements OnInit {
12
 stores: StoreResult[] = []
1314
 constructor(
15
  private storesService: StoresService,
16
  public modalCtrl: ModalController,
17
  private loadingCtrl: LoadingController
18
 ) {}
1920
 async ngOnInit() {
21
  // Show loading while getting data from Supabase
22
  const loading = await this.loadingCtrl.create({
23
   message: 'Loading nearby places...',
24
  })
25
  loading.present()
2627
  const coordinates = await Geolocation.getCurrentPosition()
2829
  if (coordinates) {
30
   // Get nearby places sorted by distance using PostGIS
31
   this.stores = await this.storesService.getNearbyStores(
32
    coordinates.coords.latitude,
33
    coordinates.coords.longitude
34
   )
35
   loading.dismiss()
36
  }
37
 }
38
}
`
At this point, you can already log the values, but we can also quickly display them in a nice list by updating the **src/app/nearby/nearby.page.html** to:
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-buttons slot="start">
4
   <ion-button (click)="modalCtrl.dismiss()">
5
    <ion-icon slot="icon-only" name="close"></ion-icon>
6
   </ion-button>
7
  </ion-buttons>
8
  <ion-title>Nearby Places</ion-title>
9
 </ion-toolbar>
10
</ion-header>
1112
<ion-content>
13
 <ion-list>
14
  <ion-item *ngFor="let store of stores">
15
   <ion-label>
16
    {{ store.name }}
17
    <p>{{store.description }}</p>
18
   </ion-label>
19
   <ion-note slot="end">{{store.dist_meters!/1000 | number:'1.0-2' }} km</ion-note>
20
  </ion-item>
21
 </ion-list>
22
</ion-content>
`
If you open the modal, you should now see a list like this after your position was loaded:
![Ionic nearby list](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-28-geoqueries-postgis%2Fionic-nearby.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
It looks so easy - but so many things are already coming together at this point:
  * Capacitor geolocation inside the browser
  * Supabase RPC to a stored database function
  * PostGIS geolocation calculation


We will see more of this powerful extension soon, but let's quickly add another modal to add our own data.
### Add Stores with Coordinates to Supabase[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#add-stores-with-coordinates-to-supabase)
To add data to Supabase we create a new function in our **src/app/services/stores.service.ts** :
`
1
 async addStore(info: StoreEntry) {
2
  // Add a new database entry using the POINT() syntax for the coordinates
3
  const { data } = await this.supabase
4
   .from('stores')
5
   .insert({
6
    name: info.name,
7
    description: info.description,
8
    location: `POINT(${info.long} ${info.lat})`,
9
   })
10
   .select()
11
   .single();
1213
  if (data && info.image) {
14
   // Upload the image to Supabase
15
   const foo = await this.supabase.storage
16
    .from('stores')
17
    .upload(`/images/${data.id}.png`, info.image);
18
  }
19
 }
`
Notice how we convert the lat/long information of an entry to a string.
This is how PostGIS expects those values!
We use our Supabase storage bucket to upload an image file if it's included in the new `StoreEntry`. It's almost too easy and feels like cheating to upload a file to cloud storage in just three lines...
Now we need a simple modal, so just like before we add a new function to the **src/app/home/home.page.ts** :
`
1
 async addStore() {
2
  const modal = await this.modalCtrl.create({
3
   component: StorePage,
4
  });
5
  modal.present();
6
 }
`
That function get's called from another button in our **src/app/home/home.page.html** :
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-buttons slot="start">
4
   <ion-button (click)="showNearby()">
5
    <ion-icon name="location" slot="start"></ion-icon> Nearby</ion-button
6
   >
7
  </ion-buttons>
89
  <ion-title> Supa Stores </ion-title>
10
  <ion-buttons slot="end">
11
   <ion-button (click)="addStore()">
12
    <ion-icon name="add" slot="start"></ion-icon> Store</ion-button
13
   >
14
  </ion-buttons>
15
 </ion-toolbar>
16
</ion-header>
`
Back in this new modal, we will define an empty `StoreEntry` object and then connect it to the input fields in our view.
Because we defined the rest of the functionality in our service, we can simply update the **src/app/store/store.page.ts** to:
`
1
import { Component, OnInit } from '@angular/core'
2
import { ModalController } from '@ionic/angular'
3
import { StoreEntry, StoresService } from '../services/stores.service'
45
@Component({
6
 selector: 'app-store',
7
 templateUrl: './store.page.html',
8
 styleUrls: ['./store.page.scss'],
9
})
10
export class StorePage implements OnInit {
11
 store: StoreEntry = {
12
  name: '',
13
  description: '',
14
  image: undefined,
15
  lat: undefined,
16
  long: undefined,
17
 }
1819
 constructor(
20
  public modalCtrl: ModalController,
21
  private storesService: StoresService
22
 ) {}
2324
 ngOnInit() {}
2526
 imageSelected(ev: any) {
27
  this.store.image = ev.detail.event.target.files[0]
28
 }
2930
 async addStore() {
31
  this.storesService.addStore(this.store)
32
  this.modalCtrl.dismiss()
33
 }
34
}
`
The view is not really special and simply holds a bunch of input fields that are connected to the new `store` entry, so bring up the **src/app/store/store.page.html** and change it to:
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-buttons slot="start">
4
   <ion-button (click)="modalCtrl.dismiss()">
5
    <ion-icon slot="icon-only" name="close"></ion-icon>
6
   </ion-button>
7
  </ion-buttons>
8
  <ion-title>Add Store</ion-title>
9
 </ion-toolbar>
10
</ion-header>
1112
<ion-content class="ion-padding">
13
 <ion-input
14
  label="Store name"
15
  label-placement="stacked"
16
  placeholder="Joeys"
17
  [(ngModel)]="store.name"
18
 />
19
 <ion-textarea
20
  rows="3"
21
  label="Store description"
22
  label-placement="stacked"
23
  placeholder="Some about text"
24
  [(ngModel)]="store.description"
25
 />
26
 <ion-input type="number" label="Latitude" label-placement="stacked" [(ngModel)]="store.lat" />
27
 <ion-input type="number" label="Longitude" label-placement="stacked" [(ngModel)]="store.long" />
28
 <ion-input
29
  label="Select store image"
30
  (ionChange)="imageSelected($event)"
31
  type="file"
32
  accept="image/*"
33
 ></ion-input>
3435
 <ion-button
36
  expand="full"
37
  (click)="addStore()"
38
  [disabled]="!store.lat || !store.long || store.name === ''"
39
  >Add Store</ion-button
40
 >
41
</ion-content>
`
As a result, you should have a clean input modal:
![Ionic add store](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-28-geoqueries-postgis%2Fionic-inputs.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Give your storage inserter a try and add some places around you - they should be available in your nearby list immediately!
## Working with Google Maps and Marker[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#working-with-google-maps-and-marker)
### Adding a Map[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#adding-a-map)
Now we have some challenges ahead: adding a map, loading data, and creating markers.
But if you've come this far, I'm sure you can do it!
Get started by adding the `CUSTOM_ELEMENTS_SCHEMA` to the **src/app/home/home.module.ts** which is required to use Capacitor native maps:
`
1
import { NgModule } from '@angular/core'
2
import { CommonModule } from '@angular/common'
3
import { IonicModule } from '@ionic/angular'
4
import { FormsModule } from '@angular/forms'
5
import { HomePage } from './home.page'
67
import { HomePageRoutingModule } from './home-routing.module'
8
import { CUSTOM_ELEMENTS_SCHEMA } from '@angular/core'
910
@NgModule({
11
 imports: [CommonModule, FormsModule, IonicModule, HomePageRoutingModule],
12
 declarations: [HomePage],
13
 schemas: [CUSTOM_ELEMENTS_SCHEMA],
14
})
15
export class HomePageModule {}
`
In our **src/app/home/home.page.ts** we can now create the map by passing in a reference to a DOM element and some initial settings for the map and of course your key.
Update the page with our first step that adds some new variables:
`
1
import { Component, ElementRef, ViewChild } from '@angular/core'
2
import { GoogleMap } from '@capacitor/google-maps'
3
import { LatLngBounds } from '@capacitor/google-maps/dist/typings/definitions'
4
import { ModalController } from '@ionic/angular'
5
import { BehaviorSubject } from 'rxjs'
6
import { environment } from 'src/environments/environment'
7
import { NearbyPage } from '../nearby/nearby.page'
8
import { StoreResult, StoresService } from '../services/stores.service'
9
import { StorePage } from '../store/store.page'
1011
export interface StoreMarker {
12
 markerId: string
13
 storeId: number
14
}
1516
@Component({
17
 selector: 'app-home',
18
 templateUrl: 'home.page.html',
19
 styleUrls: ['home.page.scss'],
20
})
21
export class HomePage {
22
 @ViewChild('map') mapRef!: ElementRef<HTMLElement>
23
 map!: GoogleMap
24
 mapBounds = new BehaviorSubject<LatLngBounds | null>(null)
25
 activeMarkers: StoreMarker[] = []
26
 selectedMarker: StoreMarker | null = null
27
 selectedStore: StoreResult | null = null
2829
 constructor(
30
  private storesService: StoresService,
31
  private modalCtrl: ModalController
32
 ) {}
3334
 ionViewDidEnter() {
35
  this.createMap()
36
 }
3738
 async createMap() {
39
  this.map = await GoogleMap.create({
40
   forceCreate: true, // Prevent issues with live reload
41
   id: 'my-map',
42
   element: this.mapRef.nativeElement,
43
   apiKey: environment.mapsKey,
44
   config: {
45
    center: {
46
     lat: 51.8,
47
     lng: 7.6,
48
    },
49
    zoom: 7,
50
   },
51
  })
52
  this.map.enableCurrentLocation(true)
53
 }
5455
 async showNearby() {
56
  const modal = await this.modalCtrl.create({
57
   component: NearbyPage,
58
  })
59
  modal.present()
60
 }
6162
 async addStore() {
63
  const modal = await this.modalCtrl.create({
64
   component: StorePage,
65
  })
66
  modal.present()
67
 }
68
}
`
The map needs a place to render, so we can now add it to our **src/app/home/home.page.html** and wrap it in a div to add some additional styling later:
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-buttons slot="start">
4
   <ion-button (click)="showNearby()">
5
    <ion-icon name="location" slot="start"></ion-icon> Nearby</ion-button
6
   >
7
  </ion-buttons>
89
  <ion-title> Supa Stores </ion-title>
10
  <ion-buttons slot="end">
11
   <ion-button (click)="addStore()">
12
    <ion-icon name="add" slot="start"></ion-icon> Store</ion-button
13
   >
14
  </ion-buttons>
15
 </ion-toolbar>
16
</ion-header>
1718
<ion-content>
19
 <div class="container">
20
  <capacitor-google-map #map></capacitor-google-map>
21
 </div>
22
</ion-content>
`
Because the Capacitor map essentially renders **behind your webview** inside a native app, we need to make the background of our current page invisible.
For this, simply add the following to the **src/app/home/home.page.scss** :
`
1
ion-content {
2
 --background: none;
3
}
45
.container {
6
 width: 100%;
7
 height: 100%;
8
}
910
capacitor-google-map {
11
 display: inline-block;
12
 width: 100%;
13
 height: 100%;
14
}
`
Now the map should fill the whole screen.
![Capacitor antive map](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-28-geoqueries-postgis%2Fcapacitor-map.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
This brings us to the last missing piece…
### Loading Places in a Box of Coordinates[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#loading-places-in-a-box-of-coordinates)
Getting all stores is usually too much - you want to show what's nearby to a user, and you can do this by sending basically a box of coordinates to our previously stored database function.
For this, we first add another call in our **src/app/services/stores.service.ts** :
`
1
 // Get all places in a box of coordinates
2
 async getStoresInView(
3
  min_lat: number,
4
  min_long: number,
5
  max_lat: number,
6
  max_long: number
7
 ) {
8
  const { data } = await this.supabase.rpc('stores_in_view', {
9
   min_lat,
10
   min_long,
11
   max_lat,
12
   max_long,
13
  });
14
  return data;
15
 }
`
Nothing fancy, just passing those values to the database function.
The challenging part is now **listening to map boundary updates** , which happen whenever you slightly touch the list.
Because we don't want to call our function 100 times in one second, we use a bit of RxJS to delay the update of our coordinates so the `updateStoresInView` function is called after the user finished swiping the list.
At that point, we grab the map bounds and call our function, so go ahead and update the **src/app/home/home.page.ts** with the following:
`
1
 async createMap() {
2
  this.map = await GoogleMap.create({
3
   forceCreate: true, // Prevent issues with live reload
4
   id: 'my-map',
5
   element: this.mapRef.nativeElement,
6
   apiKey: environment.mapsKey,
7
   config: {
8
    center: {
9
     lat: 51.8,
10
     lng: 7.6,
11
    },
12
    zoom: 7,
13
   },
14
  });
15
  this.map.enableCurrentLocation(true);
1617
  // Listen to biew changes and emit to our Behavior Subject
18
  this.map.setOnBoundsChangedListener((ev) => {
19
   this.mapBounds.next(ev.bounds);
20
  });
2122
  // React to changes of our subject with a 300ms delay so we don't trigger a reload all the time
23
  this.mapBounds.pipe(debounce((i) => interval(300))).subscribe((res) => {
24
   this.updateStoresInView();
25
  });
2627
  // Get the current user coordinates
28
  this.loadUserLocation();
29
 }
3031
 async updateStoresInView() {
32
  const bounds = await this.map.getMapBounds();
3334
  // Get stores in our bounds using PostGIS
35
  const stores = await this.storesService.getStoresInView(
36
   bounds.southwest.lat,
37
   bounds.southwest.lng,
38
   bounds.northeast.lat,
39
   bounds.northeast.lng
40
  );
4142
  // Update markers for elements
43
  this.addMarkers(stores);
44
 }
4546
 async loadUserLocation() {
47
  // TODO
48
 }
4950
 async addMarkers(stores: StoreResult[]) {
51
  // TODO
52
 }
`
We can also fill one of our functions with some code as we already used the `Geolocation` plugin to load users' coordinates before, so update the function to:
`
1
 async loadUserLocation() {
2
  // Get location with Capacitor Geolocation plugin
3
  const coordinates = await Geolocation.getCurrentPosition();
45
  if (coordinates) {
6
   // Focus the map on user and zoom in
7
   this.map.setCamera({
8
    coordinate: {
9
     lat: coordinates.coords.latitude,
10
     lng: coordinates.coords.longitude,
11
    },
12
    zoom: 14,
13
   });
14
  }
15
 }
`
Now we are loading the user location and zooming in to the current place, which will then cause our `updateStoresInView` function to be triggered and we receive a list of places that we just need to render!
### Displaying Marker on our Google Map[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#displaying-marker-on-our-google-map)
You can already play around with the app and log the stores after moving the map - it really feels magical how PostGIS returns only the elements that are within the box of coordinates.
To actually display them we can add the following function to our **src/app/home/home.page.ts** now:
`
1
 async addMarkers(stores: StoreResult[]) {
2
  // Skip if there are no results
3
  if (stores.length === 0) {
4
   return;
5
  }
67
  // Find marker that are outside of the view
8
  const toRemove = this.activeMarkers.filter((marker) => {
9
   const exists = stores.find((item) => item.id === marker.storeId);
10
   return !exists;
11
  });
1213
  // Remove markers
14
  if (toRemove.length) {
15
   await this.map.removeMarkers(toRemove.map((marker) => marker.markerId));
16
  }
1718
  // Create new marker array
19
  const markers: Marker[] = stores.map((store) => {
20
   return {
21
    coordinate: {
22
     lat: store.lat,
23
     lng: store.long,
24
    },
25
    title: store.name,
26
   };
27
  });
2829
  // Add markers, store IDs
30
  const newMarkerIds = await this.map.addMarkers(markers);
3132
  // Crate active markers by combining information
33
  this.activeMarkers = stores.map((store, index) => {
34
   return {
35
    markerId: newMarkerIds[index],
36
    storeId: store.id,
37
   };
38
  });
3940
  this.addMarkerClicks();
41
 }
4243
 addMarkerClicks() {
44
  // TODO
45
 }
`
This function got a bit longer because we need to **manage our marker information**. If we just remove and repaint all markers, it looks and feels horrible so we always keep track of existing markers and only render new markers.
Additionally, these `Marker` have limited information, and if we click a marker we want to present a modal with information about the store from Supabase.
That means we also need the real ID of that object, and so we create an array `activeMarkers` that basically connects the information of a store ID with the marker ID!
At this point, you should be able to see markers on your map. If you can't see them, zoom out and you might find them.
![Ionic map with marker](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-28-geoqueries-postgis%2Fionic-map-marker.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
To wrap this up, let's take a look at one more cool Supabase feature.
### Presenting Marker with Image Transform[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#presenting-marker-with-image-transform)
We have the marker and store ID, so we can simply load the information from our Supabase database.
Now a store might have an image, and while we download the image from our storage bucket we can use [image transformations](https://supabase.com/docs/guides/storage/serving/image-transformations) to get an image exactly in the right dimensions to save time and bandwidth!
For this, add two new functions to our **src/app/services/stores.service.ts** :
`
1
 // Load data from Supabase database
2
 async loadStoreInformation(id: number) {
3
  const { data } = await this.supabase
4
   .from('stores')
5
   .select('*')
6
   .match({ id })
7
   .single();
8
  return data;
9
 }
1011
 async getStoreImage(id: number) {
12
  // Get image for a store and transform it automatically!
13
  return this.supabase.storage
14
   .from('stores')
15
   .getPublicUrl(`images/${id}.png`, {
16
    transform: {
17
     width: 300,
18
     resize: 'contain',
19
    },
20
   }).data.publicUrl;
21
 }
`
To use image transformations we only need to add an object to the `getPublicUrl()` function and define the different properties we want to have.
Again, it's _that_ easy.
Now we just need to load this information when we click on a marker, so add the following function to our **src/app/home/home.page.ts** which handles the click on a map marker:
`
1
 addMarkerClicks() {
2
  // Handle marker clicks
3
  this.map.setOnMarkerClickListener(async (marker) => {
4
   // Find our local object based on the marker ID
5
   const info = this.activeMarkers.filter(
6
    (item) => item.markerId === marker.markerId.toString()
7
   );
8
   if (info.length) {
9
    this.selectedMarker = info[0];
1011
    // Load the store information from Supabase Database
12
    this.selectedStore = await this.storesService.loadStoreInformation(
13
     info[0].storeId
14
    );
1516
    // Get the iamge from Supabase Storage
17
    const img = await this.storesService.getStoreImage(
18
     this.selectedStore!.id
19
    );
20
    if (img) {
21
     this.selectedStore!.image = img;
22
    }
23
   }
24
  });
25
 }
`
We simply load the information and image and set this to our `selectedStore` variable.
This will now be used to trigger an **inline modal** , so we don't need to come up with another component and can simply define our Ionic modal right inside the **src/app/home/home.page.html** like this:
`
1
<ion-header>
2
 <ion-toolbar color="primary">
3
  <ion-buttons slot="start">
4
   <ion-button (click)="showNearby()">
5
    <ion-icon name="location" slot="start"></ion-icon> Nearby</ion-button
6
   >
7
  </ion-buttons>
89
  <ion-title> Supa Stores </ion-title>
10
  <ion-buttons slot="end">
11
   <ion-button (click)="addStore()">
12
    <ion-icon name="add" slot="start"></ion-icon> Store</ion-button
13
   >
14
  </ion-buttons>
15
 </ion-toolbar>
16
</ion-header>
1718
<ion-content>
19
 <div class="container">
20
  <capacitor-google-map #map></capacitor-google-map>
21
 </div>
2223
 <ion-modal
24
  [isOpen]="selectedMarker !== null"
25
  [breakpoints]="[0, 0.4, 1]"
26
  [initialBreakpoint]="0.4"
27
  (didDismiss)="selectedMarker = null;"
28
 >
29
  <ng-template>
30
   <ion-content class="ion-padding">
31
    <ion-label class="ion-texst-wrap">
32
     <h1>{{selectedStore?.name}}</h1>
33
     <ion-note>{{selectedStore?.description}}</ion-note>
34
    </ion-label>
35
    <div class="ion-text-center ion-margin-top">
36
     <img [src]="selectedStore?.image" *ngIf="selectedStore?.image" />
37
    </div>
38
   </ion-content>
39
  </ng-template>
40
 </ion-modal>
41
</ion-content>
`
Because we also used `breakpoints` and the `initialBreakpoint` properties of the modal we get this nice bottom sheet modal UI whenever we click on a marker:
![Ionic marker modal with image](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-02-28-geoqueries-postgis%2Fionic-marker-with-image.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
And with that, we have finished our Ionic app with Supabase geo-queries using PostGIS!
## Conclusion[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#conclusion)
I was fascinated by the power of this simple PostGIS extension that we enabled with just one command (or click).
Building apps based on geolocation data is a very common scenario, and with PostGIS we can build these applications easily on the back of a [Supabase](https://supabase.com/) database (and [auth](https://supabase.com/blog/authentication-in-ionic-angular) ), and storage, and so much more..)
You can [find the full code of this tutorial on Github](https://github.com/saimon24/supabase-postgis-ionic-angular) where you just need to insert your own Supabase instance. your Google Maps key and then create the tables with the included SQL file.
If you enjoyed the tutorial, you can [find many more tutorials and courses on Galaxies.dev](https://galaxies.dev) where I help modern web and mobile developers build epic apps 🚀
Until next time and happy coding with Supabase!
## Related resources[#](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#related-resources)
  * [Authentication in Ionic Angular with Supabase](https://supabase.com/blog/authentication-in-ionic-angular)
  * [Building a Realtime Trello Board with Supabase and Angular](https://supabase.com/blog/building-a-realtime-trello-board-with-supabase-and-angular)
  * [Build a User Management App with Ionic Angular](https://supabase.com/docs/guides/getting-started/tutorials/with-ionic-angular)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgeo-queries-with-postgis-in-ionic-angular&text=Geo%20Queries%20with%20PostGIS%20in%20Ionic%20Angular)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgeo-queries-with-postgis-in-ionic-angular&text=Geo%20Queries%20with%20PostGIS%20in%20Ionic%20Angular)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fgeo-queries-with-postgis-in-ionic-angular&t=Geo%20Queries%20with%20PostGIS%20in%20Ionic%20Angular)
[Last postSupabase Beta February 20239 March 2023](https://supabase.com/blog/supabase-beta-update-february-2023)
[Next postType Constraints in 65 lines of SQL17 February 2023](https://supabase.com/blog/type-constraints-in-65-lines-of-sql)
[ionic](https://supabase.com/blog/tags/ionic)[postgis](https://supabase.com/blog/tags/postgis)[geoqueries](https://supabase.com/blog/tags/geoqueries)[storage](https://supabase.com/blog/tags/storage)
On this page
  * [Creating the Supabase Project](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#creating-the-supabase-project)
  * [Why PostGIS Extension?](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#why-postgis-extension)
  * [Defining your Tables with SQL](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#defining-your-tables-with-sql)
    * [Adding the PostGIS Extensions](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#adding-the-postgis-extensions)
    * [Creating the SQL Tables](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#creating-the-sql-tables)
  * [Working with Geo Queries in Ionic Angular](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#working-with-geo-queries-in-ionic-angular)
    * [Setting up the Project](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#setting-up-the-project)
    * [Native Project Configuration](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#native-project-configuration)
    * [Finding Nearby Places with Database Functions](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#finding-nearby-places-with-database-functions)
    * [Add Stores with Coordinates to Supabase](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#add-stores-with-coordinates-to-supabase)
  * [Working with Google Maps and Marker](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#working-with-google-maps-and-marker)
    * [Adding a Map](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#adding-a-map)
    * [Loading Places in a Box of Coordinates](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#loading-places-in-a-box-of-coordinates)
    * [Displaying Marker on our Google Map](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#displaying-marker-on-our-google-map)
    * [Presenting Marker with Image Transform](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#presenting-marker-with-image-transform)
  * [Conclusion](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#conclusion)
  * [Related resources](https://supabase.com/blog/geo-queries-with-postgis-in-ionic-angular#related-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgeo-queries-with-postgis-in-ionic-angular&text=Geo%20Queries%20with%20PostGIS%20in%20Ionic%20Angular)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fgeo-queries-with-postgis-in-ionic-angular&text=Geo%20Queries%20with%20PostGIS%20in%20Ionic%20Angular)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fgeo-queries-with-postgis-in-ionic-angular&t=Geo%20Queries%20with%20PostGIS%20in%20Ionic%20Angular)
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

