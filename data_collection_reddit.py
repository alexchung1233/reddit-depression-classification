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
            for comment in praw.helpers.flatten_tree(submission.comments):
                with open("non_depressed_comments.csv",'w',encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([comment.body])
                print(comment.body)
    
                    
      

def get_depressed_data_set(subreddits):
    subreddits = list(map(reddit.subreddit, subreddits))
    comments = []
    for subreddit in subreddits:
        for submission in subreddit.hot(limit=1000):
            submission.comments.replace_more(limit=None)
            for comment in praw.helpers.flatten_tree(submission.comments):
                with open("non_depressed_comments.csv",'w',encoding='utf-8') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([comment.body])
                print(comment.body)
                    
get_non_depressed_data(["news","lifeprotips","frugal","relationships","askreddit"])            
get_depressed_data(["depression","suicidewatch","mentalhealth","bipolar","depressed","anxiety"])  
