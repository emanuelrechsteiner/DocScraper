# Developer Documentation
URL: https://docs.crawl4ai.com/core/docker-deploymeny/
Processed: 2025-01-28T22:13:52.202052

## Document Statistics
- Original Length: 21559 characters
- Generated Length: 5990 characters
- Content Ratio: 27.78%
- Code Blocks: 0

## Technical Analysis
# Crawl4AI Developer Guide

## 1. Overview and Purpose
Crawl4AI is a powerful web crawling framework designed to facilitate the extraction of data from websites efficiently. It provides a robust set of features that cater to various use cases, including data scraping, content aggregation, and automated testing.

### Core Functionality and Purpose
Crawl4AI allows developers to create crawlers that can navigate websites, extract relevant information, and store it in a structured format. The framework is built with flexibility in mind, enabling users to customize their crawling strategies according to their specific needs.

### Key Capabilities and Limitations
- **Capabilities:**
  - Supports multiple extraction strategies (basic, LLM, cosine, JSON CSS).
  - Provides API security features to protect endpoints.
  - Offers Docker support for easy deployment and scalability.
  
- **Limitations:**
  - Requires proper configuration for optimal performance.
  - May encounter issues with websites that implement anti-scraping measures.

### Target Use Cases
- Data extraction for market research.
- Automated content aggregation for news and blogs.
- Testing web applications by simulating user interactions.

## 2. Technical Implementation
Crawl4AI is designed using modern architecture principles, ensuring scalability and maintainability.

### Architecture and Design Patterns
The framework employs a microservices architecture, allowing different components to communicate over APIs. This design pattern enhances modularity and enables independent scaling of services.

### Component Interactions
Key components include:
- **Crawler:** Responsible for navigating web pages and extracting data.
- **API Server:** Handles incoming requests and manages task submissions.
- **Database:** Stores extracted data and task statuses.

### Data Flow and State Management
Data flows from the crawler to the API server, which processes requests and updates the database with task results. State management is handled through task IDs, allowing users to track the status of their crawls.

## 3. Code Implementation
### Setup and Configuration
Crawl4AI can be deployed using Docker, making it easy to set up in various environments.

### Integration Steps
1. **Pull the Docker Image:**
   ```
   docker pull unclecode/crawl4ai:basic
   ```

2. **Run the Container:**
   ```
   docker run -p 11235:11235 unclecode/crawl4ai:basic
   ```

3. **Run with API Security Enabled:**
   ```
   docker run -p 11235:11235 -e CRAWL4AI_API_TOKEN=your_secret_token unclecode/crawl4ai:basic
   ```

### Usage Patterns
#### Basic Crawling
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "priority": 10
}
response = requests.post("http://localhost:11235/crawl", json=request)
task_id = response.json()["task_id"]
# Get results
result = requests.get(f"http://localhost:11235/task/{task_id}")
```

#### Structured Data Extraction
```
schema = {
  "name": "Crypto Prices",
  "baseSelector": ".cds-tableRow-t45thuk",
  "fields": [
    {
      "name": "crypto",
      "selector": "td:nth-child(1) h2",
      "type": "text",
    },
    {
      "name": "price",
      "selector": "td:nth-child(2)",
      "type": "text",
    }
  ],
}
request = {
  "urls": "https://www.coinbase.com/explore",
  "extraction_config": {
    "type": "json_css",
    "params": {"schema": schema}
  }
}
```

#### Dynamic Content Handling
```
request = {
  "urls": "https://www.nbcnews.com/business",
  "js_code": [
    "const loadMoreButton = Array.from(document.querySelectorAll('button')).find(button => button.textContent.includes('Load More')); loadMoreButton && loadMoreButton.click();"
  ],
  "wait_for": "article.tease-card:nth-child(10)"
}
```

## 4. Advanced Usage
### Optimization Techniques
To enhance performance, consider adjusting the `MAX_CONCURRENT_TASKS` environment variable based on your server's capabilities.

### Performance Considerations
Monitor resource usage through the health endpoint to ensure optimal performance during high-load scenarios.

### Security Considerations
Always use environment variables for sensitive data like API tokens. Regularly update your dependencies to mitigate vulnerabilities.

### Error Handling
Implement robust error handling in your code to manage exceptions gracefully. Use try-catch blocks around API calls to handle potential failures.

## 5. Troubleshooting
### Common Issues
1. **Connection Refused**
   ```
   Error: Connection refused at localhost:11235
   ```
   Solution: Ensure the container is running and ports are properly mapped.

2. **Resource Limits**
   ```
   Error: No available slots
   ```
   Solution: Increase `MAX_CONCURRENT_TASKS` or container resources.

3. **GPU Access**
   ```
   Error: GPU not found
   ```
   Solution: Ensure proper NVIDIA drivers and use `--gpus all` flag.

### Debugging Strategies
- **Check Logs:** To view the container logs:
```
docker-compose -f docker-compose.local.yml logs -f
```

- **Remove Orphaned Containers:** If the service is still running unexpectedly:
```
docker-compose -f docker-compose.local.yml down --remove-orphans
```

### Known Limitations
- Some websites may block crawlers based on user-agent strings or IP addresses.
- Performance may degrade if too many concurrent tasks are executed without sufficient resources.

### Best Practices
1. **Resource Management** - Set appropriate memory and CPU limits.
2. **Scaling** - Use multiple containers for high load.
3. **Security** - Use environment variables for sensitive data.

## API Reference 📚
### Health Check
```
GET /health
```

### Submit Crawl Task
```
POST /crawl
Content-Type: application/json
{
  "urls": "string or array",
  "extraction_config": {
    "type": "basic|llm|cosine|json_css",
    "params": {}
  },
  "priority": 1-10,
  "ttl": 3600
}
```

### Get Task Status
```
GET /task/{task_id}
```

For more details, visit the [official documentation](https://docs.crawl4ai.com/core/docker-deploymeny/<https:/docs.crawl4ai.com/>).

## Processing Metadata
- Source: terminal-mkdocs-main-content
- Type: developer_documentation
- URL: https://docs.crawl4ai.com/core/docker-deploymeny/
