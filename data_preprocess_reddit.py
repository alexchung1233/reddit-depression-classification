import praw
import pandas as pd
comments = []
dataframe = pd.read_csv("depressed_comments.csv",sep = ",")
print(dataframe)
