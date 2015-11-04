import os

base_url = 'https://127.0.0.1:5000'
users_url = '/api/users'
token_url = '/api/token'
certificate_crt_file = '/server.crt'
certificate_key_file = '/server.key'
basedir = os.path.abspath(os.path.dirname(__file__))
json_header = {'Content-Type': 'application/json'}