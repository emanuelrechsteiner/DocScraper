---
url: https://supabase.com/blog/exploring-support-tooling
scraped_at: 2025-05-25T09:29:01.936791
title: Exploring Support Tooling at Supabase: A Dive into SLA Buddy
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
# Exploring Support Tooling at Supabase: A Dive into SLA Buddy
25 Apr 2024
•
15 minute read
[![Rodrigo Mansueli avatar](https://supabase.com/_next/image?url=https%3A%2F%2Fgithub.com%2Fmansueli.png&w=96&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)Rodrigo MansueliSupport Engineer](https://github.com/mansueli)
![Exploring Support Tooling at Supabase: A Dive into SLA Buddy](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-04-25-exploring-support-tooling%2Fslabuddy-og.png&w=3840&q=100&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
## Introduction[#](https://supabase.com/blog/exploring-support-tooling#introduction)
In database management and support operations, ensuring Service Level Agreement (SLA) compliance is paramount. Supabase, known for its innovative approach to database management and support, introduces SLA Buddy, a robust support tool aimed at efficient SLA enforcement. This blog post delves into the intricacies of SLA Buddy, shedding light on its functions, operations, and interactions within the Supabase ecosystem.
### Introducing SLA Buddy[#](https://supabase.com/blog/exploring-support-tooling#introducing-sla-buddy)
Supabase's commitment to innovation extends beyond database solutions; it encompasses robust support operations. SLA Buddy stands as a testament to Supabase's dedication to streamlining support processes and ensuring timely resolution of user queries.
## Dogfooding: The Birth of SLA Buddy[#](https://supabase.com/blog/exploring-support-tooling#dogfooding-the-birth-of-sla-buddy)
Supabase firmly believes in dogfooding a philosophy that entails using one's own products internally. This approach played a pivotal role in the creation of SLA Buddy. Leveraging Supabase's suite of tools, including Edge Functions and Database functionalities, SLA Buddy was meticulously developed to meet the stringent demands of support operations.
## Understanding SLA Buddy's Functions[#](https://supabase.com/blog/exploring-support-tooling#understanding-sla-buddys-functions)
SLA Buddy's core function revolves around enforcing SLAs effectively. Let's delve into its primary functions:
### SLA Enforcement[#](https://supabase.com/blog/exploring-support-tooling#sla-enforcement)
SLA Buddy ensures SLA compliance through a series of intricate processes. This includes:
  * **Slack Reminders** : Utilizing Slack reminders to prompt support engineers about impending SLA deadlines.
  * **Calendar Checks** : Employing calendar integration to determine who's currently available to answer support tickets.


## Let's take a look at SLA Buddy's Operations[#](https://supabase.com/blog/exploring-support-tooling#lets-take-a-look-at-sla-buddys-operations)
To gain a deeper understanding of SLA Buddy's operations, let's take a look on the main diagram of operations: ![SLA Buddy Operations](https://supabase.com/_next/image?url=%2Fimages%2Fblog%2F2024-04-25-exploring-support-tooling%2Fslabuddy_diagram.svg&w=3840&q=75&dpl=dpl_9xPTPeSUKoDuygMmT5sPj6DB4mgG)
### Watching Messages[#](https://supabase.com/blog/exploring-support-tooling#watching-messages)
SLA Buddy actively monitors Slack channels using PostgreSQL functions like **`process_channels`**. This function scans Slack channels, handles new messages, and adds tasks to the queue for each new ticket that comes to the platform. Once the channel is scanned through the scan_channel edge function it adds rows to the`slack_watcher` table. There is a trigger function on that table that creates tasks for each ticket according to the SLA which depends on which channel that the message came from. Tickets have different SLAs, depending on both severity and the subscription level of the user opening the ticket.
`
1
CREATE OR REPLACE FUNCTION "public"."insert_tasks"() RETURNS "trigger"
2
  LANGUAGE "plpgsql"
3
  AS $$
4
declare
5
  escalationtimeintervals int[];
6
  currentinterval int;
7
  threadts text;
89
BEGIN
10
  IF new.channel_id <> '' THEN
11
    SELECT escalation_time INTO escalationtimeintervals
12
     FROM priority WHERE channel_id = new.channel_id;
13
  ELSE
14
    escalationtimeintervals := array[10, 20, 35, 50]; -- minutes
15
  END IF;
16
  -- INSERT tasks for each escalation level
17
  FOR i IN 1..4
18
  LOOP
19
    -- set the current escalation time interval
20
    currentinterval := escalationtimeintervals[i];
21
    -- format thread_ts as (epoch time as a big int) + '.' + ts_ms
22
    thread_timestamp := extract(epoch FROM new.ts)::bigint::text || '.' || new.ts_ms;
2324
    -- check IF ticket_type is not 'feedback'
25
    IF lower(new.ticket_type) <> 'feedback' THEN
26
      INSERT INTO checking_tasks_queue (http_verb, payload, due_time, replied)
27
      values (
28
        'POST',
29
        jsonb_build_object(
30
          'channel_id', new.channel_id,
31
          'thread_ts', thread_timestamp,
32
          'escalation_level', i,
33
          'ticket_id', new.ticket_number,
34
          'ticket_priority', new.ticket_priority,
35
          'ticket_type', new.ticket_type
36
        ),
37
        new.ts + (currentinterval * interval '1 minute'),
38
        false
39
      );
40
    END IF;
41
  END LOOP;
42
  -- return the new slack_msg row
43
  return new;
44
END;
45
$$;
`
### **Verifying Due Tasks**[ #](https://supabase.com/blog/exploring-support-tooling#verifying-due-tasks)
The core function **`check_due_tasks_and_update()`**plays a pivotal role in task verification and status updating. It ensures that tasks are duly acknowledged, thereby facilitating timely resolution.
`
1
CREATE OR REPLACE FUNCTION "public"."check_due_tasks_and_update"() RETURNS "void"
2
  LANGUAGE "plpgsql"
3
  AS $$
4
DECLARE
5
  _task RECORD;
6
  _response JSONB;
7
  _response_row JSONB;
8
  _ticket_id text;
9
  _have_replied BOOLEAN;
10
  _ticket_array text;
11
  _lock_key CONSTANT int := 42;
12
  _lock_acquired boolean;
13
BEGIN
14
  -- Try to acquire the advisory lock
15
  _lock_acquired := pg_try_advisory_lock(_lock_key);
16
  IF NOT _lock_acquired THEN
17
    RAISE NOTICE 'Could not acquire lock. Another instance is running. Exiting function...';
18
    RETURN;
19
  END IF;
2021
  -- Call create_ticket_array()
22
  RAISE NOTICE 'Calling create_ticket_array()';
23
  _ticket_array := public.create_ticket_array();
2425
  -- Check IF _ticket_array is '[]'
26
  IF _ticket_array = '[]' THEN
27
    RAISE NOTICE 'No tickets to process. Exiting function...';
28
    -- Release the advisory lock
29
    PERFORM pg_advisory_unlock(_lock_key);
30
    RETURN;
31
  END IF;
3233
  -- Call help_plataform_wrapper() using _ticket_array
34
  RAISE NOTICE 'Calling help_plataform_wrapper()';
35
  _response := public.help_plataform_wrapper(_ticket_array);
3637
  -- Check IF _response is NULL
38
  IF _response IS NULL THEN
39
    RAISE NOTICE 'Response is NULL. Exiting function...';
40
    -- Release the advisory lock
41
    PERFORM pg_advisory_unlock(_lock_key);
42
    RETURN;
43
  END IF;
4445
  -- Process the response
46
  FOR _response_row IN SELECT * FROM jsonb_array_elements(_response)
47
  LOOP
48
    _ticket_id := _response_row->>'ticket_id';
49
    _have_replied := (_response_row->>'have_replied')::BOOLEAN;
50
    RAISE NOTICE 'Processing response for ticket_id: %, have_replied: %', _ticket_id, _have_replied;
51
    IF _have_replied THEN
52
      RAISE NOTICE 'Ticket % has a reply. Updating...', _ticket_id;
53
      -- Perform actions for replied tickets
54
      UPDATE public.checking_tasks_queue
55
      SET replied_at = NOW(), replied = TRUE
56
      WHERE payload->>'ticket_id' = _ticket_id;
57
    ELSE
58
      RAISE NOTICE 'Ticket % has no reply. Taking actions...', _ticket_id;
59
      -- Perform actions for no reply
60
      SELECT * INTO _task FROM public.checking_tasks_queue
61
      WHERE payload->>'ticket_id' = _ticket_id AND status = '' AND due_time <= NOW()
62
      ORDER BY due_time ASC
63
      LIMIT 1;
6465
      IF FOUND THEN
66
        RAISE NOTICE 'Sending Slack notification for ticket %', _ticket_id;
67
        -- Use EXCEPTION to handle duplicate keys
68
        BEGIN
69
          INSERT INTO post_to_slack_log(payload) VALUES (_task.payload);
70
          PERFORM slack_post_wrapper(_task.payload);
71
        EXCEPTION
72
          WHEN unique_violation THEN
73
            RAISE NOTICE 'Duplicate entry for ticket %. Skipping...', _ticket_id;
74
          WHEN OTHERS THEN
75
            RAISE NOTICE 'Error while inserting into post_to_slack_log. Skipping...';
76
            RAISE NOTICE '% %', SQLERRM, SQLSTATE;
77
        END;
78
        -- Update the status to 'sent' after calling slack_post_wrapper
79
        UPDATE public.checking_tasks_queue
80
        SET status = 'sent'
81
        WHERE id = _task.id;
82
      ELSE
83
        RAISE NOTICE 'Task for ticket % not found!', _ticket_id;
84
      END IF;
85
    END IF;
86
  END LOOP;
87
  -- Release the advisory lock
88
  PERFORM pg_advisory_unlock(_lock_key);
89
END;
90
$$;
`
### Posting SLA Enforcement Messages on Slack[#](https://supabase.com/blog/exploring-support-tooling#posting-sla-enforcement-messages-on-slack)
SLA Buddy employs the Edge Function **`post_ticket_escalation`**to post SLA enforcement messages on Slack. This integration with PostgreSQL functions ensures streamlined execution and effective communication with support engineers.
## Interactions with Support Members[#](https://supabase.com/blog/exploring-support-tooling#interactions-with-support-members)
SLA Buddy fosters seamless interactions between support engineers and the tool itself. Through Slack threads, support members can postpone the next steps in the escalation process by 30 min by `@mentioning` the bot in the thread. We also pushed a [guide on how to interact with mentions](https://supabase.com/docs/guides/functions/examples/slack-bot-mention) in Slack as part of the bot's development.
The bot won't get disarmed until a response is sent in the ticket because we believe that even if the Support Engineer is unable to help the user, they can at least triage and set expectations for the next steps in the ticket like escalating to a specific team.
## Watching Support Events[#](https://supabase.com/blog/exploring-support-tooling#watching-support-events)
Another crucial aspect of SLA Buddy is its ability to monitor support events seamlessly. At Supabase we have the concept of Embedded Support when a member of the support team will work on more advanced tickets related to a specific Supabase product such as Edge Functions, Dashboard, Storage, Auth, Realtime etc.
The shift information about Support Engineers is hosted in a Google Calendar. This information is retrieved using the following function:
`
1
CREATE OR REPLACE FUNCTION "public"."get_embedded_event_names"
2
	("date_param" timestamp with time zone DEFAULT "now"())
3
 RETURNS "jsonb"
4
 LANGUAGE "plpgsql" SECURITY DEFINER
5
 SET "search_path" TO ''
6
 AS $$
7
DECLARE
8
 target_date timestamp with time zone := COALESCE(date_param, now());
9
 start_date timestamp with time zone := target_date + INTERVAL '2 hours';
10
 end_date timestamp with time zone := start_date + INTERVAL '1 day' - INTERVAL '1 millisecond';
11
 time_min text := to_char(start_date, 'YYYY-MM-DD"T"HH24:MI:SS.MS"Z"');
12
 time_max text := to_char(end_date, 'YYYY-MM-DD"T"HH24:MI:SS.MS"Z"');
13
 base_url text;
14
 api_url text;
15
 response jsonb;
16
 events jsonb; -- Change the declaration to jsonb
17
 embedded_event_names text[];
18
BEGIN
19
 SELECT decrypted_secret
20
 INTO base_url
21
 FROM vault.decrypted_secrets
22
 WHERE name = 'calendar_base_url';
2324
 api_url := base_url || '&timeMin=' || time_min || '&timeMax=' || time_max;
2526
 select "content"::jsonb into response from extensions.http_get(api_url);
27
 events := response->'items'; -- Remove the typecast to ::jsonb
2829
 SELECT ARRAY_AGG(event->>'summary')
30
 INTO embedded_event_names
31
 FROM jsonb_array_elements(events) AS event -- Use jsonb_array_elements function
32
 WHERE (event->>'summary') ILIKE '%embedded%';
33
 RETURN COALESCE(to_jsonb(embedded_event_names)::text,'[]');
34
END;
35
$$;
`
**Escalation Logic**
SLA Buddy's escalation logic is defined in 4 steps of escalation going from a more narrow set of Support Engineers to the Head of Success. Here's the progression:
Target| Level| Action| Timeline  
---|---|---|---  
Enterprise| 1| Non-embedded support| 10 min  
| 2| On-shift support| 20 min  
| 3| @group-support| 35 min  
| 4| @head of success| 50 min  
Team| 1| Non-embedded support| 1 hour  
| 2| On-shift support| 3 hours  
| 3| @group-support| 6 hours  
| 4| @head of success| 12 hours  
## Conclusion[#](https://supabase.com/blog/exploring-support-tooling#conclusion)
SLA Buddy is a core operational component for Supabase support operations, keeping the whole team informed and engaged, and assisting with prioritizing tickets by their SLA restrictions.
We are firm believers in letting technology streamline operational work and allowing humans to focus on solving real problems, and SLA Buddy is a great example of that.
## Final Thoughts[#](https://supabase.com/blog/exploring-support-tooling#final-thoughts)
SLA Buddy started a passion project, born from a need to ensure that we're providing top-quality support to Supabase's users. We're big fans of personal exploration and kaizen incremental change.
And we're not done with SLA Buddy. It'll grow and evolve as Supabase grows, and our needs and the needs of our users change. Because it's built on Supabase features, it'll be easy to update and maintain, and it'll provide more and more value to our internal operations, we hope it might provide some value to you, too. We're also big believers in the Open Source community, and welcome any feedback or ideas you might have to make SLA Buddy even better for everyone.
## More Resources About Slack and Edge Functions[#](https://supabase.com/blog/exploring-support-tooling#more-resources-about-slack-and-edge-functions)
  * [GitHub Repo: SLA Buddy](https://github.com/mansueli/slabuddy)
  * [Docs Edge Functions: slack mention reply](https://supabase.com/docs/guides/functions/examples/slack-bot-mention)
  * [Docs Edge Functions: geting started](https://supabase.com/docs/guides/functions/getting-started)
  * [Docs Edge Functions: debugging](https://supabase.com/docs/guides/functions/debugging)
  * [Slack Consolidate: a slackbot build with Python & Supabase](https://supabase.com/blog/slack-consolidate-slackbot-to-consolidate-messages)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fexploring-support-tooling&text=Exploring%20Support%20Tooling%20at%20Supabase%3A%20A%20Dive%20into%20SLA%20Buddy)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fexploring-support-tooling&text=Exploring%20Support%20Tooling%20at%20Supabase%3A%20A%20Dive%20into%20SLA%20Buddy)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fexploring-support-tooling&t=Exploring%20Support%20Tooling%20at%20Supabase%3A%20A%20Dive%20into%20SLA%20Buddy)
[Last postPostgres Bloat Minimization26 April 2024](https://supabase.com/blog/postgres-bloat)
[Next postPackaging Supabase with Nix25 April 2024](https://supabase.com/blog/nix-postgres)
[slack](https://supabase.com/blog/tags/slack)[service-level-agreement](https://supabase.com/blog/tags/service-level-agreement)[support](https://supabase.com/blog/tags/support)
On this page
  * [Introduction](https://supabase.com/blog/exploring-support-tooling#introduction)
    * [Introducing SLA Buddy](https://supabase.com/blog/exploring-support-tooling#introducing-sla-buddy)
  * [Dogfooding: The Birth of SLA Buddy](https://supabase.com/blog/exploring-support-tooling#dogfooding-the-birth-of-sla-buddy)
  * [Understanding SLA Buddy's Functions](https://supabase.com/blog/exploring-support-tooling#understanding-sla-buddys-functions)
    * [SLA Enforcement](https://supabase.com/blog/exploring-support-tooling#sla-enforcement)
  * [Let's take a look at SLA Buddy's Operations](https://supabase.com/blog/exploring-support-tooling#lets-take-a-look-at-sla-buddys-operations)
    * [Watching Messages](https://supabase.com/blog/exploring-support-tooling#watching-messages)
    * [**Verifying Due Tasks**](https://supabase.com/blog/exploring-support-tooling#verifying-due-tasks)
    * [Posting SLA Enforcement Messages on Slack](https://supabase.com/blog/exploring-support-tooling#posting-sla-enforcement-messages-on-slack)
  * [Interactions with Support Members](https://supabase.com/blog/exploring-support-tooling#interactions-with-support-members)
  * [Watching Support Events](https://supabase.com/blog/exploring-support-tooling#watching-support-events)
  * [Conclusion](https://supabase.com/blog/exploring-support-tooling#conclusion)
  * [Final Thoughts](https://supabase.com/blog/exploring-support-tooling#final-thoughts)
  * [More Resources About Slack and Edge Functions](https://supabase.com/blog/exploring-support-tooling#more-resources-about-slack-and-edge-functions)


Share this article
[](https://twitter.com/intent/tweet?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fexploring-support-tooling&text=Exploring%20Support%20Tooling%20at%20Supabase%3A%20A%20Dive%20into%20SLA%20Buddy)[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fsupabase.com%2Fblog%2Fexploring-support-tooling&text=Exploring%20Support%20Tooling%20at%20Supabase%3A%20A%20Dive%20into%20SLA%20Buddy)[](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fsupabase.com%2Fblog%2Fexploring-support-tooling&t=Exploring%20Support%20Tooling%20at%20Supabase%3A%20A%20Dive%20into%20SLA%20Buddy)
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

