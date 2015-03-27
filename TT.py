#!/usr/bin/python
# get trending tweets from your place and display :-)
import pynotify
from tweepy import OAuthHandler
from tweepy import API
from time import sleep

ckey = 'vgncvkeqd8fLo0K64HCl2kOnV'
csecret = ''
a_secret = ''
a_token = '146477450-EwAJu8YkY0Ry9awihuP83oZyAwANzdLpvr18RuAT'


auth = OAuthHandler(ckey,csecret);
auth.set_access_token(a_token,a_secret);
api = API(auth);
def findtrending():
    global auth
    global api
    trends = api.trends_place(1)
    vals = [];
    for each in trends[0]['trends']:
        vals.append(each['name']);


    pynotify.init("TrendsNowUbuntu")
    for each in vals:
        n = pynotify.Notification("TrendingNow",
          each
        );
        n.show();

findtrending()


