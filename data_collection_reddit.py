import praw
import json
import csv
import pandas as pd
#authenication
reddit = praw.Reddit(
client_id = 'QRPUsdVY1VjByw',
client_secret = 'Tml0McbtcqBOio8ZJfVO7_UZd5I',
password = 'superman',
user_agent = 'classifier by /u/mmonsterbasher',
username = 'mmonsterbasher'
)

def get_non_depressed_data_set(subreddits):
    subreddits = list(map(reddit.subreddit, subreddits))
    comments = []
    for subreddit in subreddits:
        for submission in subreddit.hot(limit=1000):
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                with open("non_depressed_comments.csv",'w',encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([comment.body])
                print(comment.body)
    
                    
      

def get_depressed_data_set(subreddits):
    subreddits = list(map(reddit.subreddit, subreddits))
    comments = []
    for subreddit in subreddits:
        for submission in subreddit.hot(limit=400):
            submission.comments.replace_more(limit=None)
            comments.append(submission.comments.list())
            
    with open("depressed_comments.csv",'w',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for comment in comments:
                for c in comment:
                    writer.writerow([c.body])
                    
get_non_depressed_data(["news","lifeprotips","frugal","relationships","askreddit"])            

