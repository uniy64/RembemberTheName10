#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 21:13:11 2017
First version Tributed to Python For Engineers
@author: Guangyu
"""

import praw
import pdb
import re
import os

happy_rooney=['Hi rio do u want picking up in the morning pal',              
              'Mr. bean. Funny',
              'At safari park yesterday with kai. A nonkey has stole my back window wiper. Cheeky monkey.',
              'Anyone recommend any good hair gel. Haha'
              'Chicha chicha chicha.'
              ]

angry_rooney=['I''ll put u asleep within 10 seconds u little girl. Don''t say stuff and not follow up on it. I''ll be waiting',
              'shut up u egg and get out of cowells hole.',
              'Won''t tell u again.',
              'Pepe. What an idiot. Sometimes people wind u up.'
              ]
silly_rooney=['Going to sleep guys gonna count 19 sheep to help me sleep. #whenwasurlastleaguewasibornohyeahbarley',
              'Leg',
              'Mate mate mate mate mate.',
              'Whitney has passed away. RIP u will live on foever. Cant believe it. I wanna run to u. Really cant believe this. @',
              'Linekar tell them the full message what i said.',
              ]

ironic_rooney=['Trying to watch super bowl final. How do they call this football. Like watching paint dry. Looking forward to adverts and music.',
               'get ur head on the game and stop tweeting',
               'A scouser knocks Liverpool of there perch. Haha. An evertoniian aswell. Yes. People. U can''t imagine how happy I am tonight. Believe',
               'Thx. Looks like 1992. Man utd. Arsenal. Chelsea. Blackburn only 4 teams won it. Wow. I thought liverpool had won it ?',
               'Hello @piersmorgan',
               'by the way i know how to spell arsenal. But arseanal sounds better.',
               'Drogba. Your a good player but pls get up.']

#create reddit instance
reddit=praw.Reddit('bot1',user_agent='RooneyTwitter v0.1')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to=[]
else:
    with open("posts_replied_to.txt","r") as f:
        posts_replied_to=f.read()
        posts_replied_to=posts_replied_to.split("\n")
        posts_replied_to=list(filter(None,posts_replied_to))
subreddit=reddit.subreddit('pythonforengineers')

for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("piers morgan",submission.title, re.IGNORECASE):
            submission.reply(angry_rooney[1])
            #submission.reply("Mr. "+ submission.author.name+" Funny")
            #submission.reply("Hi u want picking up in the morning pal")
            print("Bot replying to : ", submission.title)
            
            
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt",'w') as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
        