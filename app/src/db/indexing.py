from app.src.db.es import es_client
from app.src.utils.functions import get_mapped_entries

index_name = "logs"

# Create Mapping
def create_mapping():
    body = {
        "mappings": {
            "properties": {
            "timestamp": { "type": "text" },
            "log_level": { "type": "keyword" },
            "log_message": { "type": "text" }
            }
        }
    }

    try:
        es_client.indices.create(index_name, body=body)
        print("Mapping created")
    except:
        print(f"Error in Creating Mapping {index_name}")

# Add Docs in Mapping
def add_docs(index_name, entries):
    for entry in entries:
        try:
            es_client.index(index=index_name, body=entry)
            print(f"Document added in {index_name} as {entry}")
        except:
            print(f"Error in adding the {entry} document as {index_name}")

# Delete Mapping
def delete_mapping(index_name):
    try:
        es_client.indices.delete(index=index_name)
        print("Mappings deleted!")
    except:
        print(f"Error in deleting the document as {index_name}")

mapped_log_entries = get_mapped_entries()

# create_mapping()
# add_docs(index_name, mapped_log_entries)
# delete_mapping(index_name)
