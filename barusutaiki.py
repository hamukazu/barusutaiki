#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import re
import time
import json
from datetime import datetime,timedelta

KEYFILE='keys'
THRESHOLD=4
TIMEWIDTH=10

def getAuth(key):
    keys={}
    for l in open(key):
        ll=re.sub('#.*','',l)
        a=ll.split(':')
        if len(a)>=2:
            keys[a[0].strip().lower()]=a[1].strip()
    auth=tweepy.OAuthHandler(keys['consumer_key'],keys['consumer_secret'])
    auth.set_access_token(keys['access_token'],keys['access_token_secret'])
    return auth

class Listener(tweepy.StreamListener):
    def __init__(self,auth):
        self._related=[]
        self._format='%a %b %d %H:%M:%S +0000 %Y'
        self._auth=auth
        self._api=tweepy.API(auth)
        self._timewidth=timedelta(seconds=TIMEWIDTH)
        self._done=False
    def filter(self,s):
        return re.search(u'バルス',s) and len(s)<=5
    def tweet(self):
        if not self._done:
            self._api.update_status('バルス！')
            time.sleep(3)
            self._api.update_status('（これは自動ツイートです）')
            self._done=True
    def on_error(self,status):
        print status
    def on_data(self,data):
        d=json.loads(data)
        if d.has_key('text'):
            text=d['text']
            date=datetime.strptime(d['created_at'],self._format)
            if self.filter(text):
                self._related.append((date,text))
            if len(self._related)>0:
                while self._related[0][0]<date-self._timewidth:
                    del self._related[0]
            if len(self._related)>=THRESHOLD:
                self.tweet()
            print text

def main():
    auth=getAuth(KEYFILE)
    stream=tweepy.Stream(auth,listener=Listener(auth))
    stream.userstream()

if __name__=='__main__':
    main()
