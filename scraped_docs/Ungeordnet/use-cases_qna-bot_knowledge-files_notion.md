---
url: https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion
scraped_at: 2025-05-25T08:59:19.977109
title: Notion | Runbear
---

[Skip to main content](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion#__docusaurus_skipToContent_fallback)
[![Runear Logo](https://docs.runbear.io/img/logo.svg)**Runbear**](https://docs.runbear.io/)[Docs](https://docs.runbear.io/)[Use Cases](https://docs.runbear.io/use-cases)
[Runbear](https://runbear.io)
  * [Use Cases](https://docs.runbear.io/use-cases)
    * [Article Summarizer](https://docs.runbear.io/use-cases/article-summarizer/)
    * [Customer Service](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion)
    * [Document Review Bot](https://docs.runbear.io/use-cases/document-review-bot/)
    * [Jira Overdue Tracker](https://docs.runbear.io/use-cases/jira-overdue-tracker/)
    * [Proof of Concept for LLM Apps](https://docs.runbear.io/use-cases/proof-of-concept/)
    * [Proofreading Bot](https://docs.runbear.io/use-cases/proofreading-bot/)
    * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
      * Preparing Knowledge Files
        * [Notion](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion)
      * [OpenAI Assistants](https://docs.runbear.io/use-cases/qna-bot/openai-assistants)
      * [OpenAI GPTs](https://docs.runbear.io/use-cases/qna-bot/openai-gpts)
    * [Sales Copy Generator](https://docs.runbear.io/use-cases/sales-copy-generator/)
    * [Sentiment Analyzer](https://docs.runbear.io/use-cases/sentiment-analyzer/)
    * [Team Deputy](https://docs.runbear.io/use-cases/team-deputy/)
    * [Thread Summarizer](https://docs.runbear.io/use-cases/thread-summarizer/)


  * [](https://docs.runbear.io/)
  * [Use Cases](https://docs.runbear.io/use-cases)
  * [Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)
  * Preparing Knowledge Files
  * Notion


On this page
# Converting Notion Pages into the OpenAI Knowledge Files
You can convert Notion Pages into OpenAI knowledge files by exporting and merging Notion pages.
## Exporting Notion Pages[​](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion#exporting-notion-pages "Direct link to Exporting Notion Pages")
  1. Open the page to export.
  2. Click the **"•••"** button on the top right and select the **"Export"** option.
  3. Make the options identical to the below:
     * Export format: **Markdown & CSV**
     * Include database: **Current view**
     * Include content: **No files or images**
     * Include subpages: **Yes**
     * Create folders for subpages: **No**
  4. Download the files by clicking the **"Export"** button.


## Merging Exported Files[​](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion#merging-exported-files "Direct link to Merging Exported Files")
The files are supposed to be merged into a few files because OpenAI does not allow uploading more than 20 knowledge files.
Visit the **[Merge Text Files](https://runbear.io/tools/merge-text-files)** page to merge the files.
## Expected Results[​](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion#expected-results "Direct link to Expected Results")
The merged file should be plain markdown text, like the below:
Sample content
```
# ACME Employee Handbook## Leave PolicyACME is committed to supporting our employees' work-life balance. This leave policy outlines the various types of leave available to employees and the procedures for requesting leave.### Sick LeaveEligibility: All full-time employees are eligible for sick leave.Entitlement: Employees are entitled to [14] paid sick days per year.Usage: Sick leave can be used for illness, medical appointments, or care for an ill family member. Employees should notify their supervisor as soon as possible if they need to take sick leave.### Annual Leave(Vacation Leave)Eligibility: All full-time employees are eligible for annual leave.Accrual: Employees accrue [20] days of paid vacation per year. Vacation accrual begins on the first day of employment and is prorated for the first year based on the start date.Carryover: Employees can carry over up to [5] days of unused vacation to the next year. Unused vacation days above this limit will be forfeited.Scheduling: Vacation requests should be submitted to your supervisor at least [2] weeks in advance. Approval is based on business needs and on a first-come, first-served basis.### Procedure for Requesting LeaveEmployees should request leave by filling out the 'Leave Request Form' and submitting it to their supervisor for approval.Requests for leave should be made as far in advance as possible, especially for extended periods of leave.In emergencies or unexpected situations, employees should notify their supervisor as soon as possible.
```

[PreviousBuilding a Q&A Bot](https://docs.runbear.io/use-cases/qna-bot/)[NextOpenAI Assistants](https://docs.runbear.io/use-cases/qna-bot/openai-assistants)
  * [Exporting Notion Pages](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion#exporting-notion-pages)
  * [Merging Exported Files](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion#merging-exported-files)
  * [Expected Results](https://docs.runbear.io/use-cases/qna-bot/knowledge-files/notion#expected-results)


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

