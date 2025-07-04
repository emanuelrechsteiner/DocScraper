---
url: https://supabase.com/blog/react-native-storage
scraped_at: 2025-05-25T09:06:30.451690
title: React Native file upload with Supabase Storage
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
# React Native file upload with Supabase Storage
01 Aug 2023
•
21 minute read
[![Simon Grimm avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsaimon24.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Simon GrimmGuest Author](https://twitter.com/schlimmson)
![React Native file upload with Supabase Storage](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-01-react-native-storage%2Freact-native-storage.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
If you want to upload files from your React Native app, you need a backend to store the files, [Supabase Storage](https://supabase.com/docs/guides/storage) is a great choice for this as it provides a simple API to upload files, and we can easily combine this with authentication to build a powerful app.
This means you can quickly build your own image-sharing app, a file-sharing app, or any other app that needs to upload files to a backend!
![Supabase File Upload React Native](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-01-react-native-storage%2Fsupabase-file-upload-react-native.gif&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
In this tutorial, you will learn to:
  * Set up a React Native app with [Expo SDK49](https://expo.dev/)
  * Use [Supabase Authentication](https://supabase.com/docs/guides/auth)
  * Work with Expo Router v2 and protected routes
  * Upload files to [Supabase Storage](https://supabase.com/docs/guides/storage)


You can also directly check out the [full source code on Github](https://github.com/saimon24/react-native-resumable-upload-supabase) so you can get started with Supabase fast!
Before we get into the app, let's quickly [start a new Supabase project](https://supabase.com/dashboard).
## Creating the Supabase Project[#](https://supabase.com/blog/react-native-storage#creating-the-supabase-project)
To use authentication and storage we need a new Supabase project. If you don't have a Supabase account yet, you can [get started for free](https://supabase.com/dashboard)!
In your dashboard, click "New Project" and leave it to the default settings, but make sure you keep a copy of your Database password!
![Supabase new project](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-01-react-native-storage%2Fnew-project.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
After a minute your project should be ready, and we can configure the authentication and storage.
## Setting up Authentication[#](https://supabase.com/blog/react-native-storage#setting-up-authentication)
Authentication will be enabled by default, but we want to turn off email confirmation for this tutorial.
Select **Authentication** from the menu, go to the **Providers** section, and expand Email.
![Email Authentication settings](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-01-react-native-storage%2Femail-auth.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Here you can disable the confirmation email, and apply other changes later if you want to!
## Setting up Storage[#](https://supabase.com/blog/react-native-storage#setting-up-storage)
Now we want to create a **bucket** under storage where we will upload our files, and also add some security rules to protect the files of a user.
First, select **Storage** from the menu, then click **New bucket** and call it `files`.
![Supabase new bucket](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-01-react-native-storage%2Fnew-bucket.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Make sure that this is not a public bucket, otherwise, even unauthenticated users can upload or read the files!
To protect that bucket and allow users only access to their own folder, we need to add some [Storage policies](https://supabase.com/docs/guides/storage/security/access-control).
You can either do this through the UI and pick from examples, or simply run my SQL script in the **SQL Editor** which you can select from the menu:
`
1
CREATE POLICY "Enable storage access for users based on user_id" ON "storage"."objects"
2
AS PERMISSIVE FOR ALL
3
TO public
4
USING (bucket_id = 'files' AND (SELECT auth.uid()::text )= (storage.foldername(name))[1])
5
WITH CHECK (bucket_id = 'files' AND (SELECT auth.uid()::text) = (storage.foldername(name))[1])
`
This will allow users to only access their own folder, and not any other files in the bucket.
## Setting up the React Native app[#](https://supabase.com/blog/react-native-storage#setting-up-the-react-native-app)
Now that we have our Supabase project ready, we can start building the React Native app!
Get started by setting up a new Expo app with the tabs template and install some dependencies:
`
1
# Create a new Expo app
2
npx create-expo-app@latest cloudApp --template tabs@49
34
# Install dependencies
5
npm i @supabase/supabase-js
6
npm i react-native-url-polyfill base64-arraybuffer react-native-loading-spinner-overlay @react-native-async-storage/async-storage
78
# Install Expo packages
9
npx expo install expo-image-picker
10
npx expo install expo-file-system
`
We will use the [Expo AsyncStorage](https://docs.expo.dev/versions/latest/sdk/async-storage/) to store the Supabase session, and the [Expo Image Picker](https://docs.expo.dev/versions/latest/sdk/imagepicker/) to select images from the device. We also need the [Expo File System](https://docs.expo.dev/versions/latest/sdk/filesystem/) to read the image from the device and upload its data.
You can now already run your project with `npx expo` and then select a platform to run on.
However, the tabs template contains a lot of code that we don't need, so to simplify things we can remove the **app** , **constants** and **components** folder.
This gives us a much cleaner project structure.
## Connecting to Supabase from React Native[#](https://supabase.com/blog/react-native-storage#connecting-to-supabase-from-react-native)
To use Supabase we need to initialize the client with our project URL and the public key, which you can find in the **Settings** of your project under **API**.
You can put both of them in a `.env` file at the root of your project:
`
1
EXPO_PUBLIC_SUPABASE_URL=
2
EXPO_PUBLIC_SUPABASE_ANON_KEY=
`
We can now simply read those values from the environment variables and initialize the Supabase client, so create a file at `config/initSupabase.ts` and add the following code:
`
1
import AsyncStorage from '@react-native-async-storage/async-storage'
2
import 'react-native-url-polyfill/auto'
34
import { createClient } from '@supabase/supabase-js'
56
const url = process.env.EXPO_PUBLIC_SUPABASE_URL
7
const key = process.env.EXPO_PUBLIC_SUPABASE_ANON_KEY
89
// Initialize the Supabase client
10
export const supabase = createClient(url, key, {
11
 auth: {
12
  storage: AsyncStorage,
13
  detectSessionInUrl: false,
14
 },
15
})
`
We are using the AsyncStorage from Expo to handle the session of our Supabase client and add in the `createClient` function.
Later we can import the `supabase` client from this file and use it in our app whenever we need to access Supabase.
## Building the authentication flow[#](https://supabase.com/blog/react-native-storage#building-the-authentication-flow)
Currently, the app won't work as we have no entry point. Because we are using the Expon Router and file-based routing, we can create a new file at `app/index.tsx` which will be the first page that comes up in our app.
On this page we will handle both login and registration, so let's start by creating a simple form with a few inputs and buttons inside the `app/index.tsx` file:
`
1
import { Alert, View, Button, TextInput, StyleSheet, Text, TouchableOpacity } from 'react-native'
2
import { useState } from 'react'
3
import React from 'react'
4
import Spinner from 'react-native-loading-spinner-overlay'
5
import { supabase } from '../config/initSupabase'
67
const Login = () => {
8
 const [email, setEmail] = useState('')
9
 const [password, setPassword] = useState('')
10
 const [loading, setLoading] = useState(false)
1112
 // Sign in with email and password
13
 const onSignInPress = async () => {
14
  setLoading(true)
1516
  const { error } = await supabase.auth.signInWithPassword({
17
   email,
18
   password,
19
  })
2021
  if (error) Alert.alert(error.message)
22
  setLoading(false)
23
 }
2425
 // Create a new user
26
 const onSignUpPress = async () => {
27
  setLoading(true)
28
  const { error } = await supabase.auth.signUp({
29
   email: email,
30
   password: password,
31
  })
3233
  if (error) Alert.alert(error.message)
34
  setLoading(false)
35
 }
3637
 return (
38
  <View style={styles.container}>
39
   <Spinner visible={loading} />
4041
   <Text style={styles.header}>My Cloud</Text>
4243
   <TextInput
44
    autoCapitalize="none"
45
    placeholder="john@doe.com"
46
    value={email}
47
    onChangeText={setEmail}
48
    style={styles.inputField}
49
   />
50
   <TextInput
51
    placeholder="password"
52
    value={password}
53
    onChangeText={setPassword}
54
    secureTextEntry
55
    style={styles.inputField}
56
   />
5758
   <TouchableOpacity onPress={onSignInPress} style={styles.button}>
59
    <Text style={{ color: '#fff' }}>Sign in</Text>
60
   </TouchableOpacity>
61
   <Button onPress={onSignUpPress} title="Create Account" color={'#fff'}></Button>
62
  </View>
63
 )
64
}
6566
const styles = StyleSheet.create({
67
 container: {
68
  flex: 1,
69
  paddingTop: 200,
70
  padding: 20,
71
  backgroundColor: '#151515',
72
 },
73
 header: {
74
  fontSize: 30,
75
  textAlign: 'center',
76
  margin: 50,
77
  color: '#fff',
78
 },
79
 inputField: {
80
  marginVertical: 4,
81
  height: 50,
82
  borderWidth: 1,
83
  borderColor: '#2b825b',
84
  borderRadius: 4,
85
  padding: 10,
86
  color: '#fff',
87
  backgroundColor: '#363636',
88
 },
89
 button: {
90
  marginVertical: 15,
91
  alignItems: 'center',
92
  backgroundColor: '#2b825b',
93
  padding: 12,
94
  borderRadius: 4,
95
 },
96
})
9798
export default Login
`
There's nothing fancy going on here, but this is all we need to use Supabase Authentication in our app!
![Login page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-01-react-native-storage%2Flogin-page.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
You can try it out right now and create a new user account or sign in with an existing one and log the values to the console to see what's going on.
However, we are not handling the authentication state yet so let's create a **Context** to listen to changes.
We will wrap a Provider around our app, which will use the `onAuthStateChange` function from Supabase to listen to changes in the authentication state and accordingly set our state.
For this, create a new file at `provider/AuthProvider.tsx` and add the following code:
`
1
import React, { useState, useEffect, createContext, PropsWithChildren } from 'react'
2
import { Session, User } from '@supabase/supabase-js'
3
import { supabase } from '../config/initSupabase'
45
type AuthProps = {
6
 user: User | null
7
 session: Session | null
8
 initialized?: boolean
9
 signOut?: () => void
10
}
1112
export const AuthContext = createContext<Partial<AuthProps>>({})
1314
// Custom hook to read the context values
15
export function useAuth() {
16
 return React.useContext(AuthContext)
17
}
1819
export const AuthProvider = ({ children }: PropsWithChildren) => {
20
 const [user, setUser] = useState<User | null>()
21
 const [session, setSession] = useState<Session | null>(null)
22
 const [initialized, setInitialized] = useState<boolean>(false)
2324
 useEffect(() => {
25
  // Listen for changes to authentication state
26
  const { data } = supabase.auth.onAuthStateChange(async (event, session) => {
27
   setSession(session)
28
   setUser(session ? session.user : null)
29
   setInitialized(true)
30
  })
31
  return () => {
32
   data.subscription.unsubscribe()
33
  }
34
 }, [])
3536
 // Log out the user
37
 const signOut = async () => {
38
  await supabase.auth.signOut()
39
 }
4041
 const value = {
42
  user,
43
  session,
44
  initialized,
45
  signOut,
46
 }
4748
 return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
49
}
`
To use the context we can now wrap it around our app, and while we do this we can also take care of the navigation:
In the topmost layout file we can check whether a user has an active session or not, and either directly sign the user into the inside area (that we will create soon) or automatically bring her back to the login screen.
To make this work with the Expo Router we can create a file at `app/_layout.tsx` and add the following code:
`
1
import { Slot, useRouter, useSegments } from 'expo-router'
2
import { useEffect } from 'react'
3
import { AuthProvider, useAuth } from '../provider/AuthProvider'
45
// Makes sure the user is authenticated before accessing protected pages
6
const InitialLayout = () => {
7
 const { session, initialized } = useAuth()
8
 const segments = useSegments()
9
 const router = useRouter()
1011
 useEffect(() => {
12
  if (!initialized) return
1314
  // Check if the path/url is in the (auth) group
15
  const inAuthGroup = segments[0] === '(auth)'
1617
  if (session && !inAuthGroup) {
18
   // Redirect authenticated users to the list page
19
   router.replace('/list')
20
  } else if (!session) {
21
   // Redirect unauthenticated users to the login page
22
   router.replace('/')
23
  }
24
 }, [session, initialized])
2526
 return <Slot />
27
}
2829
// Wrap the app with the AuthProvider
30
const RootLayout = () => {
31
 return (
32
  <AuthProvider>
33
   <InitialLayout />
34
  </AuthProvider>
35
 )
36
}
3738
export default RootLayout
`
Whenever the `initialized` or `session` state changes, we check if the user is authenticated and redirect her to the correct page.
This also means we don't have to worry about the authentication state in our pages anymore, we can just assume that the user is authenticated and use the `useAuth` hook to access the user and session data later on.
Your app might show an error right now because the `/list` route doesn't exist yet, but we will create it in the next step.
## File Upload to Supabase Storage[#](https://supabase.com/blog/react-native-storage#file-upload-to-supabase-storage)
Now that we have the authentication set up, we can start working on the file upload.
First, let's define another layout for this inside area so create a file at `/app/(auth)/_layout.tsx` and add the following code:
`
1
import { Stack } from 'expo-router'
2
import { useAuth } from '../../provider/AuthProvider'
3
import React from 'react'
4
import { TouchableOpacity } from 'react-native'
5
import { Ionicons } from '@expo/vector-icons'
67
// Simple stack layout within the authenticated area
8
const StackLayout = () => {
9
 const { signOut } = useAuth()
1011
 return (
12
  <Stack
13
   screenOptions={{
14
    headerStyle: {
15
     backgroundColor: '#0f0f0f',
16
    },
17
    headerTintColor: '#fff',
18
   }}
19
  >
20
   <Stack.Screen
21
    name="list"
22
    options={{
23
     headerTitle: 'My Files',
24
     headerRight: () => (
25
      <TouchableOpacity onPress={signOut}>
26
       <Ionicons name="log-out-outline" size={30} color={'#fff'} />
27
      </TouchableOpacity>
28
     ),
29
    }}
30
   ></Stack.Screen>
31
  </Stack>
32
 )
33
}
3435
export default StackLayout
`
This defines a simple stack navigation and adds a button to trigger the logout, so we can now also fully test the authentication flow.
Next, we create the page for uploading and displaying all files of a user from Supabase Storage.
You won't have any files to show yet, but loading the files of a user is as easy as calling `list()` on the storage bucket and passing the user id as the folder name.
Additionally, we add a little FAB (floating action button) to trigger the file picker, so create a file at `/app/(auth)/list.tsx` and add the following code:
`
1
import { View, StyleSheet, TouchableOpacity, ScrollView } from 'react-native'
2
import React, { useEffect, useState } from 'react'
3
import { Ionicons } from '@expo/vector-icons'
4
import * as ImagePicker from 'expo-image-picker'
5
import { useAuth } from '../../provider/AuthProvider'
6
import * as FileSystem from 'expo-file-system'
7
import { decode } from 'base64-arraybuffer'
8
import { supabase } from '../../config/initSupabase'
9
import { FileObject } from '@supabase/storage-js'
1011
const list = () => {
12
 const { user } = useAuth()
13
 const [files, setFiles] = useState<FileObject[]>([])
1415
 useEffect(() => {
16
  if (!user) return
1718
  // Load user images
19
  loadImages()
20
 }, [user])
2122
 const loadImages = async () => {
23
  const { data } = await supabase.storage.from('files').list(user!.id)
24
  if (data) {
25
   setFiles(data)
26
  }
27
 }
2829
 const onSelectImage = async () => {
30
  // TODO
31
 }
3233
 return (
34
  <View style={styles.container}>
35
   {/* FAB to add images */}
36
   <TouchableOpacity onPress={onSelectImage} style={styles.fab}>
37
    <Ionicons name="camera-outline" size={30} color={'#fff'} />
38
   </TouchableOpacity>
39
  </View>
40
 )
41
}
4243
const styles = StyleSheet.create({
44
 container: {
45
  flex: 1,
46
  padding: 20,
47
  backgroundColor: '#151515',
48
 },
49
 fab: {
50
  borderWidth: 1,
51
  alignItems: 'center',
52
  justifyContent: 'center',
53
  width: 70,
54
  position: 'absolute',
55
  bottom: 40,
56
  right: 30,
57
  height: 70,
58
  backgroundColor: '#2b825b',
59
  borderRadius: 100,
60
 },
61
})
6263
export default list
`
This should give us a nice and clean UI.
![Files page](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-01-react-native-storage%2Ffiles-page.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Now we can implement the image picker and upload the selected image to Supabase Storage.
Using the image picker from Expo gives us a **URI** , which we can use to read the file from the file system and convert it to a base64 string.
We can then use the `upload()` method from the storage client to upload the file to the storage bucket. Life can be easy.
At this point, you should be able to upload files to Supabase Storage, and you can already see them in your UI (or log them to the console).
To finally display them we will add a `ScrollView` component, which will render one item for every file of a user.
Let's start by creating those component rows in another file, so create a `components/ImageItem.tsx` file and add the following code:
`
1
import { FileObject } from '@supabase/storage-js'
2
import { Image, View, Text, TouchableOpacity } from 'react-native'
3
import { supabase } from '../config/initSupabase'
4
import { useState } from 'react'
5
import { Ionicons } from '@expo/vector-icons'
67
// Image item component that displays the image from Supabase Storage and a delte button
8
const ImageItem = ({
9
 item,
10
 userId,
11
 onRemoveImage,
12
}: {
13
 item: FileObject
14
 userId: string
15
 onRemoveImage: () => void
16
}) => {
17
 const [image, setImage] = useState<string>('')
1819
 supabase.storage
20
  .from('files')
21
  .download(`${userId}/${item.name}`)
22
  .then(({ data }) => {
23
   const fr = new FileReader()
24
   fr.readAsDataURL(data!)
25
   fr.onload = () => {
26
    setImage(fr.result as string)
27
   }
28
  })
2930
 return (
31
  <View style={{ flexDirection: 'row', margin: 1, alignItems: 'center', gap: 5 }}>
32
   {image ? (
33
    <Image style={{ width: 80, height: 80 }} source={{ uri: image }} />
34
   ) : (
35
    <View style={{ width: 80, height: 80, backgroundColor: '#1A1A1A' }} />
36
   )}
37
   <Text style={{ flex: 1, color: '#fff' }}>{item.name}</Text>
38
   {/* Delete image button */}
39
   <TouchableOpacity onPress={onRemoveImage}>
40
    <Ionicons name="trash-outline" size={20} color={'#fff'} />
41
   </TouchableOpacity>
42
  </View>
43
 )
44
}
4546
export default ImageItem
`
This component will display the image from Supabase Storage, the name of the file and a delete button.
To display the image we use the `download()` method from the storage client, which returns a `FileObject` with the file data. We can then use the `FileReader` to convert the file data to a base64 string, which we can use as the image source.
Now let's use this component in our `list.tsx` file to render the list of images by updating the `return` statement:
`
1
return (
2
 <View style={styles.container}>
3
  <ScrollView>
4
   {files.map((item, index) => (
5
    <ImageItem
6
     key={item.id}
7
     item={item}
8
     userId={user!.id}
9
     onRemoveImage={() => onRemoveImage(item, index)}
10
    />
11
   ))}
12
  </ScrollView>
1314
  {/* FAB to add images */}
15
  <TouchableOpacity onPress={onSelectImage} style={styles.fab}>
16
   <Ionicons name="camera-outline" size={30} color={'#fff'} />
17
  </TouchableOpacity>
18
 </View>
19
)
`
Don't forget to also include the import to the `ImageItem` component!
![Supabase Storage Files List](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2023-08-01-react-native-storage%2Fsupabase-storage-files.png&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Finally, we can also include the delete functionality by adding the following code to the `list.tsx`:
`
1
const onRemoveImage = async (item: FileObject, listIndex: number) => {
2
 supabase.storage.from('files').remove([`${user!.id}/${item.name}`])
3
 const newFiles = [...files]
4
 newFiles.splice(listIndex, 1)
5
 setFiles(newFiles)
6
}
`
We are handling the deletion here so we can accordingly update the state of the files list after removing an item.
And with that in place, you have a fully functional image gallery app with React Native and Supabase Storage!
## What about resumable uploads?[#](https://supabase.com/blog/react-native-storage#what-about-resumable-uploads)
Initially, I wanted to include [resumable uploads](https://supabase.com/blog/storage-v3-resumable-uploads) in this tutorial, but apparently, the [Uppy](https://uppy.io/) client didn't work 100% for React Native yet.
You can still see an [initial implementation of resumable downloads with Supabase and React Native](https://github.com/saimon24/react-native-resumable-upload-supabase/commit/bb45455dc2d4d3fdd42089a8a26a521cc5b5e60f#diff-2d97fcb7ad2b1ac426a8d5391cfd0ab970e525ede1f11e14885f65e6dcd116a1) in the repository of this tutorial.
However, ultimately the uploaded file was always 0 bytes, so I decided to leave it out for now.
The Supabase team is investigating this issue, so I'm very sure that we will have resumable uploads working with React Native soon.
## Conclusion[#](https://supabase.com/blog/react-native-storage#conclusion)
It's almost too easy to use Supabase Storage, and it's a great way to store files for your apps.
You now have a fully functional image gallery app with React Native and Supabase Storage including user authentication without writing a line of backend code!
You can [find the full code of this tutorial on Github](https://github.com/saimon24/react-native-resumable-upload-supabase) where you just need to insert your own Supabase URL and API key.
If you enjoyed the tutorial, you can [learn React Native on Galaxies.dev](https://galaxies.dev) where I help developers build awesome React Native apps.
Until next time and happy coding with Supabase!
## More React Native/Expo resources[#](https://supabase.com/blog/react-native-storage#more-react-nativeexpo-resources)
  * [Getting started with React Native authentication](https://supabase.com/blog/react-native-authentication)
  * [Offline-first React Native Apps with Expo, WatermelonDB](https://supabase.com/blog/react-native-offline-first-watermelon-db)
  * [React Native Quickstart](https://supabase.com/docs/guides/auth/quickstarts/react-native)
  * [Watch our React Native video tutorials](https://youtube.com/playlist?list=PL5S4mPUpp4OsrbRTx21k34aACOgpqQGlx&si=Ez-0S4QhBxtayYsq)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-storage&text=React%20Native%20file%20upload%20with%20Supabase%20Storage)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-storage&text=React%20Native%20file%20upload%20with%20Supabase%20Storage)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-storage&t=React%20Native%20file%20upload%20with%20Supabase%20Storage)
[Last postSupabase Beta July 20232 August 2023](https://supabase.com/blog/beta-update-july-2023)
[Next postSupabase Launch Week 8 Hackathon25 July 2023](https://supabase.com/blog/supabase-lw8-hackathon)
[react-native](https://supabase.com/blog/tags/react-native)[storage](https://supabase.com/blog/tags/storage)
On this page
  * [Creating the Supabase Project](https://supabase.com/blog/react-native-storage#creating-the-supabase-project)
  * [Setting up Authentication](https://supabase.com/blog/react-native-storage#setting-up-authentication)
  * [Setting up Storage](https://supabase.com/blog/react-native-storage#setting-up-storage)
  * [Setting up the React Native app](https://supabase.com/blog/react-native-storage#setting-up-the-react-native-app)
  * [Connecting to Supabase from React Native](https://supabase.com/blog/react-native-storage#connecting-to-supabase-from-react-native)
  * [Building the authentication flow](https://supabase.com/blog/react-native-storage#building-the-authentication-flow)
  * [File Upload to Supabase Storage](https://supabase.com/blog/react-native-storage#file-upload-to-supabase-storage)
  * [What about resumable uploads?](https://supabase.com/blog/react-native-storage#what-about-resumable-uploads)
  * [Conclusion](https://supabase.com/blog/react-native-storage#conclusion)
  * [More React Native/Expo resources](https://supabase.com/blog/react-native-storage#more-react-nativeexpo-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-storage&text=React%20Native%20file%20upload%20with%20Supabase%20Storage)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-storage&text=React%20Native%20file%20upload%20with%20Supabase%20Storage)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Freact-native-storage&t=React%20Native%20file%20upload%20with%20Supabase%20Storage)
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

