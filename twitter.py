import requests
import json
import random 
import bot

def tweetTweet():
    headers = {
        # Request headers
        'Subscription-Key': '3a5f419cd2b04164933ee603e990b8ff',
    }

    r = requests.get('https://api.wegmans.io/meals/recipes?api-version=2018-10-18', params=headers)

    obj=json.loads(r.content)
    arr=obj['recipes']
    finalArr=[] 
    for o in arr:
        finalArr.append(o['name'])
    idx=random.randint(0,1914)
    bot.tweet(finalArr[idx])
    return "sucess"
