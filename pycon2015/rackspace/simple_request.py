import os
import multyvac
import requests


# rackspace configuration
multyvac.config.api_key = "cloudpipe18" # Rackspace Username
multyvac.config.api_secret_key = "683df297726d4bb18c6c230e5be795fe" # Rackspace API Key
multyvac.config.api_url = "https://cloudpipe.tmpnb.org/v1"


# helpers
def status(url):
    return requests.get(url).status_code

def server_header(url):
    return requests.get(url).headers.get('server')


# execution
jid = multyvac.submit(status, "https://developer.rackspace.com")
print(multyvac.get(jid).get_result())

# notes about execution
# multyvac.submit(some_lambda_f, _image="some_docker_image_in_which_launch_the_job")
