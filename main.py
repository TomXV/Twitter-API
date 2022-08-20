# coding: UTF-8

import json
from requests_oauthlib import OAuth1Session
from HTTP_STATUS_CODE import HTTP_STATUS_CODE

with open('API.json', 'r') as f:
    json_load = json.load(f)

#API.jsonのKeyとTokenの値を書き換えておいてください
CONSUMER_KEY = json_load["APIs"]["CONSUMER_KEY"]
CONSUMER_SECRET = json_load["APIs"]["CONSUMER_SECRET"]
ACCESS_TOKEN = json_load["APIs"]["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = json_load["APIs"]["ACCESS_TOKEN_SECRET"]
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

url = "https://api.twitter.com/2/tweets"
	
import os
os.system("cls")

input_tweet = input("What do you want tweet?: ")
tweet = input_tweet #ツイート内容

os.system("cls")
print(input_tweet + '\n')
print("Is it okay if I tweet this?\n")
input_tweet_check = str(input("Y type to 1/N type to 0: "))

params = {"text" : tweet}

if input_tweet_check.lower() == "y" or input_tweet_check.lower() == "1":
    req = twitter.post(url, json = params) #ここでツイート
    if req.status_code == 200 or 201: #成功
          HTTP_STATUS_CODE(req.status_code)
    else: #エラー
          print("ERROR : %d\n"% req.status_code)
          HTTP_STATUS_CODE(req.status_code)
else:
    print("tweet canceled")
    exit()

print('')
print('Response Json Data\n')
print(req.json())
