---
url: https://supabase.com/docs/reference/self-hosting-auth/passwordless-sign-in-method-for-email-or-phone
scraped_at: 2025-05-25T09:10:12.284075
title: Self-Hosting | Supabase Docs
---

[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Main menu
Self-Hosting Auth
  * [Introduction](https://supabase.com/docs/reference/self-hosting-auth/introduction)
  * Usage
    * [Generates an email action link](https://supabase.com/docs/reference/self-hosting-auth/generates-an-email-action-link)
    * [Get a user](https://supabase.com/docs/reference/self-hosting-auth/get-a-user)
    * [Update a user](https://supabase.com/docs/reference/self-hosting-auth/update-a-user)
    * [Deletes a user](https://supabase.com/docs/reference/self-hosting-auth/deletes-a-user)
    * [List all users](https://supabase.com/docs/reference/self-hosting-auth/list-all-users)
    * [Returns the created user](https://supabase.com/docs/reference/self-hosting-auth/returns-the-created-user)
    * [Receives the redirect from an external provider during the oauth authentication process starts the process of creating an access and refresh token](https://supabase.com/docs/reference/self-hosting-auth/receives-the-redirect-from-an-external-provider-during-the-oauth-authentication-process-starts-the-process-of-creating-an-access-and-refresh-token)
    * [The healthcheck endpoint for gotrue returns the current gotrue version](https://supabase.com/docs/reference/self-hosting-auth/the-healthcheck-endpoint-for-gotrue-returns-the-current-gotrue-version)
    * [Sends an invite link to the user](https://supabase.com/docs/reference/self-hosting-auth/sends-an-invite-link-to-the-user)
    * [Logs out the user](https://supabase.com/docs/reference/self-hosting-auth/logs-out-the-user)
    * [Passwordless sign in method for email or phone](https://supabase.com/docs/reference/self-hosting-auth/passwordless-sign-in-method-for-email-or-phone)
    * [Sends a password recovery email link to the users email](https://supabase.com/docs/reference/self-hosting-auth/sends-a-password-recovery-email-link-to-the-users-email)
    * [Returns the configuration settings for the gotrue server](https://supabase.com/docs/reference/self-hosting-auth/returns-the-configuration-settings-for-the-gotrue-server)
    * [Password based signup with either email or phone](https://supabase.com/docs/reference/self-hosting-auth/password-based-signup-with-either-email-or-phone)
    * [Signs in a user with a password](https://supabase.com/docs/reference/self-hosting-auth/signs-in-a-user-with-a-password)
    * [Refreshes a users refresh token](https://supabase.com/docs/reference/self-hosting-auth/refreshes-a-users-refresh-token)
    * [Get information for the logged in user](https://supabase.com/docs/reference/self-hosting-auth/get-information-for-the-logged-in-user)
    * [Returns the updated user](https://supabase.com/docs/reference/self-hosting-auth/returns-the-updated-user)
    * [Verifies a sign up](https://supabase.com/docs/reference/self-hosting-auth/verifies-a-sign-up)


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
  * [Start](https://supabase.com/docs/guides/getting-started)
  * Products 
  * Build 
  * Manage 
  * Reference 
  * Resources 


[![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-dark.svg&w=256&q=75)![Supabase wordmark](https://supabase.com/docs/_next/image?url=%2Fdocs%2Fsupabase-light.svg&w=256&q=75)DOCS](https://supabase.com/docs)
Search docs...
K
[Sign up](https://supabase.com/dashboard)
Auth Server Reference
# Self-Hosting Auth
The Supabase Auth Server (GoTrue) is a JSON Web Token (JWT)-based API for managing users and issuing access tokens.
GoTrue is an open-source API written in Golang, that acts as a self-standing API service for handling user registration and authentication for JAM projects. It's based on OAuth2 and JWT and handles user signup, authentication, and custom user data.
### Client libraries[#](https://supabase.com/docs/reference/self-hosting-auth/passwordless-sign-in-method-for-email-or-phone#client-libraries)
  * [JavaScript](https://github.com/supabase/gotrue-js)
  * [Dart](https://github.com/supabase/gotrue-dart)


### Additional links[#](https://supabase.com/docs/reference/self-hosting-auth/passwordless-sign-in-method-for-email-or-phone#additional-links)
  * [Source code](https://github.com/supabase/gotrue)
  * [Known bugs and issues](https://github.com/supabase/gotrue/issues)
  * [Auth guides](https://supabase.com/docs/guides/auth)


## Generates an email action link.
post`/admin/generate_link`
### Body
application/json
  * dataOptionalobject
Object schema
  * emailOptionalstring
  * new_emailOptionalstring
  * passwordOptionalstring
  * redirect_toOptionalstring
  * typeOptionalstring


### Response codes
  * 200
  * 401


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
{"action_link":"lorem","app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","email_otp":"lorem","hashed_token":"lorem","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"  } ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","redirect_to":"lorem","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null },"verification_type":"lorem"}

```

## Get a user.
get`/admin/user/{user_id}`
### Path parameters
  * user_idRequired
The user's id


### Response codes
  * 200
  * 401


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
{"app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"  } ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null }}

```

## Update a user.
put`/admin/user/{user_id}`
### Path parameters
  * user_idRequired
The user's id


### Response codes
  * 200
  * 401


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
{"app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"  } ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null }}

```

## Deletes a user.
delete`/admin/user/{user_id}`
### Path parameters
  * user_idRequired
The user's id


### Response codes
  * 200
  * 401


### Response (200)
schema
```

1
{}

```

## List all users.
get`/admin/users`
### Response codes
  * 200
  * 401


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
{"aud":"lorem","users": [{"app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"}   ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null   }  } ]}

```

## Returns the created user.
post`/admin/users`
### Body
application/json
  * app_metadataOptionalobject
Object schema
  * audOptionalstring
  * ban_durationOptionalstring
  * emailOptionalstring
  * email_confirmOptionalboolean
  * passwordOptionalstring
  * phoneOptionalstring
  * phone_confirmOptionalboolean
  * roleOptionalstring
  * user_metadataOptionalobject
Object schema


### Response codes
  * 200
  * 401


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
{"app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"  } ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null }}

```

## Receives the redirect from an external provider during the OAuth authentication process. Starts the process of creating an access and refresh token.
get`/callback`
### Response codes
  * 302


## The healthcheck endpoint for gotrue. Returns the current gotrue version.
get`/health`
### Response codes
  * 200


### Response (200)
exampleschema
```

1
2
3
4
5
{"description":"lorem","name":"lorem","version":"lorem"}

```

## Sends an invite link to the user.
post`/invite`
### Body
application/json
  * dataOptionalobject
Object schema
  * emailOptionalstring


### Response codes
  * 200


### Response (200)
schema
```

1
{}

```

## Logs out the user.
post`/logout`
### Response codes
  * 204


### Response (204)
schema
```

1
{}

```

## Passwordless sign-in method for email or phone.
post`/otp`
### Body
application/json
  * create_userOptionalboolean
  * dataOptionalobject
Object schema
  * emailOptionalstring
  * phoneOptionalstring


### Response codes
  * 200


### Response (200)
schema
```

1
{}

```

## Sends a password recovery email link to the user's email.
post`/recover`
### Body
application/json
  * emailOptionalstring


### Response codes
  * 200


### Response (200)
schema
```

1
{}

```

## Returns the configuration settings for the gotrue server.
get`/settings`
### Response codes
  * 200


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
{"disable_signup":true,"external":{"apple":true,"azure":true,"bitbucket":true,"discord":true,"email":true,"facebook":true,"github":true,"gitlab":true,"google":true,"keycloak":true,"linkedin":true,"notion":true,"phone":true,"saml":true,"slack":true,"spotify":true,"twitch":true,"twitter":true,"workos":true,"zoom":true},"mailer_autoconfirm":true,"phone_autoconfirm":true,"sms_provider":"lorem"}

```

## Password-based signup with either email or phone.
post`/signup`
### Body
application/json
  * dataOptionalobject
Object schema
  * emailOptionalstring
  * passwordOptionalstring
  * phoneOptionalstring


### Response codes
  * 200


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
{"app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"  } ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null }}

```

## Signs in a user with a password.
post`/token?grant_type=password`
### Body
application/json
  * emailOptionalstring
  * passwordOptionalstring
  * phoneOptionalstring


### Response codes
  * 200


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
{"access_token":"lorem","expires_in":42,"refresh_token":"lorem","token_type":"lorem","user":{"app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"   }  ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null  } }}

```

## Refreshes a user's refresh token.
post`/token?grant_type=refresh_token`
### Body
application/json
  * refresh_tokenOptionalstring


### Response codes
  * 200


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
{"access_token":"lorem","expires_in":42,"refresh_token":"lorem","token_type":"lorem","user":{"app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"   }  ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null  } }}

```

## Get information for the logged-in user.
get`/user`
### Response codes
  * 200
  * 401


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
{"app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"  } ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null }}

```

## Returns the updated user.
put`/user`
### Body
application/json
  * app_metadataOptionalobject
Object schema
  * dataOptionalobject
Object schema
  * emailOptionalstring
  * nonceOptionalstring
  * passwordOptionalstring
  * phoneOptionalstring


### Response codes
  * 200
  * 401


### Response (200)
exampleschema
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
{"app_metadata":{"property1":null,"property2":null},"aud":"lorem","banned_until":"2021-12-31T23:34:00Z","confirmation_sent_at":"2021-12-31T23:34:00Z","confirmed_at":"2021-12-31T23:34:00Z","created_at":"2021-12-31T23:34:00Z","email":"lorem","email_change_sent_at":"2021-12-31T23:34:00Z","email_confirmed_at":"2021-12-31T23:34:00Z","id":"fbdf5a53-161e-4460-98ad-0e39408d8689","identities": [{"created_at":"2021-12-31T23:34:00Z","id":"lorem","identity_data":{"property1":null,"property2":null},"last_sign_in_at":"2021-12-31T23:34:00Z","provider":"lorem","updated_at":"2021-12-31T23:34:00Z","user_id":"fbdf5a53-161e-4460-98ad-0e39408d8689"  } ],"invited_at":"2021-12-31T23:34:00Z","last_sign_in_at":"2021-12-31T23:34:00Z","new_email":"lorem","new_phone":"lorem","phone":"lorem","phone_change_sent_at":"2021-12-31T23:34:00Z","phone_confirmed_at":"2021-12-31T23:34:00Z","reauthentication_sent_at":"2021-12-31T23:34:00Z","recovery_sent_at":"2021-12-31T23:34:00Z","role":"lorem","updated_at":"2021-12-31T23:34:00Z","user_metadata":{"property1":null,"property2":null }}

```

## Verifies a sign up.
post`/verify`
### Body
application/json
  * emailOptionalstring
  * phoneOptionalstring
  * redirect_toOptionalstring
  * tokenOptionalstring
  * typeOptionalstring


  * Need some help?
[Contact support](https://supabase.com/support)
  * Latest product updates?
[See Changelog](https://supabase.com/changelog)
  * Something's not right?
[Check system status](https://status.supabase.com/)


[© Supabase Inc](https://supabase.com/)—[Contributing](https://github.com/supabase/supabase/blob/master/apps/docs/DEVELOPERS.md)[Author Styleguide](https://github.com/supabase/supabase/blob/master/apps/docs/CONTRIBUTING.md)[Open Source](https://supabase.com/open-source)[SupaSquad](https://supabase.com/supasquad)Privacy Settings
[GitHub](https://github.com/supabase/supabase)[Twitter](https://twitter.com/supabase)[Discord](https://discord.supabase.com/)
  1. We use cookies to collect data and improve our services. [Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)
[Learn more](https://supabase.com/privacy#8-cookies-and-similar-technologies-used-on-our-european-services)•Privacy settings
Accept Opt out Privacy settings



