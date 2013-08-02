#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import re
import time
import json
from datetime import datetime,timedelta
from operator import itemgetter

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
    def filter(self,text,user):
        return (re.search(u'バルス',text)
                and len(text)<=5
                and user not in map(itemgetter(1), self._related))
    def tweet(self):
        if not self._done:
            try:
                self._api.update_status('バルス！')
                time.sleep(3)
                self._api.update_status('（これは自動ツイートです）')
                self._done=True
            except:
                pass
    def on_error(self,status):
        print status
    def on_data(self,data):
        d=json.loads(data)
        if d.has_key('text'):
            text=d['text']
            user=d['user']['screen_name']
            try:
                date=datetime.strptime(d['created_at'],self._format)
            except:
                return True
            if self.filter(text,user):
                self._related.append((date,user,text))
            while len(self._related)>0 and self._related[0][0]<date-self._timewidth:
                del self._related[0]
            if len(self._related)>=THRESHOLD:
                self.tweet()
            print user,text
        return True

def main():
    auth=getAuth(KEYFILE)
    stream=tweepy.Stream(auth,listener=Listener(auth))
    stream.userstream()

if __name__=='__main__':
    main()
