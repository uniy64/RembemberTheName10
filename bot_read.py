#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:34:39 2017
First version tributed to Python For Engineer
@author: Guangyu
"""

import praw

reddit=praw.Reddit('bot1',user_agent='RooneyTwitter v0.1')
#print(reddit.user.me())

#Use this subreddit for testing
subreddit=reddit.subreddit('pythonforengineers')

#read top 5 hot sumbissions
for submission in subreddit.hot(limit=3):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

    
