---
url: https://docs.anthropic.com/en/docs/build-with-claude/pdf-support
scraped_at: 2025-05-24T19:40:11.922151
title: PDF support - Anthropic
---

[Anthropic home page![light logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/light.svg)![dark logo](https://mintlify.s3.us-west-1.amazonaws.com/anthropic/logo/dark.svg)](https://docs.anthropic.com/)
English
Search...
⌘K
  * [Research](https://www.anthropic.com/research)
  * [News](https://www.anthropic.com/news)
  * [Go to claude.ai](https://claude.ai/)
  * [Go to claude.ai](https://claude.ai/)


Search...
Navigation
Explore features
PDF support
[Welcome](https://docs.anthropic.com/en/home)[Developer Guide](https://docs.anthropic.com/en/docs/welcome)[API Guide](https://docs.anthropic.com/en/api/overview)[Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)[Resources](https://docs.anthropic.com/en/resources/overview)[Release Notes](https://docs.anthropic.com/en/release-notes/overview)
* [Documentation](https://docs.anthropic.com/en/home)
* [Developer Console](https://console.anthropic.com/)
* [Developer Discord](https://www.anthropic.com/discord)
* [Support](https://support.anthropic.com/)
##### First steps
  * [Intro to Claude](https://docs.anthropic.com/en/docs/welcome)
  * [Get started](https://docs.anthropic.com/en/docs/get-started)


##### Models & pricing
  * [Models overview](https://docs.anthropic.com/en/docs/about-claude/models/overview)
  * [Choosing a model](https://docs.anthropic.com/en/docs/about-claude/models/choosing-a-model)
  * [Migrating to Claude 4](https://docs.anthropic.com/en/docs/about-claude/models/migrating-to-claude-4)
  * [Model deprecations](https://docs.anthropic.com/en/docs/about-claude/model-deprecations)
  * [Pricing](https://docs.anthropic.com/en/docs/about-claude/pricing)


##### Learn about Claude
  * [Building with Claude](https://docs.anthropic.com/en/docs/overview)
  * Use cases
  * [Context windows](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)
  * [Glossary](https://docs.anthropic.com/en/docs/about-claude/glossary)
  * Prompt engineering


##### Explore features
  * [Features overview](https://docs.anthropic.com/en/docs/build-with-claude/overview)
  * [Prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
  * [Extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
  * [Streaming Messages](https://docs.anthropic.com/en/docs/build-with-claude/streaming)
  * [Batch processing](https://docs.anthropic.com/en/docs/build-with-claude/batch-processing)
  * [Citations](https://docs.anthropic.com/en/docs/build-with-claude/citations)
  * [Multilingual support](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support)
  * [Token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting)
  * [Embeddings](https://docs.anthropic.com/en/docs/build-with-claude/embeddings)
  * [Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)
  * [PDF support](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support)
  * [Files API (beta)](https://docs.anthropic.com/en/docs/build-with-claude/files)


##### Agent components
  * Tools
  * Model Context Protocol (MCP)
  * [Computer use (beta)](https://docs.anthropic.com/en/docs/agents-and-tools/computer-use)
  * [Google Sheets add-on](https://docs.anthropic.com/en/docs/agents-and-tools/claude-for-sheets)


##### Test & evaluate
  * [Define success criteria](https://docs.anthropic.com/en/docs/test-and-evaluate/define-success)
  * [Develop test cases](https://docs.anthropic.com/en/docs/test-and-evaluate/develop-tests)
  * Strengthen guardrails
  * [Using the Evaluation Tool](https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool)


##### Legal center
  * [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
  * [Security and compliance](https://trust.anthropic.com/)


Explore features
# PDF support
Process PDFs with Claude. Extract text, analyze charts, and understand visual content from your documents.
You can now ask Claude about any text, pictures, charts, and tables in PDFs you provide. Some sample use cases:
  * Analyzing financial reports and understanding charts/tables
  * Extracting key information from legal documents
  * Translation assistance for documents
  * Converting document information into structured formats


## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#before-you-begin)
Before you begin
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#check-pdf-requirements)
Check PDF requirements
Claude works with any standard PDF. However, you should ensure your request size meet these requirements when using PDF support:
Requirement| Limit  
---|---  
Maximum request size| 32MB  
Maximum pages per request| 100  
Format| Standard PDF (no passwords/encryption)  
Please note that both limits are on the entire request payload, including any other content sent alongside PDFs.
Since PDF support relies on Claude’s vision capabilities, it is subject to the same [limitations and considerations](https://docs.anthropic.com/en/docs/build-with-claude/vision#limitations) as other vision tasks.
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#supported-platforms-and-models)
Supported platforms and models
PDF support is currently supported via direct API access and Google Vertex AI on:
  * Claude Opus 4 (`claude-opus-4-20250514`)
  * Claude Sonnet 4 (`claude-sonnet-4-20250514`)
  * Claude Sonnet 3.7 (`claude-3-7-sonnet-20250219`)
  * Claude Sonnet 3.5 models (`claude-3-5-sonnet-20241022`, `claude-3-5-sonnet-20240620`)
  * Claude Haiku 3.5 (`claude-3-5-haiku-20241022`)


This functionality will be supported on Amazon Bedrock soon.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#process-pdfs-with-claude)
Process PDFs with Claude
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#send-your-first-pdf-request)
Send your first PDF request
Let’s start with a simple example using the Messages API. You can provide PDFs to Claude in three ways:
  1. As a URL reference to a PDF hosted online
  2. As a base64-encoded PDF in `document` content blocks
  3. By a `file_id` from the [Files API](https://docs.anthropic.com/en/docs/build-with-claude/files)


#### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#option-1%3A-url-based-pdf-document)
Option 1: URL-based PDF document
The simplest approach is to reference a PDF directly from a URL:
Shell
Python
TypeScript
Java
Copy
```
 curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
   "model": "claude-opus-4-20250514",
   "max_tokens": 1024,
   "messages": [{
     "role": "user",
     "content": [{
       "type": "document",
       "source": {
         "type": "url",
         "url": "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf"
       }
     },
     {
       "type": "text",
       "text": "What are the key findings in this document?"
     }]
   }]
 }'

```

#### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#option-2%3A-base64-encoded-pdf-document)
Option 2: Base64-encoded PDF document
If you need to send PDFs from your local system or when a URL isn’t available:
Shell
Python
TypeScript
Java
Copy
```
# Method 1: Fetch and encode a remote PDF
curl -s "https://assets.anthropic.com/m/1cd9d098ac3e6467/original/Claude-3-Model-Card-October-Addendum.pdf" | base64 | tr -d '\n' > pdf_base64.txt
# Method 2: Encode a local PDF file
# base64 document.pdf | tr -d '\n' > pdf_base64.txt
# Create a JSON request file using the pdf_base64.txt content
jq -n --rawfile PDF_BASE64 pdf_base64.txt '{
  "model": "claude-opus-4-20250514",
  "max_tokens": 1024,
  "messages": [{
    "role": "user",
    "content": [{
      "type": "document",
      "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": $PDF_BASE64
      }
    },
    {
      "type": "text",
      "text": "What are the key findings in this document?"
    }]
  }]
}' > request.json
# Send the API request using the JSON file
curl https://api.anthropic.com/v1/messages \
 -H "content-type: application/json" \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -d @request.json

```

#### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#option-3%3A-files-api)
Option 3: Files API
For PDFs you’ll use repeatedly, or when you want to avoid encoding overhead, use the [Files API](https://docs.anthropic.com/en/docs/build-with-claude/files):
Shell
Python
TypeScript
Java
Copy
```
# First, upload your PDF to the Files API
curl -X POST https://api.anthropic.com/v1/files \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: files-api-2025-04-14" \
 -F "file=@document.pdf"
# Then use the returned file_id in your message
curl https://api.anthropic.com/v1/messages \
 -H "content-type: application/json" \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -H "anthropic-beta: files-api-2025-04-14" \
 -d '{
  "model": "claude-opus-4-20250514", 
  "max_tokens": 1024,
  "messages": [{
   "role": "user",
   "content": [{
    "type": "document",
    "source": {
     "type": "file",
     "file_id": "file_abc123"
    }
   },
   {
    "type": "text",
    "text": "What are the key findings in this document?"
   }]
  }]
 }'

```

### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#how-pdf-support-works)
How PDF support works
When you send a PDF to Claude, the following steps occur:
1
The system extracts the contents of the document.
  * The system converts each page of the document into an image.
  * The text from each page is extracted and provided alongside each page’s image.


2
Claude analyzes both the text and images to better understand the document.
  * Documents are provided as a combination of text and images for analysis.
  * This allows users to ask for insights on visual elements of a PDF, such as charts, diagrams, and other non-textual content.


3
Claude responds, referencing the PDF's contents if relevant.
Claude can reference both textual and visual content when it responds. You can further improve performance by integrating PDF support with:
  * **Prompt caching** : To improve performance for repeated analysis.
  * **Batch processing** : For high-volume document processing.
  * **Tool use** : To extract specific information from documents for use as tool inputs.


### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#estimate-your-costs)
Estimate your costs
The token count of a PDF file depends on the total text extracted from the document as well as the number of pages:
  * Text token costs: Each page typically uses 1,500-3,000 tokens per page depending on content density. Standard API pricing applies with no additional PDF fees.
  * Image token costs: Since each page is converted into an image, the same [image-based cost calculations](https://docs.anthropic.com/en/docs/build-with-claude/vision#evaluate-image-size) are applied.


You can use [token counting](https://docs.anthropic.com/en/docs/build-with-claude/token-counting) to estimate costs for your specific PDFs.
## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#optimize-pdf-processing)
Optimize PDF processing
### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#improve-performance)
Improve performance
Follow these best practices for optimal results:
  * Place PDFs before text in your requests
  * Use standard fonts
  * Ensure text is clear and legible
  * Rotate pages to proper upright orientation
  * Use logical page numbers (from PDF viewer) in prompts
  * Split large PDFs into chunks when needed
  * Enable prompt caching for repeated analysis


### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#scale-your-implementation)
Scale your implementation
For high-volume processing, consider these approaches:
#### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#use-prompt-caching)
Use prompt caching
Cache PDFs to improve performance on repeated queries:
Shell
Python
TypeScript
Java
Copy
```
# Create a JSON request file using the pdf_base64.txt content
jq -n --rawfile PDF_BASE64 pdf_base64.txt '{
  "model": "claude-opus-4-20250514",
  "max_tokens": 1024,
  "messages": [{
    "role": "user",
    "content": [{
      "type": "document",
      "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": $PDF_BASE64
      },
      "cache_control": {
       "type": "ephemeral"
      }
    },
    {
      "type": "text",
      "text": "Which model has the highest human preference win rates across each use-case?"
    }]
  }]
}' > request.json
# Then make the API call using the JSON file
curl https://api.anthropic.com/v1/messages \
 -H "content-type: application/json" \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -d @request.json

```

#### 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#process-document-batches)
Process document batches
Use the Message Batches API for high-volume workflows:
Shell
Python
TypeScript
Java
Copy
```
# Create a JSON request file using the pdf_base64.txt content
jq -n --rawfile PDF_BASE64 pdf_base64.txt '
{
 "requests": [
   {
     "custom_id": "my-first-request",
     "params": {
       "model": "claude-opus-4-20250514",
       "max_tokens": 1024,
       "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "document",
              "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": $PDF_BASE64
              }
            },
            {
              "type": "text",
              "text": "Which model has the highest human preference win rates across each use-case?"
            }
          ]
        }
       ]
     }
   },
   {
     "custom_id": "my-second-request",
     "params": {
       "model": "claude-opus-4-20250514",
       "max_tokens": 1024,
       "messages": [
        {
          "role": "user",
          "content": [
            {
              "type": "document",
              "source": {
                "type": "base64",
                "media_type": "application/pdf",
                "data": $PDF_BASE64
              }
            },
            {
              "type": "text",
              "text": "Extract 5 key insights from this document."
            }
          ]
        }
       ]
     }
   }
 ]
}
' > request.json
# Then make the API call using the JSON file
curl https://api.anthropic.com/v1/messages/batches \
 -H "content-type: application/json" \
 -H "x-api-key: $ANTHROPIC_API_KEY" \
 -H "anthropic-version: 2023-06-01" \
 -d @request.json

```

## 
[​](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#next-steps)
Next steps
## [Try PDF examplesExplore practical examples of PDF processing in our cookbook recipe.](https://github.com/anthropics/anthropic-cookbook/tree/main/multimodal)## [View API referenceSee complete API documentation for PDF support.](https://docs.anthropic.com/en/api/messages)
Was this page helpful?
YesNo
[Vision](https://docs.anthropic.com/en/docs/build-with-claude/vision)[Files API (beta)](https://docs.anthropic.com/en/docs/build-with-claude/files)
[x](https://x.com/AnthropicAI)[linkedin](https://www.linkedin.com/company/anthropicresearch)
On this page
  * [Before you begin](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#before-you-begin)
  * [Check PDF requirements](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#check-pdf-requirements)
  * [Supported platforms and models](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#supported-platforms-and-models)
  * [Process PDFs with Claude](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#process-pdfs-with-claude)
  * [Send your first PDF request](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#send-your-first-pdf-request)
  * [Option 1: URL-based PDF document](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#option-1%3A-url-based-pdf-document)
  * [Option 2: Base64-encoded PDF document](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#option-2%3A-base64-encoded-pdf-document)
  * [Option 3: Files API](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#option-3%3A-files-api)
  * [How PDF support works](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#how-pdf-support-works)
  * [Estimate your costs](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#estimate-your-costs)
  * [Optimize PDF processing](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#optimize-pdf-processing)
  * [Improve performance](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#improve-performance)
  * [Scale your implementation](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#scale-your-implementation)
  * [Use prompt caching](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#use-prompt-caching)
  * [Process document batches](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#process-document-batches)
  * [Next steps](https://docs.anthropic.com/en/docs/build-with-claude/pdf-support#next-steps)



