# coding: UTF-8

import json
from requests_oauthlib import OAuth1Session

#ここにKeyとToken
CONSUMER_KEY =''
CONSUMER_SECRET =''
ACCESS_TOKEN =''
ACCESS_TOKEN_SECRET =''

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

url = "https://api.twitter.com/1.1/statuses/update.json"

input_tweet = input("What do you want tweet?: ")
tweet = input_tweet #ツイート内容

import os
os.system("cls")

print(input_tweet + '\n')
print("Is it okay if I tweet this?\n")
input_tweet_check = str(input("Y type to 1/N type to 0: "))

params = {"status" : tweet}

if input_tweet_check.lower() == "y" or input_tweet_check.lower() == "1":
    req = twitter.post(url, params = params) #ここでツイート
    if req.status_code == 200: #成功
          print("Succeed!")
    else: #エラー
          print("ERROR : %d"% req.status_code) 
else:
    print("tweet canceled")
    exit()
