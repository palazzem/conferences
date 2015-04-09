import os
import multyvac
import requests


# Rackspace config
multyvac.config.api_key = "cloudpipe18" # Rackspace Username
multyvac.config.api_secret_key = "683df297726d4bb18c6c230e5be795fe" # Rackspace API Key
multyvac.config.api_url = "https://cloudpipe.tmpnb.org/v1"


# Helpers
def status(url):
    return requests.get(url).status_code

def server_header(url):
    return requests.get(url).headers.get('server')


# Execution
jid = multyvac.submit(status, "https://developer.rackspace.com")
print(multyvac.get(jid).get_result())
