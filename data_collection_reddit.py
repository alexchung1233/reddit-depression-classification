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

def get_non_depressed_data_set(subreddits, num_comments):
    subreddits = list(map(reddit.subreddit, subreddits))
    comments = []
    for subreddit in subreddits:
        comments += list(subreddit.comments(limit=num_comments/len(subreddits)))
    with open('non_depression_data_set.csv','w') as file:
        writer = csv.writer(file)
        for comment in comments:
            writer.writerow([comment.body])

def get_depressed_data_set(subreddits, num_comments):
    subreddits = list(map(reddit.subreddit, subreddits))
    comments = []
    for subreddit in subreddits:
        comments += list(subreddit.comments(limit=num_comments/len(subreddits)))
    with open('depression_data_set.csv','w') as file:
        writer = csv.writer(file)
        for comment in comments:
            writer.writerow([comment.body])

get_depressed_data_set(["depression","suicidewatch"],10000)
get_non_depressed_data_set(["news","askreddit","food","pics"],10000)
