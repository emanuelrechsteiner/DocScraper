---
url: https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive
scraped_at: 2025-05-25T09:01:28.284015
title: Sync Google Drive Files | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive)
    * [LLM Apps](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive)
      * [OpenAI GPTs](https://docs.runbear.io/integrations/apps/openai-gpts/)
      * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
        * [Knowledge Bases](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive)
          * [Google Drive](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive)
          * [Confluence](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence)
          * [Slack](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/slack)
        * [Web Browsing](https://docs.runbear.io/integrations/apps/openai-assistants/web-browsing)
        * [OpenAPI Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling-openapi)
        * [API Function Calling](https://docs.runbear.io/integrations/apps/openai-assistants/api-calling)
        * [Current Date Fetching](https://docs.runbear.io/integrations/apps/openai-assistants/current-date-fetching)
        * [Zapier AI Actions](https://docs.runbear.io/integrations/apps/openai-assistants/zapier-ai-actions)
      * [LangChain](https://docs.runbear.io/integrations/apps/langchain/)
      * [Python Application](https://docs.runbear.io/integrations/apps/python-sdk/)
      * [Anthropic Claude](https://docs.runbear.io/integrations/apps/anthropic-claude/)
  * [FAQs](https://docs.runbear.io/faq)


  * [](https://docs.runbear.io/)
  * [Integrations](https://docs.runbear.io/integrations)
  * LLM Apps
  * [OpenAI Assistants](https://docs.runbear.io/integrations/apps/openai-assistants/)
  * Knowledge Bases
  * Google Drive


On this page
# Sync Google Drive Files
warning
Google Drive File Sync is still in its early stages and may not work as expected. Please reach out to us if you encounter any issues.
The Google Drive File Sync for OpenAI Assistants on Runbear streamlines the process of keeping your assistant's knowledge base current by directly synchronizing with files stored in Google Drive. This functionality is integral for organizations relying on up-to-date information to inform their AI-driven interactions. It eliminates the need for manual data updates—previously a time-consuming task involving exporting and uploading files after every change.
## How it Works[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#how-it-works "Direct link to How it Works")
Runbear leverages the Google Drive API to access and sync files stored in your Google Drive account. We periodically check for updates of the files you've selected to sync with your assistant. When changes are detected, we automatically update the assistant's vector store with the updated information.
## Setting Up Google Drive File Sync[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#setting-up-google-drive-file-sync "Direct link to Setting Up Google Drive File Sync")
Service Accounts are used to authenticate and authorize access to Google Drive files. Here's how you can set up Google Drive File Sync for your OpenAI Assistant on Runbear:
### Create a Service Account[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#create-a-service-account "Direct link to Create a Service Account")
  1. Go to the [Google Cloud Console](https://console.cloud.google.com/), and create a new project or select an existing one.
  2. Navigate to the [Credentials](https://console.cloud.google.com/apis/credentials) page under the APIs & Services section
  3. Click on the "Create Credentials" button and select "Service Account" from the dropdown.
  4. Give your service account a name, grant it the "Project > Viewer" role, and click "Create".
  5. Click on the newly created service account and navigate to the "Keys" tab.
  6. Click on "Add Key" and select "JSON" to download the JSON key file. Keep this file secure as it contains sensitive information.


### Enable Google Drive API[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#enable-google-drive-api "Direct link to Enable Google Drive API")
  1. Navigate to the [Google API Library](https://console.cloud.google.com/apis/library) and search for "Google Drive API".
  2. Click on the "Enable" button to enable the API for your project.


### Share Google Drive Files[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#share-google-drive-files "Direct link to Share Google Drive Files")
note
Shared Drive files are not supported yet. Only files stored in your personal Google Drive account can be synced.
  1. Share the Google Drive files you want to sync with your assistant with the service account email address found in the JSON key file.
  2. The service account will now have access to the shared files and can sync them with your assistant.


### Configure Google Drive File Sync[​](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#configure-google-drive-file-sync "Direct link to Configure Google Drive File Sync")
  1. In edit page of your LLM App in Runbear, click "Add from Google Drive" under the "File Search" section. ![Add from Google Drive](https://docs.runbear.io/assets/images/google-drive-sync-button-9387e09f59fb1a2ff95a58940966ee6a.png)
  2. Upload the JSON key file you downloaded earlier.
  3. Select the Google Drive files you want to sync with your assistant click "Add Files". ![Select Files](https://docs.runbear.io/assets/images/google-drive-sync-files-87e460cea5a5ccedf9de828d1a5b612f.png)


Runbear will then upload the selected files to your assistant and periodically check for updates to keep the assistant's knowledge base current. Let us know if your files are not syncing after 1 hour.
[PreviousIntroduction](https://docs.runbear.io/integrations/apps/openai-assistants/)[NextConfluence](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/confluence)
  * [How it Works](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#how-it-works)
  * [Setting Up Google Drive File Sync](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#setting-up-google-drive-file-sync)
    * [Create a Service Account](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#create-a-service-account)
    * [Enable Google Drive API](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#enable-google-drive-api)
    * [Share Google Drive Files](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#share-google-drive-files)
    * [Configure Google Drive File Sync](https://docs.runbear.io/integrations/apps/openai-assistants/knowledge-bases/google-drive#configure-google-drive-file-sync)


Docs
  * [Docs](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)


Community
  * [Twitter](https://twitter.com/runbear_io)
  * [LinkedIn](https://www.linkedin.com/company/runbear)


More
  * [Runbear](https://runbear.io)
  * [GitHub](https://github.com/runbear-io/plugbear-python-sdk)


Copyright © 2025 Runbear, Inc.

