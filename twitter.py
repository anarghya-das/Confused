import json
import random 
import bot
with open('cache.json','r') as f:
    js=f.read()

ob=json.loads(js)
arr=ob['recipes']
finalArr=[]
for o in arr:
    finalArr.append(o['name'])

idx=random.randint(0,1914)
bot.tweet(finalArr[idx])