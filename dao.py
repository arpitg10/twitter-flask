import os
import requests

# Fetching bearer token
bearer_token = os.environ.get("BEARER_TOKEN")
if not bearer_token:
    bearer_token = ""


def bearer_auth():
    auth = {'Authorization': f'Bearer {bearer_token}'}
    return auth


def get_twitter_response(url, params={}):
    response = requests.get(url, headers=bearer_auth(), params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()
