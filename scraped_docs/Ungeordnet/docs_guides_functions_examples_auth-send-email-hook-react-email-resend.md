---
url: https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend
scraped_at: 2025-05-25T08:41:20.760615
title: Custom Auth Emails with React Email and Resend | Supabase Docs
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
[Edge Functions](https://supabase.com/docs/guides/functions)
  * [Overview](https://supabase.com/docs/guides/functions)
Getting started
  * [Quickstart](https://supabase.com/docs/guides/functions/quickstart)
  * [Create an Edge Function Locally](https://supabase.com/docs/guides/functions/local-quickstart)
  * [Deploy to Production](https://supabase.com/docs/guides/functions/deploy)
  * [Setting up your editor](https://supabase.com/docs/guides/functions/local-development)
  * [Development tips](https://supabase.com/docs/guides/functions/development-tips)
Guides
  * [Managing dependencies](https://supabase.com/docs/guides/functions/dependencies)
  * [Managing environment variables](https://supabase.com/docs/guides/functions/secrets)
  * [Integrating with Supabase Auth](https://supabase.com/docs/guides/functions/auth)
  * [Integrating with Postgres](https://supabase.com/docs/guides/functions/connect-to-postgres)
  * [Integrating with Supabase Storage](https://supabase.com/docs/guides/functions/storage-caching)
  * [Handling Routing in Functions](https://supabase.com/docs/guides/functions/routing)
  * [Background Tasks](https://supabase.com/docs/guides/functions/background-tasks)
  * [Ephemeral Storage](https://supabase.com/docs/guides/functions/ephemeral-storage)
  * [WebSockets](https://supabase.com/docs/guides/functions/websockets)
  * [Running AI Models](https://supabase.com/docs/guides/functions/ai-models)
  * [Wasm modules](https://supabase.com/docs/guides/functions/wasm)
  * [Deploying with CI / CD pipelines](https://supabase.com/docs/guides/functions/cicd-workflow)
  * [Integrating with Log Drains](https://supabase.com/docs/guides/platform/log-drains)
  * [Using Deno 2](https://supabase.com/docs/guides/functions/deno2)
Debugging
  * [Local Debugging with DevTools](https://supabase.com/docs/guides/functions/debugging-tools)
  * [Logging](https://supabase.com/docs/guides/functions/logging)
  * [Troubleshooting Common Issues](https://supabase.com/docs/guides/functions/troubleshooting)
  * [Testing your Edge Functions](https://supabase.com/docs/guides/functions/unit-test)
  * [Monitoring with Sentry](https://supabase.com/docs/guides/functions/examples/sentry-monitoring)
Platform
  * [Regional invocations](https://supabase.com/docs/guides/functions/regional-invocation)
  * [Status codes](https://supabase.com/docs/guides/functions/status-codes)
  * [Limits](https://supabase.com/docs/guides/functions/limits)
  * [Pricing](https://supabase.com/docs/guides/functions/pricing)
Examples
  * [Auth Send Email Hook](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend)
  * [CORS support for invoking from the browser](https://supabase.com/docs/guides/functions/cors)
  * [Scheduling Functions](https://supabase.com/docs/guides/functions/schedule-functions)
  * [Sending Push Notifications](https://supabase.com/docs/guides/functions/examples/push-notifications)
  * [Generating AI images](https://supabase.com/docs/guides/functions/examples/amazon-bedrock-image-generator)
  * [Generating OG images ](https://supabase.com/docs/guides/functions/examples/og-image)
  * [Semantic AI Search](https://supabase.com/docs/guides/functions/examples/semantic-search)
  * [CAPTCHA support with Cloudflare Turnstile](https://supabase.com/docs/guides/functions/examples/cloudflare-turnstile)
  * [Building a Discord Bot](https://supabase.com/docs/guides/functions/examples/discord-bot)
  * [Building a Telegram Bot](https://supabase.com/docs/guides/functions/examples/telegram-bot)
  * [Handling Stripe Webhooks ](https://supabase.com/docs/guides/functions/examples/stripe-webhooks)
  * [Rate-limiting with Redis](https://supabase.com/docs/guides/functions/examples/rate-limiting)
  * [Taking Screenshots with Puppeteer](https://supabase.com/docs/guides/functions/examples/screenshots)
  * [Slack Bot responding to mentions](https://supabase.com/docs/guides/functions/examples/slack-bot-mention)
  * [Image Transformation & Optimization](https://supabase.com/docs/guides/functions/examples/image-manipulation)
Third-Party Tools
  * [Dart Edge on Supabase](https://supabase.com/docs/guides/functions/dart-edge)
  * [Browserless.io](https://supabase.com/docs/guides/functions/examples/screenshots)
  * [Hugging Face](https://supabase.com/docs/guides/ai/examples/huggingface-image-captioning)
  * [Monitoring with Sentry](https://supabase.com/docs/guides/functions/examples/sentry-monitoring)
  * [OpenAI API](https://supabase.com/docs/guides/ai/examples/openai)
  * [React Email](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend)
  * [Sending Emails with Resend](https://supabase.com/docs/guides/functions/examples/send-emails)
  * [Upstash Redis](https://supabase.com/docs/guides/functions/examples/upstash-redis)
  * [Type-Safe SQL with Kysely](https://supabase.com/docs/guides/functions/kysely-postgres)
  * [Text To Speech with ElevenLabs](https://supabase.com/docs/guides/functions/examples/elevenlabs-generate-speech-stream)
  * [Speech Transcription with ElevenLabs](https://supabase.com/docs/guides/functions/examples/elevenlabs-transcribe-speech)


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
Edge Functions
  1. [Edge Functions](https://supabase.com/docs/guides/functions)
  2. Examples
  3. [Auth Send Email Hook](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend)


Custom Auth Emails with React Email and Resend
Use the [send email hook](https://supabase.com/docs/guides/auth/auth-hooks/send-email-hook?queryGroups=language&language=http) to send custom auth emails with [React Email](https://react.email/) and [Resend](https://resend.com/) in Supabase Edge Functions.
Prefer to jump straight to the code? [Check out the example on GitHub](https://github.com/supabase/supabase/tree/master/examples/edge-functions/supabase/functions/auth-hook-react-email-resend).
### Prerequisites[#](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#prerequisites)
To get the most out of this guide, you’ll need to:
  * [Create a Resend API key](https://resend.com/api-keys)
  * [Verify your domain](https://resend.com/domains)


Make sure you have the latest version of the [Supabase CLI](https://supabase.com/docs/guides/cli#installation) installed.
### 1. Create Supabase function[#](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#1-create-supabase-function)
Create a new function locally:
```

1
supabasefunctionsnewsend-email

```

### 2. Edit the handler function[#](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#2-edit-the-handler-function)
Paste the following code into the `index.ts` file:
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
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
importReactfrom'npm:react@18.3.1'import{Webhook}from'https://esm.sh/standardwebhooks@1.0.0'import{Resend}from'npm:resend@4.0.0'import{renderAsync}from'npm:@react-email/components@0.0.22'import{MagicLinkEmail}from'./_templates/magic-link.tsx'constresend=newResend(Deno.env.get('RESEND_API_KEY')asstring)consthookSecret=Deno.env.get('SEND_EMAIL_HOOK_SECRET')asstringDeno.serve(async(req)=>{if (req.method!=='POST') {returnnewResponse('not allowed',{status:400})}constpayload=awaitreq.text()constheaders=Object.fromEntries(req.headers)constwh=newWebhook(hookSecret)try{const{user,email_data:{token,token_hash,redirect_to,email_action_type},}=wh.verify(payload,headers)as{user:{email:string}email_data:{token:stringtoken_hash:stringredirect_to:stringemail_action_type:stringsite_url:stringtoken_new:stringtoken_hash_new:string}}consthtml=awaitrenderAsync(React.createElement(MagicLinkEmail,{supabase_url:Deno.env.get('SUPABASE_URL')??'',token,token_hash,redirect_to,email_action_type,}))const{error}=awaitresend.emails.send({from:'welcome <onboarding@resend.dev>',to:[user.email],subject:'Supa Custom MagicLink!',html,})if (error) {throwerror}}catch (error) {console.log(error)returnnewResponse(JSON.stringify({error:{http_code:error.code,message:error.message,},}),{status:401,headers:{'Content-Type':'application/json'},}  )}constresponseHeaders=newHeaders()responseHeaders.set('Content-Type','application/json')returnnewResponse(JSON.stringify({}),{status:200,headers:responseHeaders,})})

```

### 3. Create React Email templates[#](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#3-create-react-email-templates)
Create a new folder `_templates` and create a new file `magic-link.tsx` with the following code:
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
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
import{Body,Container,Head,Heading,Html,Link,Preview,Text,}from'npm:@react-email/components@0.0.22'import*asReactfrom'npm:react@18.3.1'interfaceMagicLinkEmailProps{supabase_url:stringemail_action_type:stringredirect_to:stringtoken_hash:stringtoken:string}exportconstMagicLinkEmail=({token,supabase_url,email_action_type,redirect_to,token_hash,}:MagicLinkEmailProps)=>(<Html><Head /><Preview>Log in with this magic link</Preview><Body style={main}><Container style={container}><Heading style={h1}>Login</Heading><Linkhref={`${supabase_url}/auth/v1/verify?token=${token_hash}&type=${email_action_type}&redirect_to=${redirect_to}`}target="_blank"style={{...link,display:'block',marginBottom:'16px',}}>     Click here to log in with this magic link</Link><Text style={{...text,marginBottom:'14px'}}>     Or, copy and paste this temporary login code:</Text><code style={code}>{token}</code><Textstyle={{...text,color:'#ababab',marginTop:'14px',marginBottom:'16px',}}>     If you didn&apos;t try to login, you can safely ignore this email.</Text><Text style={footer}><Linkhref="https://demo.vercel.store/"target="_blank"style={{...link,color:'#898989'}}>      ACME Corp</Link>     , the famouse demo corp.</Text></Container></Body></Html>)exportdefaultMagicLinkEmailconstmain={backgroundColor:'#ffffff',}constcontainer={paddingLeft:'12px',paddingRight:'12px',margin:'0 auto',}consth1={color:'#333',fontFamily:"-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",fontSize:'24px',fontWeight:'bold',margin:'40px 0',padding:'0',}constlink={color:'#2754C5',fontFamily:"-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",fontSize:'14px',textDecoration:'underline',}consttext={color:'#333',fontFamily:"-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",fontSize:'14px',margin:'24px 0',}constfooter={color:'#898989',fontFamily:"-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif",fontSize:'12px',lineHeight:'22px',marginTop:'12px',marginBottom:'24px',}constcode={display:'inline-block',padding:'16px 4.5%',width:'90.5%',backgroundColor:'#f4f4f4',borderRadius:'5px',border:'1px solid #eee',color:'#333',}

```

You can find a selection of React Email templates in the [React Email Examples](https://react.email/examples).
### 4. Deploy the Function[#](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#4-deploy-the-function)
Deploy function to Supabase:
```

1
supabasefunctionsdeploysend-email--no-verify-jwt

```

Note down the function URL, you will need it in the next step!
### 5. Configure the Send Email Hook[#](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#5-configure-the-send-email-hook)
  * Go to the [Auth Hooks](https://supabase.com/dashboard/project/_/auth/hooks) section of the Supabase dashboard and create a new "Send Email hook".
  * Select HTTPS as the hook type.
  * Paste the function URL in the "URL" field.
  * Click "Generate Secret" to generate your webhook secret and note it down.
  * Click "Create" to save the hook configuration.


Store these secrets in your `.env` file.
```

1
2
RESEND_API_KEY=your_resend_api_keySEND_EMAIL_HOOK_SECRET=<base64_secret>

```

You can generate the secret in the [Auth Hooks](https://supabase.com/dashboard/project/_/auth/hooks) section of the Supabase dashboard. Make sure to remove the `v1,whsec_` prefix!
Set the secrets from the `.env` file:
```

1
supabasesecretsset--env-filesupabase/functions/.env

```

Now your Supabase Edge Function will be triggered anytime an Auth Email needs to be send to the user!
## More resources[#](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#more-resources)
  * [Send Email Hooks](https://supabase.com/docs/guides/auth/auth-hooks/send-email-hook)
  * [Auth Hooks](https://supabase.com/docs/guides/auth/auth-hooks)

[Edit this page on GitHub ](https://github.com/supabase/supabase/blob/master/apps/docs/content/guides/functions/examples/auth-send-email-hook-react-email-resend.mdx)
Watch video guide
![Video guide preview](https://supabase.com/docs/_next/image?url=https%3A%2F%2Fimg.youtube.com%2Fvi%2FtlA7BomSCgU%2F0.jpg&w=3840&q=75)
### Is this helpful?
No Yes
### On this page
[Prerequisites](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#prerequisites)[1. Create Supabase function](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#1-create-supabase-function)[2. Edit the handler function](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#2-edit-the-handler-function)[3. Create React Email templates](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#3-create-react-email-templates)[4. Deploy the Function](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#4-deploy-the-function)[5. Configure the Send Email Hook](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#5-configure-the-send-email-hook)[More resources](https://supabase.com/docs/guides/functions/examples/auth-send-email-hook-react-email-resend#more-resources)
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



