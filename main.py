import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from tweepy import OAuthHandler
import tweepy as twp
import datetime
# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "  " 
consumer_secret = "  "
access_key = "  "
access_secret = "  "
  
# Function to extract tweets 
def connect_tweepy(ck,cs,ack,acs): 
          
    # Authorization to consumer key and consumer secret 
    auth = tweepy.OAuthHandler(ck, cs) 

    # Access to user's access key and access secret 
    auth.set_access_token(ack, acs) 

    # Calling api 
    api = tweepy.API(auth) 
  
    return api 

api=connect_tweepy(consumer_key,consumer_secret,access_key,access_secret)
#fetch tweet
def fetch_tweet(search_words,date_since,records):
    tweets = twp.Cursor(api.search,
                  q=search_words,
                  lang="en",
                  since=date_since).items(records)
    return tweets
    tweets=fetch_tweet('#kanyewest','2020-11-05',60)
    tweet_text_list=[]
tweet_date_list=[]
tweet_location_list=[]

for tweet in tweets:
    tweet_text_list.append(tweet.text)
    tweet_date_list.append(tweet.created_at)
    tweet_location_list.append(tweet.user.location)
    data = {'Tweets':tweet_text_list, 'Date':tweet_date_list,'Location':tweet_location_list}
tweet_df=pd.DataFrame.from_dict(data)
tweet_df.to_csv('tweet.csv') 
