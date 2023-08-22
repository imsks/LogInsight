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

# Setup Virtual Env

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install opensearch-py==2.2.0
```

# Run OpenSearch Dashboards using Docker

https://opensearch.org/docs/latest/install-and-configure/install-dashboards/docker/
