import time
from pathlib import Path

import requests
from rdflib import Graph

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)

graph = Graph()
graph.parse("metapnc.ttl")

urls = """
PREFIX schema: <http://schema.org/>

SELECT ?bid ?curl
WHERE {
    ?bid schema:contentUrl ?curl
}"""

for book_id, content_url in graph.query(urls):  # type: ignore
    book_name = book_id.split("/")[-1]

    book_dir = data_dir / book_name
    book_dir.mkdir(exist_ok=True)

    vol_name = content_url.split("/")[-1]
    vol_path = book_dir / vol_name

    print(f"Downloading {content_url} ...", end="", flush=True)

    response = requests.get(content_url, allow_redirects=True)

    with open(vol_path, "wb") as fp:
        fp.write(response.content)

    print(" done")

    time.sleep(3)
