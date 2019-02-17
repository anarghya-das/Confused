import json
import random 
import bot
from flask import current_app


def tweetTweet():
    with current_app.open_resource("{{url_for('static',filename='pic.png')}}",'r') as f:
        js=f.read()

    ob=json.loads(js)
    arr=ob['recipes']
    finalArr=[]
    for o in arr:
        finalArr.append(o['name'])

    idx=random.randint(0,1914)
    bot.tweet(finalArr[idx])