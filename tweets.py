#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
from tweepy.error import TweepError 
from secrets import *
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = C_KEY
CONSUMER_SECRET = C_SECRET 
ACCESS_KEY = A_KEY 
ACCESS_SECRET =  A_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
for follower in tweepy.Cursor(api.followers).items():
    try:
        follower.follow()
    except TweepError:
        continue

filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    try:
        api.update_status(status=line)
    except TweepError:
        continue
    time.sleep(300)#Tweet every 15 minutes

