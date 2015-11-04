import requests, json

from pybudget.client.config import base_url, users_url, basedir, certificate_crt_file, certificate_key_file, json_header

cert_files = (basedir + certificate_crt_file, basedir + certificate_key_file)


def register(username, password):
    data = json.dumps({'username': username, 'password': password})
    # TODO Add cert support
    request = requests.post(base_url + users_url, headers=json_header, data=data, verify=False)

    return request.json()