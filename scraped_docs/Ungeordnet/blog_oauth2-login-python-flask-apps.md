---
url: https://supabase.com/blog/oauth2-login-python-flask-apps
scraped_at: 2025-05-25T09:11:28.026705
title: GitHub OAuth in your Python Flask app
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
# GitHub OAuth in your Python Flask app
21 Nov 2023
•
5 minute read
[![Andrew Smith avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fsilentworks.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Andrew SmithDevRel & DX](https://github.com/silentworks)
![GitHub OAuth in your Python Flask app](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Foauth2-login-python-flask-apps%2Fflask-supabase-auth.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
In this guide we'll learn how to quickly build an OAuth2.0 integration into a simple Flask app using Supabase-py. This will enable your users to login to your web app using their GitHub account.
## Prerequisites[#](https://supabase.com/blog/oauth2-login-python-flask-apps#prerequisites)
This article assumes you are familiar with creating an application in Flask. It also assumes that you have read the Supabase documentation and are familiar the with concept of [Authentication](https://supabase.com/docs/guides/auth).
We'll use the following tools:
  * [Flask](https://flask.palletsprojects.com/en/3.0.x/) - we used version 2.3.3 for this article
  * Supabase Dashboard - [create an account](https://database.new/) if you don't have one already


## Getting started[#](https://supabase.com/blog/oauth2-login-python-flask-apps#getting-started)
To begin, inside your Flask application install the `supabase` library using the following command in the terminal:
`
1
pip install supabase
`
## Session storage[#](https://supabase.com/blog/oauth2-login-python-flask-apps#session-storage)
Open the project in your preferred code editor and create a file called `flask_storage.py` with the following content:
`
1
from gotrue import SyncSupportedStorage
2
from flask import session
34
class FlaskSessionStorage(SyncSupportedStorage):
5
  def __init__(self):
6
    self.storage = session
78
  def get_item(self, key: str) -> str | None:
9
    if key in self.storage:
10
      return self.storage[key]
1112
  def set_item(self, key: str, value: str) -> None:
13
    self.storage[key] = value
1415
  def remove_item(self, key: str) -> None:
16
    if key in self.storage:
17
      self.storage.pop(key, None)
`
In this file, we're extending the `SyncSupportedStorage` class from the `gotrue` library which comes bundled with the `supabase` library. Here we're telling the Supabase authentication library (`gotrue`) how to retrieve, store and remove a session that will store our JSON Web Token (JWT).
## Initiate the client[#](https://supabase.com/blog/oauth2-login-python-flask-apps#initiate-the-client)
Create another file called `supabase_client.py` and in this file, we'll initiate our Supabase client.
`
1
import os
2
from flask import g
3
from werkzeug.local import LocalProxy
4
from supabase.client import Client, ClientOptions
5
from flask_storage import FlaskSessionStorage
67
url = os.environ.get("SUPABASE_URL", "")
8
key = os.environ.get("SUPABASE_KEY", "")
910
def get_supabase() -> Client:
11
  if "supabase" not in g:
12
    g.supabase = Client(
13
      url,
14
      key,
15
      options=ClientOptions(
16
        storage=FlaskSessionStorage(),
17
        flow_type="pkce"
18
      ),
19
    )
20
  return g.supabase
2122
supabase: Client = LocalProxy(get_supabase)
`
Let's focus on the `get_supabase` function. Here we are checking if we have an instance of the client stored in our global object `g`, if not we create the client and store it in the global object under the `supabase` name. You will notice in the `ClientOptions` that we are specifying the `FlaskSessionStorage` class we created earlier and we are also specifying a very important option that allows us to handle the OAuth flow on the server side, the `flow_type="pkce"`.
## Sign in with GitHub[#](https://supabase.com/blog/oauth2-login-python-flask-apps#sign-in-with-github)
Supabase Auth supports Sign in with GitHub on the web, native Android applications, and Chrome extensions.
For detailed set up and implementation instructions please refer to the [docs](https://supabase.com/docs/guides/auth/social-login/auth-github).
## Create sign-in route[#](https://supabase.com/blog/oauth2-login-python-flask-apps#create-sign-in-route)
Inside our application code `app.py`, we can create the sign-in route to trigger the OAuth sign-in request.
`
1
@app.route("/signin/github")
2
def signin_with_github():
3
  res = supabase.auth.sign_in_with_oauth(
4
    {
5
      "provider": "github",
6
      "options": {
7
	      "redirect_to": f"{request.host_url}callback"
8
	    },
9
    }
10
  )
11
  return redirect(res.url)
`
In this function `options` object we specify a `redirect_to` parameter which will point to the callback route we will create in the next step. This function will generate a url for us to use to redirect the user to, in this case we are using `github` as our OAuth provider so we will be redirected to the GitHub OAuth consent screen.
## Create callback route[#](https://supabase.com/blog/oauth2-login-python-flask-apps#create-callback-route)
Let's add another route to our `app.py` file for the callback endpoint we specified in our sign in route.
`
1
@app.route("/callback")
2
def callback():
3
  code = request.args.get("code")
4
  next = request.args.get("next", "/")
56
  if code:
7
    res = supabase.auth.exchange_code_for_session({"auth_code": code})
89
  return redirect(next)
`
Here we're getting the `code` query parameter from the request object, if this is available we then exchange the code for a session so that the user will be signed in. Under the hood the `supabase` python library will handle storing this session (JWT) into a cookie and sign the user in.
## Conclusion[#](https://supabase.com/blog/oauth2-login-python-flask-apps#conclusion)
In this post we explained how to setup a flask session storage to work with the Supabase python library, setting the `flow_type` to use Proof Key for Code Exchange (PKCE) and creating a sign in and a callback route to handle the user authentication.
## More Resources[#](https://supabase.com/blog/oauth2-login-python-flask-apps#more-resources)
  * [supabase-py reference docs](https://supabase.com/docs/reference/python/installing)
  * [supabase-py GitHub repo](https://github.com/supabase-community/supabase-py)
  * [Deep Dive series on auth concepts in Supabase](https://supabase.com/docs/learn/auth-deep-dive/auth-deep-dive-jwts)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&text=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&text=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&t=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)
[Last postAutomatic CLI login1 December 2023](https://supabase.com/blog/automatic-cli-login)
[Next postGetting started with React Native authentication16 November 2023](https://supabase.com/blog/react-native-authentication)
[python](https://supabase.com/blog/tags/python)[auth](https://supabase.com/blog/tags/auth)
On this page
  * [Prerequisites](https://supabase.com/blog/oauth2-login-python-flask-apps#prerequisites)
  * [Getting started](https://supabase.com/blog/oauth2-login-python-flask-apps#getting-started)
  * [Session storage](https://supabase.com/blog/oauth2-login-python-flask-apps#session-storage)
  * [Initiate the client](https://supabase.com/blog/oauth2-login-python-flask-apps#initiate-the-client)
  * [Sign in with GitHub](https://supabase.com/blog/oauth2-login-python-flask-apps#sign-in-with-github)
  * [Create sign-in route](https://supabase.com/blog/oauth2-login-python-flask-apps#create-sign-in-route)
  * [Create callback route](https://supabase.com/blog/oauth2-login-python-flask-apps#create-callback-route)
  * [Conclusion](https://supabase.com/blog/oauth2-login-python-flask-apps#conclusion)
  * [More Resources](https://supabase.com/blog/oauth2-login-python-flask-apps#more-resources)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&text=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&text=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Foauth2-login-python-flask-apps&t=GitHub%20OAuth%20in%20your%20Python%20Flask%20app)
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

