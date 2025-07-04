---
url: https://docs.runbear.io/integrations/channels/slack/
scraped_at: 2025-05-25T08:57:34.756167
title: Integration Guide for Slack | Runbear
---

[Skip to main content](https://docs.runbear.io/integrations/channels/slack/#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Introduction](https://docs.runbear.io/)
  * [Get Started](https://docs.runbear.io/get-started)
    * [Step 1 - Adding LLM Apps](https://docs.runbear.io/get-started/app)
    * [Step 2 - Adding Channels](https://docs.runbear.io/get-started/channel)
    * [Step 3 - Connecting Channels with LLM Apps](https://docs.runbear.io/get-started/connection)
  * [Integrations](https://docs.runbear.io/integrations)
    * [Channels](https://docs.runbear.io/integrations/channels/slack/)
      * [Slack](https://docs.runbear.io/integrations/channels/slack/)
        * [How to Change the Slack Bot Icon](https://docs.runbear.io/integrations/channels/slack/how-to-change-slack-bot-icon)
        * [Display AI Apps in Slack](https://docs.runbear.io/integrations/channels/slack/how-to-enable-slack-ai-agent)
      * [HubSpot](https://docs.runbear.io/integrations/channels/hubspot/)
      * [Teams](https://docs.runbear.io/integrations/channels/teams/)
    * [LLM Apps](https://docs.runbear.io/integrations/channels/slack/)
  * [FAQs](https://docs.runbear.io/faq)


  * [](https://docs.runbear.io/)
  * [Integrations](https://docs.runbear.io/integrations)
  * Channels
  * Slack


On this page
# Integration Guide for Slack
Runbear is a no/low-code solution for connecting communication channels with LLM (Large Language Model) applications. For example, it enables the creation of a bot for Slack from an LLM app in just a few clicks.
## How does it works?[​](https://docs.runbear.io/integrations/channels/slack/#how-does-it-works "Direct link to How does it works?")
Runbear forwards the message from Slack to LLM apps and then relays the generated answers back to the thread.
Slack
Runbear
LLM Apps
When a trigger event, such as a bot mention, occurs in the connected Slack channels, Runbear receives this event. It then transforms the messages to be suitable for LLM applications and initiates generation. Once the apps complete the generation, Runbear transforms the results to be compatible with Slack.
![bot-mention](https://docs.runbear.io/img/slack-trigger-bot-mention.png)
## Integration Walkthrough[​](https://docs.runbear.io/integrations/channels/slack/#integration-walkthrough "Direct link to Integration Walkthrough")
### Initial Configuration[​](https://docs.runbear.io/integrations/channels/slack/#initial-configuration "Direct link to Initial Configuration")
  1. Navigate to channels. Click the `Connect` button of the Slack tile.


![image](https://docs.runbear.io/assets/images/plugbear-activate-channel-ca174f23aec60f2aa0cfaf29070f99da.png)
  1. On the new channel page, click `Add Runbear to Slack` to install the Runbear bot on Slack.
  2. After installation, please make sure the correct workspace is selected and click the Add button to activate your workspace on Runbear.
  3. To support the LLM apps, the bot needs to be able to join the channel.
  4. To connect your LLM apps, follow the instructions provided [here](https://docs.runbear.io/get-started/connection).
  5. After connecting the LLM app to Slack, you can send a message with `@Runbear` to get the LLM app's response to your query.


### Disconnect Workspace[​](https://docs.runbear.io/integrations/channels/slack/#disconnect-workspace "Direct link to Disconnect Workspace")
Navigate to channels. Click on the more options of the Slack tile and select `Deactivate`.
note
Disclaimer: While our app delivers responses from a user-built LLM app, any inaccuracies in the responses are not the responsibility of our service. Users are encouraged to independently verify essential information and acknowledge that inaccuracies may arise from the nature of their customized model.
[PreviousIntegrations](https://docs.runbear.io/integrations)[NextHow to Change the Slack Bot Icon](https://docs.runbear.io/integrations/channels/slack/how-to-change-slack-bot-icon)
  * [How does it works?](https://docs.runbear.io/integrations/channels/slack/#how-does-it-works)
  * [Integration Walkthrough](https://docs.runbear.io/integrations/channels/slack/#integration-walkthrough)
    * [Initial Configuration](https://docs.runbear.io/integrations/channels/slack/#initial-configuration)
    * [Disconnect Workspace](https://docs.runbear.io/integrations/channels/slack/#disconnect-workspace)


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

