---
url: https://supabase.com/partners/integrations/keyri
scraped_at: 2025-05-25T09:12:58.252625
title: Keyri | Works With Supabase
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
[Back](https://supabase.com/partners/integrations)
![Keyri](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fkeyri%2Fkeyri_logo.jpeg&w=128&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
# Keyri
![Keyri](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fkeyri%2Fkeyri_og1.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Keyri](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fkeyri%2Fkeyri_og2.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
![Keyri](https://supabase.com/_next/image?url=https%3A%2F%2Fobuldanrptloktxcffvn.supabase.co%2Fstorage%2Fv1%2Fobject%2Fpublic%2Fimages%2Fintegrations%2Fkeyri%2Fkeyri_og3.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Overview
Keyri is an authentication company, providing customers with a simple and secure form of passwordless MFA. Our platform transforms every login into a one-step biometrics-based process that provides a seamless user experience while strengthening account security. Users simply scan a QR code on your login page with their smartphone and pass biometrics in your mobile app to log into your web app.
Incorporating Keyri QR login into your Supabase-based authentication system is a matter of sending the user's `refreshToken` from your mobile app to your web app via the Keyri mobile SDK and web Widget. On the mobile side, just load the `refreshToken` string as the payload into the Keyri method you're using in your app. On the web side, extract the refreshToken string from the payload that the Widget outputs and load it into the setSession method provided by the Supabase JS SDK.
## Documentation
Keyri can be used to incorporate sign-in-with-QR functionality into your Supabase app, allowing users to scan a QR code on your web app with your mobile app and be instantly logged into the web app without having to input any credentials.
Configuration is split into Web and Mobile components. On web, the Keyri QR Widget needs to be installed along with an event listener, and in your mobile app, install the Keyri SDK and pass into it the user's refresh token when sign-in-with-QR is initiated. When the refresh token lands in your web app, it's passed into Supabase's `setSession()` method.
# Sign up for Keyri
First make a free account on the Keyri dashboard (<https://app.keyri.com>). On Add Your Application, set a name and input the domain on which your app will eventually be deployed. You can create multiple application in Keyri to account for your development, staging, and production environments
![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/keyri/documentation/HvTIja3KfgKUIMiNVKAqP_screen-shot-2022-10-13-at-21524-pm.png)
Note your application key from the Keys and Credentials section - this will be used in the Mobile portion of the implementation
![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/keyri/documentation/KnD6LkWs-PUDtTS1sT9Rz_screen-shot-2022-10-13-at-21746-pm.png)
# Web
For your web app, first download KeyriQR.html (available [here](https://raw.githubusercontent.com/Keyri-Co/library-keyri-connect/main/KeyriQR.html)) and save it to a public directory.
Next, embed KeyriQR.html in your login page as an iFrame within the desired div. This serves as the widget that displays the dynamic QR code and connects with the Keyri API.
`
1
<div>
2
  <iframe
3
    title='KeyriQR'
4
    src='/KeyriQR.html'
5
    id='qr-frame'
6
    height='300'
7
    width='300'
8
    scrolling='no'
9
    style={{ border: 'solid 5px white' }}
10
   ></iframe>
11
</div>
`
Next, for the same login view, set up an event listener to pick up the session token that the iFrame emits when the QR code is scanned by your app.
`
1
useEffect(() => {
2
  window.addEventListener('message', async (evt) => {
3
   if (evt.data.keyri && evt.data.data && document.location.origin == evt.origin) {
4
    const { data } = evt;
5
    if (!data.error) {
6
     let refresh_token = JSON.parse(data.data).refreshToken;
7
     await handleQrLogin(refresh_token);
8
    } else if (data.error) {
9
     console.log(`Keyri error: ${data.message}`);
10
    }
11
   }
12
});
`
That's it!
# Mobile
### Install Flutter
First, install the Flutter SDK, found at flutter.dev
Make sure to add Flutter to your PATH, for example: 
`
1
export PATH="$PATH:`pwd`/flutter/bin"
`
### Apple - initial setup
Download the latest version of Xcode from the Mac App Store. Make sure the Xcode provided simulator is using a 64-bit device (iPhone 5s or later). You can check the device by viewing the settings in the simulator’s **Hardware > Device** or **File > Open Simulator** menus.
### Android - initial setup
Download the latest version of [Android Studio](https://developer.android.com/studio). Install Android SDK and needed emulator(s).
### Create Project
Run this command in your terminal/shell at the desired location for your new project
`
1
$ flutter create my_app
`
You can then CD into the new directory, and run the test app with 
`
1
flutter run
`
This is a good test - if things are configured correctly so far you should see the default Flutter test app deployed.
### Add dependencies (Keyri and Supabase)
Open your Pubspec.yaml file, which should be at the top level directory in your new project
Add Keyri and Supabase under **dependencies**
![](https://obuldanrptloktxcffvn.supabase.co/storage/v1/object/public/images/integrations/keyri/documentation/jlAfOTEchuZpBq8TeXhJZ_screen-shot-2022-09-29-at-060908.png)
One can now access Supabase and Keyri sdks in their Flutter code
### Utilize the two together
  1. Make a request to Supabase to authenticate the user
  2. Parse the response to extract the token
  3. Authenticate using Keyri 
    1. Below, we show how to utilize the EasyKeyriAuth function, which takes the user through scanning the code, creating the session, displaying the confirmation screen, and finalizing the payload transmission 
       * Note - you can find your App Key in the Keyri Developer Portal​
    2. Alternatively, intermediate functions in the Keyri SDK, discussed in the mobile docs, can provide control over displaying a custom QR Scanner and/or Confirmation screen


`
1
// Sign in user with email and password
2
// Alternatively one can utilize the Supabase API to accomplish the same thing
3
final response = await client.auth.signIn(email: 'email', password: 'password');
4
if (response.error != null) {
5
 // Error
6
  print('Error: ${response.error?.message}');
7
} else {
8
  // Success
9
  final session = response.data;
10
  // This is the payload that needs to be send through Keyri
11
  final refreshToken = session.refreshToken
12
  // EasyKeyriAuth guides the user through scanning and parsing the QR, confirming the session, and configuring the payload
13
  // One can also use the initiateQRSession method to use the Keyri Scanner with a custom Confirmation screen
14
  // Or the ProcessLink method if you have your own scanner or are using deep linking
15
  await keyri
16
    .easyKeyriAuth([App Key],
17
      '{"refreshToken":"$refreshToken"}', [email])
18
    .then((authResult) => _onAuthResult(authResult))
19
    .catchError((error, stackTrace) => _onError(error));
20
}
`
## Details
DeveloperKeyri
Category[Auth](https://supabase.com/partners/integrations#auth)
Website[keyri.com](https://keyri.com/?utm_source=supabase-partner-gallery)
Documentation[Learn](https://docs.keyri.com/supabase?utm_source=supabase-partner-gallery)
Third-party integrations and docs are managed by Supabase partners.
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

