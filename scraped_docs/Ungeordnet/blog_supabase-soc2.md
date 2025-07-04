---
url: https://supabase.com/blog/supabase-soc2
scraped_at: 2025-05-25T08:59:20.761169
title: Supabase is SOC2 compliant
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
# Supabase is SOC2 compliant
17 Aug 2022
•
9 minute read
[![Inian Parameshwaran avatar](https://supabase.com/_next/image?url=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F2155545%3Fv%3D4&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Inian ParameshwaranEngineering](https://twitter.com/everConfusedGuy)
[![Joel Lee avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fj0.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Joel LeeEngineering](https://github.com/j0)
![Supabase is SOC2 compliant](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2Flw5-soc2%2Fthumb.jpg&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
Update (2023-05-22): Supabase is now SOC2 Type 2 compliant. Read more about security at Supabase in our [Security Center](https://supabase.com/security).
Supabase is now SOC2 Type 1 compliant. Let’s dig into what that means, and explain the process we went through to get there. If you’re building a SaaS product, this blog post should provide a rough guide to getting your SOC2 certification.
## What is SOC2?[#](https://supabase.com/blog/supabase-soc2#what-is-soc2)
SOC2 is a compliance standard developed by the American Institute of CPAs. Yup CPAs - a bunch of accountants came up with the generally accepted compliance security standard for SaaS companies. SOC2 evaluates companies on 5 Trust Services Criteria: security, availability, processing integrity, confidentiality, and privacy. There are two types of compliance, both requiring an external audit:
  * Type 1: checks if a company is compliant at a point in time.
  * Type 2: checks if a company stays compliant during an observation window (typically 6 months to a year).


## Why did we get SOC2 certified?[#](https://supabase.com/blog/supabase-soc2#why-did-we-get-soc2-certified)
The main reason to go through a SOC2 audit is a simple one - customers expect it.
The Supabase team was spending a considerable amount of time filling out security questionnaires and fielding calls with potential customers - walking them through our security practices and how we protect customer data.
We are a database company — customers trust us with their data. We started with a SOC2 audit since one of the main things covered is our handling of sensitive customer data.
It is also much easier to become-and remain-SOC2 compliant when you institute the appropriate practices and standards as early as possible.
## Choosing a compliance monitoring tool[#](https://supabase.com/blog/supabase-soc2#choosing-a-compliance-monitoring-tool)
There are a few tools that plug into your cloud providers, task management system, identity, and HR providers and make it easy to monitor, collect and submit evidence to auditors. We evaluated [Vanta](https://www.vanta.com/), [Drata](https://drata.com/), [Secureframe](https://secureframe.com/), and [Tugboat Logic](https://tugboatlogic.com/). Our stack is pretty standard (AWS, GCP, GSuite, and Github). All the tools we evaluated were integrated with these systems.
Some of them had overly broad permissions when integrating with our vendors (read/write access to Github for example) which made them a no-go. Some came with a lightweight agent that we could use for Mobile Device Management (MDM). Other than that, the products are largely the same.
We chose Vanta, with Drata coming in a close second. Vanta supported more compliance standards (at that time) and is a fellow YC company (which sealed the deal). The gap between these tools is much closer now since all of them support the compliance standards we have our eyes on.
## Choosing an auditor[#](https://supabase.com/blog/supabase-soc2#choosing-an-auditor)
After setting up Vanta (nb: pestering devs to install a security agent on their laptop) and working through the checklist of tasks required for SOC2, we started looking around for auditors. Vanta was helpful here - they made introductions to a few auditors and we chose one who has previously worked with a lot of SaaS companies. Our auditors were also familiar with how Vanta worked which made the audit easier for us.
The engagement started with a call where we reviewed the systems which are in scope for the audit. We then set a date at which the audit takes place. The Type 1 audit verifies that we are adhering to our stated policies at this point in time.
## Off to the races[#](https://supabase.com/blog/supabase-soc2#off-to-the-races)
Once the date for the audit was set, it was a mad scramble to get everything in order.
Vanta has a lightweight, read-only agent built on top of [osquery](https://github.com/osquery/osquery) to verify if all team members have important security features enabled: hard disk encryption, screen locks, etc. It supports Mac, Windows, and Linux, although we had [some issues](https://github.com/system76/firmware-open/issues/268) with the agent running correctly in Linux. Getting hard disk encryption right is still difficult in some Linux distros. We decided to standardize on Mac and Windows to sidestep these issues. A more powerful MDM would enable us to remote wipe computers in case it is stolen, but we decided that the existing protections we had in place were sufficient to defend against this scenario.
We came up with a few important policies. For example, Access Control Policy, Data Management Policy, Asset Management Policy, etc. Vanta has templates which we used as a starting point and adapted to our requirements. Since our auditors are familiar with the Vanta templates, there wasn’t much back and forth regarding the policy language.
For employee background checks, we use [Certn](https://certn.co/). They integrate with Vanta, making it easy to check the status within the Vanta portal itself. Background checks aren’t _required_ for SOC2, but they are a factor in deciding whom we hire especially in certain roles like SRE and Finance where there is little room for error.
We submitted a ton of evidence to prove that we can stay on top of all activities in our cloud. We use [Vector](https://vector.dev/) to ship logs to [Logflare](http://logflare.com/), where they are retained at least for a year. Our [monitoring stack](https://supabase.com/blog/supabase-reports-and-metrics) consists of regional Victoria Metrics clusters and metrics are then aggregated into a centralized cluster. We also read from Cloudtrail logs and get notified in Slack when certain events like the root AWS account is logged into, a bucket is made public, an IAM policy changes, etc.
Enabling GitHub’s branch protection protects your repos from merging code without receiving a review first. This can be a challenge sometimes - at Supabase we have a few one-person teams. We had to relax our policy for some repos (POCs, internal projects) while keeping it strict for repos that handle critical systems.
Other tasks were already handled - encrypting data at rest and in transit, enforcing MFA where possible, standardizing on a password manager, and not using long-lived SSH keys (we use [AWS Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html)), etc.
We also evaluated all our vendors who had access to confidential data and now it was our turn to send them questionnaires or ask them for their SOC2 reports 😈.
## Making the SOC2 process work for you[#](https://supabase.com/blog/supabase-soc2#making-the-soc2-process-work-for-you)
We went through a lot of effort to make sure we weren’t adding processes just because it’s a requirement for SOC2. Everything had to improve our security or risk threshold in a meaningful way. This usually involves back and forth with the auditor to show how you satisfy a particular control even though you may not be doing it in exactly the way they want you to.
We used the SOC2 process to codify the security practices we were already doing informally at Supabase.
There are a few more debatable “check-the-box” activities - like the security awareness training which I couldn’t find a way around as much as I tried. Our team has a pretty good security posture and we don’t think watching a video on why reusing passwords is a bad idea helps much.
## A few surprises[#](https://supabase.com/blog/supabase-soc2#a-few-surprises)
We were surprised by the amount of manual evidence that we had to collect (umm..take screenshots) even with a tool like Vanta. There are things an automated tool like Vanta can never fully automate. For example, we had to collect evidence to show that have proper on-boarding and off-boarding checklists or demonstrate how we resolve security issues reported by our penetration tests within a certain time frame.
Since the Type 1 audit is just about providing evidence at a single point in time, there isn’t _that_ much utility in using a tool like Vanta. However, for Type 2 certification, where we need to show evidence that we have been compliant over a period of time, a monitoring tool like Vanta becomes more useful. Additionally, if you’re planning to get multiple certifications, investing in a compliance monitoring tool is valuable since there is considerable overlap between different frameworks, and you’ll only need to do the work of collecting your evidence once.
We spent some time trying to get a perfect score in Vanta before reaching out to the auditor. That turned out to be a mistake; Vanta is fairly broad in its checks, but the ones you need to pass depend on the audit’s scope, and the auditor. For example, our auditor didn’t care about seeing our exact board meeting minutes, but Vanta wanted us to document it!
Another revelation was that a lot of controls other companies had talked about in their SOC2 compliance journeys ended up not being a blocker for us. I am not going to list them here since it is dependent on the systems that are in scope, your larger architecture, and your auditor. Again, the takeaway here is to reach out to your auditor as early as possible to get a sense of what is relevant to your audit.
Auditors aren’t adversarial like pentesters or bug bounty hunters. For example, if you point them to a PR and say that PR closes a security issue reported, they _trust_ that it did. They aren’t going to find a way to bypass the fix you implemented and use that to raise an exception in your audit. This is why getting SOC2 certified is just a small part of staying secure - what makes your auditor happy will likely be pretty different from what makes a penetration tester happy.
## Security Center[#](https://supabase.com/blog/supabase-soc2#security-center)
Today we are launching our [security center](https://supabase.com/security), which shows the steps we take to protect your data. You can also find our audit reports at our security portal [here](https://security.supabase.com), or reach out to growth@supabase.com
## What’s next[#](https://supabase.com/blog/supabase-soc2#whats-next)
Getting the SOC2 certification is just the start, and we will be working on getting certified for HIPAA next. If you are interested in discussing these, we would love to chat. We will also be rolling out a series of security improvements to all projects hosted on the Supabase Cloud offering over the coming months. Stay tuned!
## Announcement video and discussion[#](https://supabase.com/blog/supabase-soc2#announcement-video-and-discussion)
## More Launch Week 5[#](https://supabase.com/blog/supabase-soc2#more-launch-week-5)
  * [Launch Week Page](https://supabase.com/launch-week)
  * [Launch Week 5 Hackathon](https://supabase.com/blog/launch-week-5-hackathon)
  * [Day 1 - Supabase CLI v1 and Management API Beta](https://supabase.com/blog/supabase-cli-v1-and-admin-api-beta)
  * [Youtube video - Supabase CLI v1 and Management API Beta](https://www.youtube.com/watch?v=OpPOaJI_Z28&feature=emb_title)
  * [Day 2 - supabase-js v2 Release Candidate](https://supabase.com/blog/supabase-js-v2)
  * [Youtube Video - supabase-js v2 Release Candidate](https://www.youtube.com/watch?v=iqZlPtl_b-I)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2&text=Supabase%20is%20SOC2%20compliant)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2&text=Supabase%20is%20SOC2%20compliant)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2&t=Supabase%20is%20SOC2%20compliant)
[Last postRealtime: Multiplayer Edition18 August 2022](https://supabase.com/blog/supabase-realtime-multiplayer-general-availability)
[Next postsupabase-js v216 August 2022](https://supabase.com/blog/supabase-js-v2)
[launch-week](https://supabase.com/blog/tags/launch-week)
On this page
  * [What is SOC2?](https://supabase.com/blog/supabase-soc2#what-is-soc2)
  * [Why did we get SOC2 certified?](https://supabase.com/blog/supabase-soc2#why-did-we-get-soc2-certified)
  * [Choosing a compliance monitoring tool](https://supabase.com/blog/supabase-soc2#choosing-a-compliance-monitoring-tool)
  * [Choosing an auditor](https://supabase.com/blog/supabase-soc2#choosing-an-auditor)
  * [Off to the races](https://supabase.com/blog/supabase-soc2#off-to-the-races)
  * [Making the SOC2 process work for you](https://supabase.com/blog/supabase-soc2#making-the-soc2-process-work-for-you)
  * [A few surprises](https://supabase.com/blog/supabase-soc2#a-few-surprises)
  * [Security Center](https://supabase.com/blog/supabase-soc2#security-center)
  * [What’s next](https://supabase.com/blog/supabase-soc2#whats-next)
  * [Announcement video and discussion](https://supabase.com/blog/supabase-soc2#announcement-video-and-discussion)
  * [More Launch Week 5](https://supabase.com/blog/supabase-soc2#more-launch-week-5)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2&text=Supabase%20is%20SOC2%20compliant)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2&text=Supabase%20is%20SOC2%20compliant)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fsupabase-soc2&t=Supabase%20is%20SOC2%20compliant)
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

