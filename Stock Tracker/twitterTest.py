import requests
import os
import json
from datetime import datetime, timedelta
import pytz
from pyrfc3339 import generate, parse

def auth():
    return 'AAAAAAAAAAAAAAAAAAAAAC2oGwEAAAAANe6sIQ%2Bpy%2F34oVdXB5DA8I4xcG4%3DvojzwDscZh0Wu7ds214h99nHBQqyDHxZMed7KKlyVrJrO3pxbe'


def create_url():
    query = "TCDA"
    results = 100

    d = datetime.utcnow() - timedelta(hours=16)
    start = d.isoformat("T") + "Z"


    url = "https://api.twitter.com/2/tweets/search/recent?query={}&max_results={}&start_time={}".format(
        query, results, start
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    bearer_token = auth()
    url = create_url()
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    
    twit_list = []
    twit_data = json_response
    for i in twit_data['data']:
        twit_list.append(i)

    print(len(twit_list))


if __name__ == "__main__":
    main()