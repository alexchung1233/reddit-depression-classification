import praw
import json
import csv
#authenication
reddit = praw.Reddit(
client_id = 'QRPUsdVY1VjByw',
client_secret = 'Tml0McbtcqBOio8ZJfVO7_UZd5I',
password = 'superman',
user_agent = 'classifier by /u/mmonsterbasher',
username = 'mmonsterbasher'
)

depression = reddit.subreddit('depression')
comments = []
for submission in depression.hot(limit=20):
    submission.comments.replace_more(limit=0)
    comments.append(submission.comments.list())
with open("depressed_comments.csv",'w') as csvfile:
    writer = csv.writer(csvfile)
    for comment in comments:
        for c in comment:
            writer.writerow([c.body])
            print(c.body)
