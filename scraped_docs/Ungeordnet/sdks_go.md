---
url: https://docs.firecrawl.dev/sdks/go
scraped_at: 2025-05-25T08:34:20.752008
title: Go SDK | Firecrawl
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
Community
Go
[Documentation](https://docs.firecrawl.dev/introduction)[SDKs](https://docs.firecrawl.dev/sdks/overview)[Learn](https://www.firecrawl.dev/blog/category/tutorials)[Integrations](https://www.firecrawl.dev/app)[API Reference](https://docs.firecrawl.dev/api-reference/introduction)
* [Playground](https://firecrawl.dev/playground)
* [Blog](https://firecrawl.dev/blog)
* [Community](https://discord.gg/gSmWdAkdwd)
* [Changelog](https://firecrawl.dev/changelog)
##### Overall
  * [Overview](https://docs.firecrawl.dev/sdks/overview)


##### Official
  * [Python](https://docs.firecrawl.dev/sdks/python)
  * [Node](https://docs.firecrawl.dev/sdks/node)


##### Community
  * [Go](https://docs.firecrawl.dev/sdks/go)
  * [Rust](https://docs.firecrawl.dev/sdks/rust)


Community
# Go
Copy page
Firecrawl Go SDK is a wrapper around the Firecrawl API to help you easily turn websites into markdown.
## 
[​](https://docs.firecrawl.dev/sdks/go#installation)
Installation
To install the Firecrawl Go SDK, you can use go get:
Go
Copy
```
go get github.com/mendableai/firecrawl-go

```

## 
[​](https://docs.firecrawl.dev/sdks/go#usage)
Usage
  1. Get an API key from [firecrawl.dev](https://firecrawl.dev)
  2. Set the `API key` as a parameter to the `FirecrawlApp` struct.
  3. Set the `API URL` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `https://api.firecrawl.dev`.
  4. Set the `version` and/or pass it as a parameter to the `FirecrawlApp` struct. Defaults to `v1`.


Here’s an example of how to use the SDK with error handling:
Go
Copy
```
import (
	"fmt"
	"log"
	"github.com/google/uuid"
	"github.com/mendableai/firecrawl-go"
)
func ptr[T any](v T) *T {
	return &v
}
func main() {
	// Initialize the FirecrawlApp with your API key
	apiKey := "fc-YOUR_API_KEY"
	apiUrl := "https://api.firecrawl.dev"
	version := "v1"
	app, err := firecrawl.NewFirecrawlApp(apiKey, apiUrl, version)
	if err != nil {
		log.Fatalf("Failed to initialize FirecrawlApp: %v", err)
	}
 // Scrape a website
 scrapeStatus, err := app.ScrapeUrl("https://firecrawl.dev", firecrawl.ScrapeParams{
  Formats: []string{"markdown", "html"},
 })
 if err != nil {
  log.Fatalf("Failed to send scrape request: %v", err)
 }
 fmt.Println(scrapeStatus)
	// Crawl a website
 idempotencyKey := uuid.New().String() // optional idempotency key
 crawlParams := &firecrawl.CrawlParams{
		ExcludePaths: []string{"blog/*"},
		MaxDepth:   ptr(2),
	}
	crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", crawlParams, &idempotencyKey)
	if err != nil {
		log.Fatalf("Failed to send crawl request: %v", err)
	}
	fmt.Println(crawlStatus) 
}

```

### 
[​](https://docs.firecrawl.dev/sdks/go#scraping-a-url)
Scraping a URL
To scrape a single URL with error handling, use the `ScrapeURL` method. It takes the URL as a parameter and returns the scraped data as a dictionary.
Go
Copy
```
// Scrape a website
scrapeResult, err := app.ScrapeUrl("https://firecrawl.dev", map[string]any{
 "formats": []string{"markdown", "html"},
})
if err != nil {
 log.Fatalf("Failed to scrape URL: %v", err)
}
fmt.Println(scrapeResult)

```

### 
[​](https://docs.firecrawl.dev/sdks/go#crawling-a-website)
Crawling a Website
To crawl a website, use the `CrawlUrl` method. It takes the starting URL and optional parameters as arguments. The `params` argument allows you to specify additional options for the crawl job, such as the maximum number of pages to crawl, allowed domains, and the output format.
Go
Copy
```
crawlStatus, err := app.CrawlUrl("https://firecrawl.dev", map[string]any{
 "limit": 100,
 "scrapeOptions": map[string]any{
  "formats": []string{"markdown", "html"},
 },
})
if err != nil {
 log.Fatalf("Failed to send crawl request: %v", err)
}
fmt.Println(crawlStatus) 

```

### 
[​](https://docs.firecrawl.dev/sdks/go#checking-crawl-status)
Checking Crawl Status
To check the status of a crawl job, use the `CheckCrawlStatus` method. It takes the job ID as a parameter and returns the current status of the crawl job.
Go
Copy
```
// Get crawl status
crawlStatus, err := app.CheckCrawlStatus("<crawl_id>")
if err != nil {
 log.Fatalf("Failed to get crawl status: %v", err)
}
fmt.Println(crawlStatus)

```

### 
[​](https://docs.firecrawl.dev/sdks/go#map-a-website)
Map a Website
Use `MapUrl` to generate a list of URLs from a website. The `params` argument let you customize the mapping process, including options to exclude subdomains or to utilize the sitemap.
Go
Copy
```
// Map a website
mapResult, err := app.MapUrl("https://firecrawl.dev", nil)
if err != nil {
 log.Fatalf("Failed to map URL: %v", err)
}
fmt.Println(mapResult)

```

## 
[​](https://docs.firecrawl.dev/sdks/go#error-handling)
Error Handling
The SDK handles errors returned by the Firecrawl API and raises appropriate exceptions. If an error occurs during a request, an exception will be raised with a descriptive error message.
[Suggest edits](https://github.com/mendableai/firecrawl-docs/edit/main/sdks/go.mdx)[Raise issue](https://github.com/mendableai/firecrawl-docs/issues/new?title=Issue on docs&body=Path: /sdks/go)
[Node](https://docs.firecrawl.dev/sdks/node)[Rust](https://docs.firecrawl.dev/sdks/rust)
[x](https://x.com/firecrawl_dev)[github](https://github.com/mendableai/firecrawl)[linkedin](https://www.linkedin.com/company/firecrawl)
[Powered by Mintlify](https://mintlify.com/preview-request?utm_campaign=poweredBy&utm_medium=referral&utm_source=docs.firecrawl.dev)
On this page
  * [Installation](https://docs.firecrawl.dev/sdks/go#installation)
  * [Usage](https://docs.firecrawl.dev/sdks/go#usage)
  * [Scraping a URL](https://docs.firecrawl.dev/sdks/go#scraping-a-url)
  * [Crawling a Website](https://docs.firecrawl.dev/sdks/go#crawling-a-website)
  * [Checking Crawl Status](https://docs.firecrawl.dev/sdks/go#checking-crawl-status)
  * [Map a Website](https://docs.firecrawl.dev/sdks/go#map-a-website)
  * [Error Handling](https://docs.firecrawl.dev/sdks/go#error-handling)


Assistant
Responses are generated using AI and may contain mistakes.

