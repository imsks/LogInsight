# To Create a Index

```
PUT /logs
{
  "mappings": {
    "properties": {
      "timestamp": { "type": "text" },
      "log_level": { "type": "keyword" },
      "log_message": { "type": "text" }
    }
  }
}
```

# Add a document

```
POST logs/_doc
{"timestamp": "2023-08-16 16:35:20", "log_level": "ERROR", "log_message": "Database connection failed."}
```
