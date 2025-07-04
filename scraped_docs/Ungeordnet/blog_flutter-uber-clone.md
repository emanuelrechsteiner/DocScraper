---
url: https://supabase.com/blog/flutter-uber-clone
scraped_at: 2025-05-25T09:08:15.402545
title: Building an Uber Clone with Flutter and Supabase
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
# Building an Uber Clone with Flutter and Supabase
05 Sep 2024
•
38 minute read
[![Tyler Shukert avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fdshukertjr.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Tyler ShukertDevRel](https://twitter.com/dshukertjr)
![Building an Uber Clone with Flutter and Supabase](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Fflutter-uber-clone%2Fflutter-uber-clone-thumb.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
[Do you prefer audio-visual learning? Watch the video guide!](https://youtu.be/cL4pVpaOH9o)
[Or jump straight into the code](https://github.com/dshukertjr/uber-clone)
Postgres can handle geography data efficiently thanks to the PostGIS extension. Combining it with Supabase realtime and you can create a real-time location tracking app.
In this tutorial, we will guide you through the process of creating an Uber-like application using Flutter and Supabase. This project demonstrates the capabilities of Supabase for building complex, real-time applications with minimal backend code.
## App Overview[#](https://supabase.com/blog/flutter-uber-clone#app-overview)
An actual Uber app has two apps, the consumer facing app and the driver facing app. This article only covers the consumer facing app. The app works by first choosing a destination, and then waiting for the driver to come pick them up. Once they are picked up, they head to the destination and the journey is complete once they arrive at the destination. Throughout the lifecycle of the app, the driver’s position is shared on screen in real-time.
The focus of the app is to showcase how to use Supabase realtime with geographical data, so handling payments will not be covered in this article.
## Prerequisites[#](https://supabase.com/blog/flutter-uber-clone#prerequisites)
Before beginning, ensure you have:
  1. Flutter installed
  2. A Supabase account - head to [database.new](http://database.new) if you don’t have one yet.
  3. Basic knowledge of Dart and Flutter


## Step 1: Project Setup[#](https://supabase.com/blog/flutter-uber-clone#step-1-project-setup)
Start by creating a blank Flutter project.
`
1
flutter create canvas --empty --platforms=ios,android
`
Then, add the required dependencies to your `pubspec.yaml` file:
`
1
supabase_flutter: ^2.5.9
2
google_maps_flutter: ^2.7.0
3
geolocator: ^12.0.0
4
duration: ^3.0.13
5
intl: ^0.19.0
`
`google_maps_flutter` is used to display the map on our app. We will also draw and move icons on the map. `geolocator` is used to access the GPS information. `duration` is used to parse duration value returned from Google’s routes API, and `intl` is used to display currencies nicely.
In addition to adding it to `pubspec.yaml` file, `google_maps_flutter` requires additional setup to get started. Follow the [readme.md](https://pub.dev/packages/google_maps_flutter) file to configure Google Maps for the platform you want to support.
Run `flutter pub get` to install these dependencies.
## Step 2: Supabase Initialization[#](https://supabase.com/blog/flutter-uber-clone#step-2-supabase-initialization)
In your `main.dart` file, initialize Supabase with the following code:
`
1
import 'package:supabase_flutter/supabase_flutter.dart';
23
void main() async {
4
 await Supabase.initialize(
5
  url: 'YOUR_SUPABASE_URL',
6
  anonKey: 'YOUR_SUPABASE_ANON_KEY',
7
 );
8
 runApp(const MainApp());
9
}
1011
final supabase = Supabase.instance.client;
`
Replace `YOUR_SUPABASE_URL` and `YOUR_SUPABASE_ANON_KEY` with your actual Supabase project credentials.
## Step 3: Database Configuration[#](https://supabase.com/blog/flutter-uber-clone#step-3-database-configuration)
We need to create two tables for this application. The `drivers` table holds the vehicle information as well as the position. Notice that we have a `latitude` and `longitude` generated column. These columns are generated from the `location` column, and will be used to display the real-time location on the map later on.
The `rides` table holds information about customer’s request to get a ride.
`
1
-- Enable the "postgis" extension
2
create extension postgis with schema extensions;
34
create table if not exists public.drivers (
5
	id uuid primary key default gen_random_uuid(),
6
	model text not null,
7
 number text not null,
8
 is_available boolean not null default false,
9
	location geography(POINT) not null,
10
 latitude double precision generated always as (st_y(location::geometry)) stored,
11
 longitude double precision generated always as (st_x(location::geometry)) stored
12
);
1314
create type ride_status as enum ('picking_up', 'riding', 'completed');
1516
create table if not exists public.rides (
17
 id uuid primary key default gen_random_uuid(),
18
 driver_id uuid not null references public.drivers(id),
19
 passenger_id uuid not null references auth.users(id),
20
 origin geography(POINT) not null,
21
 destination geography(POINT) not null,
22
 fare integer not null,
23
 status ride_status not null default 'picking_up'
24
);
`
Let’s also set [row level security](https://supabase.com/docs/guides/database/postgres/row-level-security) policies for the tables to secure our database.
`
1
alter table public.drivers enable row level security;
2
create policy "Any authenticated users can select drivers." on public.drivers for select to authenticated using (true);
3
create policy "Drivers can update their own status." on public.drivers for update to authenticated using (auth.uid() = id);
45
alter table public.rides enable row level security;
6
create policy "The driver or the passenger can select the ride." on public.rides for select to authenticated using (driver_id = auth.uid() or passenger_id = auth.uid());
7
create policy "The driver can update the status. " on public.rides for update to authenticated using (auth.uid() = driver_id);
`
Lastly, we will create a few database functions and triggers. The first function and trigger updates the driver status depending on the status of the ride. This ensures that the driver status is always in sync with the status of the ride.
The second function is for the customer to find available drivers. This function will be called from the Flutter app, which automatically find available drivers within 3,000m radius and returns the driver ID and a newly created ride ID if a driver was found.
`
1
-- Create a trigger to update the driver status
2
create function update_driver_status()
3
  returns trigger
4
  language plpgsql
5
  as $$
6
    begin
7
      if new.status = 'completed' then
8
        update public.drivers
9
        set is_available = true
10
        where id = new.driver_id;
11
      else
12
        update public.drivers
13
        set is_available = false
14
        where id = new.driver_id;
15
      end if;
16
      return new;
17
  end $$;
1819
create trigger driver_status_update_trigger
20
after insert or update on rides
21
for each row
22
execute function update_driver_status();
2324
-- Finds the closest available driver within 3000m radius
25
create function public.find_driver(origin geography(POINT), destination geography(POINT), fare int)
26
  returns table(driver_id uuid, ride_id uuid)
27
  language plpgsql
28
  as $$
29
    declare
30
      v_driver_id uuid;
31
      v_ride_id uuid;
32
    begin
33
      select
34
        drivers.id into v_driver_id
35
      from public.drivers
36
      where is_available = true
37
        and st_dwithin(origin, location, 3000)
38
      order by drivers.location <-> origin
39
      limit 1;
4041
      -- return null if no available driver is found
42
      if v_driver_id is null then
43
        return;
44
      end if;
4546
      insert into public.rides (driver_id, passenger_id, origin, destination, fare)
47
      values (v_driver_id, auth.uid(), origin, destination, fare)
48
      returning id into v_ride_id;
4950
      return query
51
        select v_driver_id as driver_id, v_ride_id as ride_id;
52
  end $$ security definer;
`
## Step 4: Defining the models[#](https://supabase.com/blog/flutter-uber-clone#step-4-defining-the-models)
Start by defining the models for this app. The `AppState` enum holds the 5 different state that this app could take in the order that it proceeds. The `Ride` and `Driver` class are simple data class for the `rides` and `drivers` table we created earlier.
`
1
enum AppState {
2
 choosingLocation,
3
 confirmingFare,
4
 waitingForPickup,
5
 riding,
6
 postRide,
7
}
89
enum RideStatus {
10
 picking_up,
11
 riding,
12
 completed,
13
}
1415
class Ride {
16
 final String id;
17
 final String driverId;
18
 final String passengerId;
19
 final int fare;
20
 final RideStatus status;
2122
 Ride({
23
  required this.id,
24
  required this.driverId,
25
  required this.passengerId,
26
  required this.fare,
27
  required this.status,
28
 });
2930
 factory Ride.fromJson(Map<String, dynamic> json) {
31
  return Ride(
32
   id: json['id'],
33
   driverId: json['driver_id'],
34
   passengerId: json['passenger_id'],
35
   fare: json['fare'],
36
   status: RideStatus.values
37
     .firstWhere((e) => e.toString().split('.').last == json['status']),
38
  );
39
 }
40
}
4142
class Driver {
43
 final String id;
44
 final String model;
45
 final String number;
46
 final bool isAvailable;
47
 final LatLng location;
4849
 Driver({
50
  required this.id,
51
  required this.model,
52
  required this.number,
53
  required this.isAvailable,
54
  required this.location,
55
 });
5657
 factory Driver.fromJson(Map<String, dynamic> json) {
58
  return Driver(
59
   id: json['id'],
60
   model: json['model'],
61
   number: json['number'],
62
   isAvailable: json['is_available'],
63
   location: LatLng(json['latitude'], json['longitude']),
64
  );
65
 }
66
}
`
## Step 5: Main UI Implementation[#](https://supabase.com/blog/flutter-uber-clone#step-5-main-ui-implementation)
Create a `UberCloneMainScreen` widget to serve as the main interface for the application. This widget will manage the five different `AppState` that we created in the previous step.
  1. Location selection - The customer scrolls through the map and chooses the destination
  2. Fare confirmation - The fare is displayed to the user, and the customer can accept the fare to find a nearby driver
  3. Pickup waiting - A driver was found, and the customer is waiting for the driver to arrive
  4. In-ride - The customer has got on the car, and they are headed to the destination
  5. Post-ride - The customer has arrived at the destination, and a thank you modal is displayed


For statuses 3, 4, and 5, the status update happens on the driver’s app, which we don’t have. So you can directly modify the data from the Supabase dashboard and update the status of the ride.
`
1
class UberCloneMainScreen extends StatefulWidget {
2
 const UberCloneMainScreen({super.key});
34
 @override
5
 UberCloneMainScreenState createState() => UberCloneMainScreenState();
6
}
78
class UberCloneMainScreenState extends State<UberCloneMainScreen> {
9
 AppState _appState = AppState.choosingLocation;
10
 GoogleMapController? _mapController;
1112
 /// The default camera position is arbitrarily set to San Francisco.
13
 CameraPosition _initialCameraPosition = const CameraPosition(
14
  target: LatLng(37.7749, -122.4194),
15
  zoom: 14.0,
16
 );
1718
 /// The selected destination by the user.
19
 LatLng? _selectedDestination;
2021
 /// The current location of the user.
22
 LatLng? _currentLocation;
2324
 final Set<Polyline> _polylines = {};
25
 final Set<Marker> _markers = {};
2627
 /// Fare in cents
28
 int? _fare;
29
 StreamSubscription<dynamic>? _driverSubscription;
30
 StreamSubscription<dynamic>? _rideSubscription;
31
 Driver? _driver;
3233
 LatLng? _previousDriverLocation;
34
 BitmapDescriptor? _pinIcon;
35
 BitmapDescriptor? _carIcon;
3637
 @override
38
 void initState() {
39
  super.initState();
40
  _signInIfNotSignedIn();
41
  _checkLocationPermission();
42
  _loadIcons();
43
 }
4445
 @override
46
 void dispose() {
47
  _cancelSubscriptions();
48
  super.dispose();
49
 }
5051
 // TODO: Add missing methods
5253
 @override
54
 Widget build(BuildContext context) {
55
  return Scaffold(
56
   appBar: AppBar(
57
    title: Text(_getAppBarTitle()),
58
   ),
59
   body: Stack(
60
    children: [
61
     _currentLocation == null
62
       ? const Center(child: CircularProgressIndicator())
63
       : GoogleMap(
64
         initialCameraPosition: _initialCameraPosition,
65
         onMapCreated: (GoogleMapController controller) {
66
          _mapController = controller;
67
         },
68
         myLocationEnabled: true,
69
         onCameraMove: _onCameraMove,
70
         polylines: _polylines,
71
         markers: _markers,
72
        ),
73
     if (_appState == AppState.choosingLocation)
74
      Center(
75
       child: Image.asset(
76
        'assets/images/center-pin.png',
77
        width: 96,
78
        height: 96,
79
       ),
80
      ),
81
    ],
82
   ),
83
   floatingActionButton: _appState == AppState.choosingLocation
84
     ? FloatingActionButton.extended(
85
       onPressed: _confirmLocation,
86
       label: const Text('Confirm Destination'),
87
       icon: const Icon(Icons.check),
88
      )
89
     : null,
90
   floatingActionButtonLocation: FloatingActionButtonLocation.centerFloat,
91
   bottomSheet: _appState == AppState.confirmingFare ||
92
       _appState == AppState.waitingForPickup
93
     ? Container(
94
       width: MediaQuery.of(context).size.width,
95
       padding: const EdgeInsets.all(16)
96
         .copyWith(bottom: 16 + MediaQuery.of(context).padding.bottom),
97
       decoration: BoxDecoration(
98
        color: Colors.white,
99
        boxShadow: [
100
         BoxShadow(
101
          color: Colors.grey.withOpacity(0.5),
102
          spreadRadius: 5,
103
          blurRadius: 7,
104
          offset: const Offset(0, 3),
105
         ),
106
        ],
107
       ),
108
       child: Column(
109
        mainAxisSize: MainAxisSize.min,
110
        children: [
111
         if (_appState == AppState.confirmingFare) ...[
112
          Text('Confirm Fare',
113
            style: Theme.of(context).textTheme.titleLarge),
114
          const SizedBox(height: 16),
115
          Text(
116
            'Estimated fare: ${NumberFormat.currency(
117
             symbol:
118
               '\$', // You can change this to your preferred currency symbol
119
             decimalDigits: 2,
120
            ).format(_fare! / 100)}',
121
            style: Theme.of(context).textTheme.titleMedium),
122
          const SizedBox(height: 16),
123
          ElevatedButton(
124
           onPressed: _findDriver,
125
           style: ElevatedButton.styleFrom(
126
            minimumSize: const Size(double.infinity, 50),
127
           ),
128
           child: const Text('Confirm Fare'),
129
          ),
130
         ],
131
         if (_appState == AppState.waitingForPickup &&
132
           _driver != null) ...[
133
          Text('Your Driver',
134
            style: Theme.of(context).textTheme.titleLarge),
135
          const SizedBox(height: 8),
136
          Text('Car: ${_driver!.model}',
137
            style: Theme.of(context).textTheme.titleMedium),
138
          const SizedBox(height: 8),
139
          Text('Plate Number: ${_driver!.number}',
140
            style: Theme.of(context).textTheme.titleMedium),
141
          const SizedBox(height: 16),
142
          Text(
143
            'Your driver is on the way. Please wait at the pickup location.',
144
            style: Theme.of(context).textTheme.bodyMedium),
145
         ]
146
        ],
147
       ),
148
      )
149
     : const SizedBox.shrink(),
150
  );
151
 }
152
}
`
The code above still has many missing methods, so do not worry if you see many errors.
## Step 6: Location Selection Implementation[#](https://supabase.com/blog/flutter-uber-clone#step-6-location-selection-implementation)
The way the customer chooses the destination is by scrolling through the map and tapping on the confirmation FAB. Once the FAB is pressed, the `_confirmLocation` method is called, which calls a Supabase Edge Function called `route`. This `route` function returns a list of coordinates to create a polyline to get from the current location to the destination. We then draw the polyline on the Google Maps to provide to simulate an Uber-like user experience.
`
1
Future<void> _confirmLocation() async {
2
  if (_selectedDestination != null && _currentLocation != null) {
3
   try {
4
    final response = await supabase.functions.invoke(
5
     'route',
6
     body: {
7
      'origin': {
8
       'latitude': _currentLocation!.latitude,
9
       'longitude': _currentLocation!.longitude,
10
      },
11
      'destination': {
12
       'latitude': _selectedDestination!.latitude,
13
       'longitude': _selectedDestination!.longitude,
14
      },
15
     },
16
    );
1718
    final data = response.data as Map<String, dynamic>;
19
    final coordinates = data['legs'][0]['polyline']['geoJsonLinestring']
20
      ['coordinates'] as List<dynamic>;
21
    final duration = parseDuration(data['duration'] as String);
22
    _fare = ((duration.inMinutes * 40)).ceil();
2324
    final List<LatLng> polylineCoordinates = coordinates.map((coord) {
25
     return LatLng(coord[1], coord[0]);
26
    }).toList();
2728
    setState(() {
29
     _polylines.add(Polyline(
30
      polylineId: const PolylineId('route'),
31
      points: polylineCoordinates,
32
      color: Colors.black,
33
      width: 5,
34
     ));
3536
     _markers.add(Marker(
37
      markerId: const MarkerId('destination'),
38
      position: _selectedDestination!,
39
      icon: _pinIcon ??
40
        BitmapDescriptor.defaultMarkerWithHue(BitmapDescriptor.hueRed),
41
     ));
42
    });
4344
    LatLngBounds bounds = LatLngBounds(
45
     southwest: LatLng(
46
      polylineCoordinates
47
        .map((e) => e.latitude)
48
        .reduce((a, b) => a < b ? a : b),
49
      polylineCoordinates
50
        .map((e) => e.longitude)
51
        .reduce((a, b) => a < b ? a : b),
52
     ),
53
     northeast: LatLng(
54
      polylineCoordinates
55
        .map((e) => e.latitude)
56
        .reduce((a, b) => a > b ? a : b),
57
      polylineCoordinates
58
        .map((e) => e.longitude)
59
        .reduce((a, b) => a > b ? a : b),
60
     ),
61
    );
62
    _mapController?.animateCamera(CameraUpdate.newLatLngBounds(bounds, 50));
63
    _goToNextState();
64
   } catch (e) {
65
    if (mounted) {
66
     ScaffoldMessenger.of(context).showSnackBar(
67
      SnackBar(content: Text('Error: ${e.toString()}')),
68
     );
69
    }
70
   }
71
  }
72
 }
`
Let’s also create the `route` edge functions. This function calls the [routes API from Google](https://developers.google.com/maps/documentation/routes), which provides us the array of lines on the map to take us from the customer’s current location to the destination.
Run the following commands to create the edge functions.
`
1
# initialize Supabase
2
npx supabase init
34
# Create a new function named route
5
npx supabase functions new route
`
`
1
type Coordinates = {
2
 latitude: number
3
 longitude: number
4
}
56
Deno.serve(async (req) => {
7
 const {
8
  origin,
9
  destination,
10
 }: {
11
  origin: Coordinates
12
  destination: Coordinates
13
 } = await req.json()
1415
 const response = await fetch(
16
  `https://routes.googleapis.com/directions/v2:computeRoutes?key=${Deno.env.get(
17
   'GOOGLE_MAPS_API_KEY'
18
  )}`,
19
  {
20
   method: 'POST',
21
   headers: {
22
    'Content-Type': 'application/json',
23
    'X-Goog-FieldMask':
24
     'routes.duration,routes.distanceMeters,routes.polyline,routes.legs.polyline',
25
   },
26
   body: JSON.stringify({
27
    origin: { location: { latLng: origin } },
28
    destination: { location: { latLng: destination } },
29
    travelMode: 'DRIVE',
30
    polylineEncoding: 'GEO_JSON_LINESTRING',
31
   }),
32
  }
33
 )
3435
 if (!response.ok) {
36
  const error = await response.json()
37
  console.error({ error })
38
  throw new Error(`HTTP error! status: ${response.status}`)
39
 }
4041
 const data = await response.json()
4243
 const res = data.routes[0]
4445
 return new Response(JSON.stringify(res), { headers: { 'Content-Type': 'application/json' } })
46
})
`
Once the function is ready, you can [run it locally](https://supabase.com/docs/guides/functions/quickstart) or [deploy it to a remote Supabase instance](https://supabase.com/docs/guides/functions/deploy).
## Step 7: Driver Assignment[#](https://supabase.com/blog/flutter-uber-clone#step-7-driver-assignment)
Now, once a route is displayed on the map and the customer agrees on the fare, a driver needs to be found. We created a convenient method for this earlier, so we can just call the method to find a driver and create a new ride.
If a driver was successfully found, we listen to real-time changes on both the driver and the ride to keep track of the driver’s position and the ride’s current status. For this, we use the [.stream()](https://supabase.com/docs/reference/dart/stream) method.
`
1
 /// Finds a nearby driver
2
 ///
3
 /// When a driver is found, it subscribes to the driver's location and ride status.
4
 Future<void> _findDriver() async {
5
  try {
6
   final response = await supabase.rpc('find_driver', params: {
7
    'origin':
8
      'POINT(${_currentLocation!.longitude} ${_currentLocation!.latitude})',
9
    'destination':
10
      'POINT(${_selectedDestination!.longitude} ${_selectedDestination!.latitude})',
11
    'fare': _fare,
12
   }) as List<dynamic>;
1314
   if (response.isEmpty) {
15
    if (mounted) {
16
     ScaffoldMessenger.of(context).showSnackBar(
17
      const SnackBar(
18
        content: Text('No driver found. Please try again later.')),
19
     );
20
    }
21
    return;
22
   }
23
   String driverId = response.first['driver_id'];
24
   String rideId = response.first['ride_id'];
2526
   _driverSubscription = supabase
27
     .from('drivers')
28
     .stream(primaryKey: ['id'])
29
     .eq('id', driverId)
30
     .listen((List<Map<String, dynamic>> data) {
31
      if (data.isNotEmpty) {
32
       setState(() {
33
        _driver = Driver.fromJson(data[0]);
34
       });
35
       _updateDriverMarker(_driver!);
36
       _adjustMapView(
37
         target: _appState == AppState.waitingForPickup
38
           ? _currentLocation!
39
           : _selectedDestination!);
40
      }
41
     });
4243
   _rideSubscription = supabase
44
     .from('rides')
45
     .stream(primaryKey: ['id'])
46
     .eq('id', rideId)
47
     .listen((List<Map<String, dynamic>> data) {
48
      if (data.isNotEmpty) {
49
       setState(() {
50
        final ride = Ride.fromJson(data[0]);
51
        if (ride.status == RideStatus.riding &&
52
          _appState != AppState.riding) {
53
         _appState = AppState.riding;
54
        } else if (ride.status == RideStatus.completed &&
55
          _appState != AppState.postRide) {
56
         _appState = AppState.postRide;
57
         _cancelSubscriptions();
58
         _showCompletionModal();
59
        }
60
       });
61
      }
62
     });
6364
   _goToNextState();
65
  } catch (e) {
66
   if (mounted) {
67
    ScaffoldMessenger.of(context).showSnackBar(
68
     SnackBar(content: Text('Error: ${e.toString()}')),
69
    );
70
   }
71
  }
72
 }
`
## Step 8: Updating the car icon on the map[#](https://supabase.com/blog/flutter-uber-clone#step-8-updating-the-car-icon-on-the-map)
We will not make an app for the driver in this article, but let’s imagine we had one. As the driver’s car moves, it could update it’s position on the `drivers` table. In the previous step, we are listening to the driver’s position being updated, and using those information, we could move the car in the UI as well.
Implement `_updateDriverMarker` method, which updates the driver’s icon on the map as the position changes. We can also calculate the angle at which the driver is headed to using the previous position and the current position.
`
1
 void _updateDriverMarker(Driver driver) {
2
  setState(() {
3
   _markers.removeWhere((marker) => marker.markerId.value == 'driver');
45
   double rotation = 0;
6
   if (_previousDriverLocation != null) {
7
    rotation =
8
      _calculateRotation(_previousDriverLocation!, driver.location);
9
   }
1011
   _markers.add(Marker(
12
    markerId: const MarkerId('driver'),
13
    position: driver.location,
14
    icon: _carIcon!,
15
    anchor: const Offset(0.5, 0.5),
16
    rotation: rotation,
17
   ));
1819
   _previousDriverLocation = driver.location;
20
  });
21
 }
2223
 void _adjustMapView({required LatLng target}) {
24
  if (_driver != null && _selectedDestination != null) {
25
   LatLngBounds bounds = LatLngBounds(
26
    southwest: LatLng(
27
     min(_driver!.location.latitude, target.latitude),
28
     min(_driver!.location.longitude, target.longitude),
29
    ),
30
    northeast: LatLng(
31
     max(_driver!.location.latitude, target.latitude),
32
     max(_driver!.location.longitude, target.longitude),
33
    ),
34
   );
35
   _mapController?.animateCamera(CameraUpdate.newLatLngBounds(bounds, 100));
36
  }
37
 }
3839
 double _calculateRotation(LatLng start, LatLng end) {
40
  double latDiff = end.latitude - start.latitude;
41
  double lngDiff = end.longitude - start.longitude;
42
  double angle = atan2(lngDiff, latDiff);
43
  return angle * 180 / pi;
44
 }
`
## Step 9: Ride Completion[#](https://supabase.com/blog/flutter-uber-clone#step-9-ride-completion)
Finally when the car arrives at the destination (when the driver updates the status to `completed`), a modal thanking the user for using the app shows up. Implement `_showCompletionModal` to greet our valuable customers.
Upon closing the modal, we reset the app’s state so that the user can take another ride.
`
1
 /// Shows a modal to indicate that the ride has been completed.
2
 void _showCompletionModal() {
3
  showDialog(
4
   context: context,
5
   barrierDismissible: false,
6
   builder: (BuildContext context) {
7
    return AlertDialog(
8
     title: const Text('Ride Completed'),
9
     content: const Text(
10
       'Thank you for using our service! We hope you had a great ride.'),
11
     actions: <Widget>[
12
      TextButton(
13
       child: const Text('Close'),
14
       onPressed: () {
15
        Navigator.of(context).pop();
16
        _resetAppState();
17
       },
18
      ),
19
     ],
20
    );
21
   },
22
  );
23
 }
2425
 void _resetAppState() {
26
  setState(() {
27
   _appState = AppState.choosingLocation;
28
   _selectedDestination = null;
29
   _driver = null;
30
   _fare = null;
31
   _polylines.clear();
32
   _markers.clear();
33
   _previousDriverLocation = null;
34
  });
35
  _getCurrentLocation();
36
 }
`
With the edge function deployed, you should be able to run the app at this point. Note that you do need to manually tweak the driver and ride data to test out all the features. I have created a [simple script that simulates the movement and status updates of a driver](https://github.com/dshukertjr/uber-clone/tree/main/scripts/dart) so that you can enjoy the full Uber experience without actually manually updating anything from the dashboard.
You can also find the complete code [here](https://github.com/dshukertjr/uber-clone) to fully see everything put together.
## Conclusion[#](https://supabase.com/blog/flutter-uber-clone#conclusion)
This tutorial has walked you through the process of building a basic Uber clone using Flutter and Supabase. The application demonstrates how easy it is to handle real-time geospatial data using Supabase and Flutter.
This implementation serves as a foundation that can be expanded upon. Additional features such as processing payments, ride history, and driver ratings can be incorporated to enhance the application's functionality.
Want to learn more about Maps and PostGIS? Make sure to follow our [Twitter](https://x.com/supabase) and [YouTube](https://www.youtube.com/@Supabase) channels to not miss out! See you then!
## More Supabase Resources[#](https://supabase.com/blog/flutter-uber-clone#more-supabase-resources)
  * [Flutter Tutorial: building a Flutter chat app](https://supabase.com/blog/flutter-tutorial-building-a-chat-app)
  * [Generate Flame template using Very Good CLI](https://verygood.ventures/blog/generate-a-game-with-our-new-template)
  * [Supabase Flutter SDK docs](https://supabase.com/docs/reference/dart/start)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-uber-clone&text=Building%20an%20Uber%20Clone%20with%20Flutter%20and%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-uber-clone&text=Building%20an%20Uber%20Clone%20with%20Flutter%20and%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-uber-clone&t=Building%20an%20Uber%20Clone%20with%20Flutter%20and%20Supabase)
[Last postEdge Functions are now 2x smaller and boot 3x faster12 September 2024](https://supabase.com/blog/edge-functions-faster-smaller)
[Next postIn-Browser Semantic AI Search with PGlite and Transformers.js29 August 2024](https://supabase.com/blog/in-browser-semantic-search-pglite)
[realtime](https://supabase.com/blog/tags/realtime)[flutter](https://supabase.com/blog/tags/flutter)
On this page
  * [App Overview](https://supabase.com/blog/flutter-uber-clone#app-overview)
  * [Prerequisites](https://supabase.com/blog/flutter-uber-clone#prerequisites)
  * [Step 1: Project Setup](https://supabase.com/blog/flutter-uber-clone#step-1-project-setup)
  * [Step 2: Supabase Initialization](https://supabase.com/blog/flutter-uber-clone#step-2-supabase-initialization)
  * [Step 3: Database Configuration](https://supabase.com/blog/flutter-uber-clone#step-3-database-configuration)
  * [Step 4: Defining the models](https://supabase.com/blog/flutter-uber-clone#step-4-defining-the-models)
  * [Step 5: Main UI Implementation](https://supabase.com/blog/flutter-uber-clone#step-5-main-ui-implementation)
  * [Step 6: Location Selection Implementation](https://supabase.com/blog/flutter-uber-clone#step-6-location-selection-implementation)
  * [Step 7: Driver Assignment](https://supabase.com/blog/flutter-uber-clone#step-7-driver-assignment)
  * [Step 8: Updating the car icon on the map](https://supabase.com/blog/flutter-uber-clone#step-8-updating-the-car-icon-on-the-map)
  * [Step 9: Ride Completion](https://supabase.com/blog/flutter-uber-clone#step-9-ride-completion)
  * [Conclusion](https://supabase.com/blog/flutter-uber-clone#conclusion)
  * [More Supabase Resources](https://supabase.com/blog/flutter-uber-clone#more-supabase-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-uber-clone&text=Building%20an%20Uber%20Clone%20with%20Flutter%20and%20Supabase)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-uber-clone&text=Building%20an%20Uber%20Clone%20with%20Flutter%20and%20Supabase)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fflutter-uber-clone&t=Building%20an%20Uber%20Clone%20with%20Flutter%20and%20Supabase)
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

