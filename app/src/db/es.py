from opensearchpy import OpenSearch

# es_client = OpenSearch(
#     hosts = [{"host": "localhost", "port": 9200}],
#     http_auth = ("admin", "admin"),
#     use_ssl = True,
#     verify_certs = False,
#     ssl_assert_hostname = False,
#     ssl_show_warn = False,
# )

def connect_to_os():
    host = 'opensearch-node1'
    port = 9200
    auth = ('admin', 'admin')

    try:
        client = OpenSearch(
            hosts = [{'host': host, 'port': port}],
            http_auth=auth,
            http_compress=True,
            use_ssl=True,
            verify_certs=False,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )
        print("HERE", client)
    except BaseException: 
        print("ERROR unable to connect opensearch instance")
        return False
    
    return client