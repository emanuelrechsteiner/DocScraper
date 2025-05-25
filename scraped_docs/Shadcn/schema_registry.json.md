---
url: https://ui.shadcn.com/schema/registry.json
scraped_at: 2025-05-24T22:30:28.506948
title: Untitled
---

```
{
 "$schema": "https://json-schema.org/draft-07/schema#",
 "description": "A shadcn registry of components, hooks, pages, etc.",
 "type": "object",
 "properties": {
  "name": {
   "type": "string"
  },
  "homepage": {
   "type": "string"
  },
  "items": {
   "type": "array",
   "items": {
    "$ref": "https://ui.shadcn.com/schema/registry-item.json"
   }
  }
 },
 "required": ["name", "homepage", "items"],
 "uniqueItems": true,
 "minItems": 1
}

```


