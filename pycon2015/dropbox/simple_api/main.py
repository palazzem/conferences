from dropbox.client import DropboxClient
from pprint import pprint

from time import sleep

token = "DiUSTNb6VUEAAAAAAAAApYAZSaPDNOcaxBBVGVwUbrW9gqTYRYlQwUWAvJAemayf"

client = DropboxClient(token)

cursor = None

while True:
    has_more = True

    while has_more:
        result = client.delta(cursor)
        for path, metadata in result["entries"]:
            pprint(path)
            pprint(metadata)

        cursor = result["cursor"]
        has_more = result["has_more"]

        sleep(1)
