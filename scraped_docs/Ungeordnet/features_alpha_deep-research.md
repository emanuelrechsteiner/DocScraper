---
url: https://docs.firecrawl.dev/features/alpha/deep-research
scraped_at: 2025-05-25T08:35:06.876461
title: Deep Research | Firecrawl
---

[Firecrawl Docs home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo.png)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/firecrawl/logo/logo-dark.png)](https://firecrawl.dev)
v1
Search...
⌘KAsk AI
  * [Status](https://firecrawl.betteruptime.com)
  * Support
  * [mendableai/firecrawl38.791](https://github.com/mendableai/firecrawl)
  * [mendableai/firecrawl38.791](https://github.com/mendableai/firecrawl)


Search...
Navigation
Deep Research API
Deep Research
[Documentation](https://docs.firecrawl.dev/introduction)[SDKs](https://docs.firecrawl.dev/sdks/overview)[Learn](https://www.firecrawl.dev/blog/category/tutorials)[Integrations](https://www.firecrawl.dev/app)[API Reference](https://docs.firecrawl.dev/api-reference/introduction)
* [Playground](https://firecrawl.dev/playground)
* [Blog](https://firecrawl.dev/blog)
* [Community](https://discord.gg/gSmWdAkdwd)
* [Changelog](https://firecrawl.dev/changelog)
##### Get Started
  * [Quickstart](https://docs.firecrawl.dev/introduction)
  * [MCP Server](https://docs.firecrawl.dev/mcp)
  * [Launch Week III (New)](https://docs.firecrawl.dev/launch-week)
  * [Rate Limits](https://docs.firecrawl.dev/rate-limits)
  * [Advanced Scraping Guide](https://docs.firecrawl.dev/advanced-scraping-guide)


##### Standard Features
  * Scrape
  * Crawl
  * [Map](https://docs.firecrawl.dev/features/map)
  * [Search](https://docs.firecrawl.dev/features/search)


##### Agentic Features
  * [Extract](https://docs.firecrawl.dev/features/extract)
  * [FIRE-1](https://docs.firecrawl.dev/agents/fire-1)


##### Alpha tools
  * LLMs.txt API
  * Deep Research API
    * [Deep Research API](https://docs.firecrawl.dev/features/alpha/deep-research)


##### Contributing
  * [Open Source vs Cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud)
  * [Running locally](https://docs.firecrawl.dev/contributing/guide)
  * [Self-hosting](https://docs.firecrawl.dev/contributing/self-host)


Deep Research API
# Deep Research
Copy page
Research API that allows you to build deep research into your own applications”
## 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#introducing-deep-research-alpha)
Introducing Deep Research (Alpha)
The `/deep-research` endpoint enables AI-powered deep research and analysis on any topic. Simply provide a research query, and Firecrawl will autonomously explore the web, gather relevant information, and synthesize findings into comprehensive insights.
## 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#building-with-deep-research)
Building with Deep Research
Deep Research works by:
  1. Analyzing your query to identify key research areas
  2. Iteratively searching and exploring relevant web content
  3. Synthesizing information from multiple sources
  4. Providing structured findings with source attribution


Firecrawl provides structured results that enable you to build powerful applications:
  * **Activities** : Detailed timeline of research steps and findings
  * **Sources** : Curated list of relevant URLs with titles and descriptions
  * **Final Analysis** : Comprehensive synthesis of key insights and conclusions
  * **Progress Tracking** : Real-time status updates on research depth and completion


### 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#example-usage)
Example Usage
Python
Node
cURL
Copy
```
from firecrawl import FirecrawlApp
# Initialize the client
firecrawl = FirecrawlApp(api_key="your_api_key")

# Start research with real-time updates
def on_activity(activity):
  print(f"[{activity['type']}] {activity['message']}")
# Run deep research
results = firecrawl.deep_research(
  query="What are the latest developments in quantum computing?",
  max_depth=5,
  time_limit=180,
  max_urls=15,
  on_activity=on_activity
)
# Access research findings.
print(f"Final Analysis: {results['data']['finalAnalysis']}")
print(f"Sources: {len(results['data']['sources'])} references")


```

**Key Parameters:**
  * **query** : The research topic or question you want to investigate
  * **maxDepth** (Optional): Maximum number of research iterations (1-10, default: 7)
  * **timeLimit** (Optional): Time limit in seconds (30-300, default: 270)
  * **maxUrls** (Optional): Maximum number of URLs to analyze (1-1000, default: 20)


See [API Reference](https://docs.firecrawl.dev/api-reference/endpoint/deep-research) for more details.
### 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#response)
Response
Copy
```
{
 "success": true,
 "data": {
  "finalAnalysis": "Recent developments in quantum computing show significant progress in several key areas:\n\n1. Error Correction: Improved quantum error correction techniques have increased qubit stability\n2. Quantum Supremacy: Multiple demonstrations of quantum advantage in specific computational tasks\n3. Hardware Advances: New architectures using superconducting circuits and trapped ions\n4. Commercial Applications: Growing industry adoption in optimization and cryptography",
  "activities": [
   {
    "type": "search",
    "status": "completed",
    "message": "Analyzing quantum computing breakthroughs in 2024",
    "timestamp": "2024-03-15T10:30:00Z",
    "depth": 1
   }
  ],
  "sources": [
   {
    "url": "https://example.com/quantum-computing-2024",
    "title": "Latest Quantum Computing Breakthroughs",
    "description": "Overview of recent advances in quantum computing technology"
   }
  ]
 },
 "status": "completed",
 "currentDepth": 5,
 "maxDepth": 5,
 "expiresAt": "2024-03-16T10:30:00Z"
} 

```

## 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#monitoring-research-progress)
Monitoring Research Progress
Deep Research jobs run asynchronously. You can monitor progress and receive real-time updates:
Python
Node
Copy
```
from firecrawl import FirecrawlApp
# Initialize the client
firecrawl = FirecrawlApp(api_key="your_api_key")
# Check research status
status = firecrawl.check_deep_research_status("job_id")
# Print current progress
print(f"Status: {status.status}")
print(f"Progress: {status.current_depth}/{status.max_depth} iterations")
if status.status == 'completed':
  print(f"Final Analysis: {status.data.final_analysis}")
  print(f"Sources found: {len(status.data.sources)}") 

```

### 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#research-activities)
Research Activities
The data response includes:
  * **activities** : List of research activities with the following properties:
  * `type`: Type of activity (‘search’, ‘extract’, ‘analyze’, ‘reasoning’, ‘synthesis’, ‘thought’)
  * `status`: Activity status (‘processing’, ‘complete’, ‘error’)
  * `message`: Description of the activity or finding
  * `timestamp`: ISO timestamp of when the activity occurred
  * `depth`: Current research depth level
  * **sources** : Referenced URLs with titles and descriptions
  * `title`: Title of the source
  * `description`: Description of the source
  * `url`: URL of the source
  * `icon`: Icon of the source
  * **finalAnalysis** : Comprehensive analysis (when completed)


### 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#status-examples)
Status Examples
#### 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#in-progress)
In Progress
Copy
```
{
 "success": true,
 "status": "processing",
 "data": {
  "activities": [
   {
    "type": "search",
    "status": "completed",
    "message": "Initial research on quantum computing trends",
    "timestamp": "2024-03-15T10:30:00Z",
    "depth": 1
   },
   {
    "type": "analyze",
    "status": "in_progress",
    "message": "Analyzing quantum error correction advances",
    "timestamp": "2024-03-15T10:31:00Z",
    "depth": 2
   }
  ],
  "sources": [
   {
    "url": "https://example.com/quantum-computing-2024",
    "title": "Latest Quantum Computing Breakthroughs",
    "description": "Overview of recent advances in quantum computing technology"
    }
   ],
  },
 "currentDepth": 2,
 "maxDepth": 5,
 "expiresAt": "2024-03-16T10:30:00Z"
} 

```

#### 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#completed)
Completed
Copy
```
{
 "success": true,
 "status": "completed",
 "data": {
  "finalAnalysis": "Recent developments in quantum computing show significant progress in several key areas:\n\n1. Error Correction: Improved quantum error correction techniques have increased qubit stability\n2. Quantum Supremacy: Multiple demonstrations of quantum advantage in specific computational tasks\n3. Hardware Advances: New architectures using superconducting circuits and trapped ions\n4. Commercial Applications: Growing industry adoption in optimization and cryptography",
  "activities": [
   {
    "type": "search",
    "status": "completed",
    "message": "Initial research on quantum computing trends",
    "timestamp": "2024-03-15T10:30:00Z",
    "depth": 1
   },
   {
    "type": "analyze",
    "status": "completed",
    "message": "Analyzing quantum error correction advances",
    "timestamp": "2024-03-15T10:31:00Z",
    "depth": 2
   },
   {
    "type": "synthesize",
    "status": "completed",
    "message": "Synthesizing findings from multiple sources",
    "timestamp": "2024-03-15T10:32:00Z",
    "depth": 5
   }
  ],
  "sources": [
   {
    "url": "https://example.com/quantum-computing-2024",
    "title": "Latest Quantum Computing Breakthroughs",
    "description": "Overview of recent advances in quantum computing technology"
   },
   {
    "url": "https://example.com/quantum-error-correction",
    "title": "Advances in Quantum Error Correction",
    "description": "Deep dive into recent quantum error correction techniques"
   }
  ]
 },
 "currentDepth": 5,
 "maxDepth": 5,
 "expiresAt": "2024-03-16T10:30:00Z"
} 

```

### 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#json-output)
JSON Output
You can now specify the JSON output format by setting the `formats` parameter to `json`. Set the `jsonOptions` parameter to specify the schema for the JSON output.
### 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#customize-even-further)
Customize even further
You can also specify a `systemPrompt` and an `analysisPrompt` to customize the agentic process and the final analysis, respectively.
## 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#models)
Models
While in Alpha we use a combination of small models to explore the web and synthesize information. That way we can keep the cost low and the research fast. But this can result in the synthesis not being very long and detailed. If you’d like us to offer more powerful models, let us know at help@firecrawl.com.
## 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#known-limitations-alpha)
Known Limitations (Alpha)
  1. **Research Scope** Best suited for topics with publicly available information. May not access paywalled or private content.
  2. **Time Constraints** Research jobs are limited to 10 minutes maximum to ensure reasonable response times.
  3. **Source Verification** While sources are provided, manual verification of critical information is recommended.
  4. **Alpha State** As an Alpha feature, the research methodology and output format may evolve based on feedback.


## 
[​](https://docs.firecrawl.dev/features/alpha/deep-research#billing-and-usage)
Billing and Usage
Billing is done based on the number of `urls` analyzed. Each `url` is 1 credit. You can specify the max number of urls to analyze with the `maxUrls` parameter.
Have feedback or need help? Email help@firecrawl.com.
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/features/alpha/deep-research.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /features/alpha/deep-research)
[Generate with NPX](https://docs.firecrawl.dev/features/alpha/llmstxt-npx)[Open Source vs Cloud](https://docs.firecrawl.dev/contributing/open-source-or-cloud)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Introducing Deep Research (Alpha)](https://docs.firecrawl.dev/features/alpha/deep-research#introducing-deep-research-alpha)
  * [Building with Deep Research](https://docs.firecrawl.dev/features/alpha/deep-research#building-with-deep-research)
  * [Example Usage](https://docs.firecrawl.dev/features/alpha/deep-research#example-usage)
  * [Response](https://docs.firecrawl.dev/features/alpha/deep-research#response)
  * [Monitoring Research Progress](https://docs.firecrawl.dev/features/alpha/deep-research#monitoring-research-progress)
  * [Research Activities](https://docs.firecrawl.dev/features/alpha/deep-research#research-activities)
  * [Status Examples](https://docs.firecrawl.dev/features/alpha/deep-research#status-examples)
  * [In Progress](https://docs.firecrawl.dev/features/alpha/deep-research#in-progress)
  * [Completed](https://docs.firecrawl.dev/features/alpha/deep-research#completed)
  * [JSON Output](https://docs.firecrawl.dev/features/alpha/deep-research#json-output)
  * [Customize even further](https://docs.firecrawl.dev/features/alpha/deep-research#customize-even-further)
  * [Models](https://docs.firecrawl.dev/features/alpha/deep-research#models)
  * [Known Limitations (Alpha)](https://docs.firecrawl.dev/features/alpha/deep-research#known-limitations-alpha)
  * [Billing and Usage](https://docs.firecrawl.dev/features/alpha/deep-research#billing-and-usage)


Assistant
Responses are generated using AI and may contain mistakes.

