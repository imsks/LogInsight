# To Create a Index

```
PUT /logs
{
  "mappings": {
    "properties": {
      "timestamp": { "type": "date" },
      "log_level": { "type": "keyword" },
      "log_message": { "type": "text" }
    }
  }
}
```
