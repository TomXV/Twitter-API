# coding: UTF-8

import json

print("Write mode\n")
A = input("CONSUMER_KEY: ")
B = input("CONSUMER_SECRET: ")
C = input("ACCESS_TOKEN: ")
D = input("ACCESS_TOKEN_SECRET: ")

CONSUMER_KEY = A
CONSUMER_SECRET = B
ACCESS_TOKEN = C
ACCESS_TOKEN_SECRET = D

API_DATA = {
"APIs":{
        "CONSUMER_KEY":CONSUMER_KEY,
        "CONSUMER_SECRET":CONSUMER_SECRET,
        "ACCESS_TOKEN":ACCESS_TOKEN,
        "ACCESS_TOKEN_SECRET":ACCESS_TOKEN_SECRET,
    }
}

with open('API.json', 'w') as f:
    json_dump = json.dump(API_DATA, f, ensure_ascii=False, indent=4)

print("\n"+"done!")
