#!/usr/bin/python
#Gets Feed from the handle mentioned in the app.cfg file and uses ubuntu's notify system to create a notification

#I use it to get news and 


import pynotify
from tweepy import OAuthHandler
from tweepy import API
from time import sleep
import subprocess
from urllib import urlopen
import pickledb
import os
import re
import ConfigParser

configParser = ConfigParser.RawConfigParser()   
configFilePath = r'app.cfg'
configParser.read(configFilePath)

ckey = configParser.get('APP', 'consumerPublickey')
csecret = configParser.get('APP', 'consumerSecretkey')
a_token = configParser.get('APP', 'acessToken')
a_secret = configParser.get('APP', 'acessTokenSecret')

TEMPIMGPATH = configParser.get('PATH', 'tempdir')
screen_names = configParser.get('NEWS', 'screen_name')
screen_names = screen_names.split(',');
articles = configParser.get('NEWS', 'articles')
articles =  articles.split(',');
articles = [int(e) for e in articles];


print ckey
print csecret
print a_token
print a_secret


##
##ckey = 'vgncvkeqd8fLo0K64HCl2kOnV'
##csecret = '6J9S2yyX01zT5O1cYw3CTcjgTnTHdImhtfeWMXbomgjYCpaizk'
##a_token = '146477450-EwAJu8YkY0Ry9awihuP83oZyAwANzdLpvr18RuAT'
##a_secret = 'zLGb6OmYxelNQulfvM2kZItvp2VhLDiAqwhBDXQaL4fAx'
##TEMPIMGPATH = "/home/poochi/APP_tweetynews/pics"
##TEMPDATABASE = "/home/poochi/APP_tweetynews/tweetNews.db"


auth = OAuthHandler(ckey,csecret);
auth.set_access_token(a_token,a_secret);
api = API(auth);


def getnews(screen_name,postscount):
    
    new_tweets = api.user_timeline(screen_name = screen_name,count=postscount)
    d={};
    
    for each in new_tweets:
#        print each.profile_image_url_https
        
        d[each.id] = None;
        if "media" in each.entities.keys():        
            picurl = each.entities["media"][0];
            picurl = picurl["media_url"]            
            f = urlopen(picurl);            
            fname = os.path.join(TEMPIMGPATH,str(each.id)+'.jpg');
            print fname
            if os.path.isfile(fname) is False:
                print "New one"
                with open(fname, "wb") as imgFile:
                    imgFile.write(f.read())
            d[each.id] = fname;
            
            
#Show tweets with images only
    for each in new_tweets:        
        pynotify.init("TrendsNowUbuntu")
        x = each.text.encode("utf-8")
        text = ' '.join(re.sub("(@[A-Za-z0-9',]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",x).split())
        print text
        if d[each.id] is None:
            #No tweets withouth images
            n = pynotify.Notification(screen_name,text);
            continue;
        else:            
            n = pynotify.Notification(screen_name,text,d[each.id]);            
        n.show();    
    try:
        subprocess.Popen(["paplay", "/usr/share/sounds/ubuntu/stereo/message.ogg"])
    except:
        print "Unable to play sound"


#handles
print screen_names
for _s,_c in zip(screen_names,articles):
    
    getnews(_s,int(_c));
