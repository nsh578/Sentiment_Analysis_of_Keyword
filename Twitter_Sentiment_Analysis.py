# sentiment analysis about a topic using data of twitter tweets of the topic
# we tokenize text inputs and count number of times a word shows up (Bag of Words model)
# get sentiment value from sentiment lexicon

# API keys will authenticate me with twitter

import tweepy
from textblob import TextBlob

consumer_key = 'zWY0TJSy3VYZARGBs55te6IUP'
consumer_secret = 'Yvg5EeCuqz3IVZZdYLesr5PFfazKFD9PZvazZ5iVoo0mrPdt9L'

access_token = '1037574877631328256-elfBCzUo8oq2upDjB8rpivPoDLDm6i'
access_token_secret = 'tMeWqMSWc3XJM0MLWDNu6B3jOTfreDtE5XLmjQGm72nAl'

#logging in
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#can create tweets, delete tweets, find twitter users, etc using api methods
api = tweepy.API(auth)

public_tweets = api.search('guns')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
	print('')
