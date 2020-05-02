# coding: UTF-8

import json

with open('API.json', 'r') as f:
    json_load = json.load(f)

CONSUMER_KEY = json_load["APIs"]["CONSUMER_KEY"]
CONSUMER_SECRET = json_load["APIs"]["CONSUMER_SECRET"]
ACCESS_TOKEN = json_load["APIs"]["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = json_load["APIs"]["ACCESS_TOKEN_SECRET"]

print("CONSUMER_KEY:", CONSUMER_KEY)
print("CONSUMER_SECRET:", CONSUMER_SECRET)
print("ACCESS_TOKEN:", ACCESS_TOKEN)
print("ACCESS_TOKEN_SECRET", ACCESS_TOKEN_SECRET)