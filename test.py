import tweepy
from textblob import TextBlob

consumer_key = 'EjXTChxrOmEWULyuuJ8iDXdyQ'
consumer_secret = 'NrtHvELXi0i6dtue39icLkrT3rrrUVHKWOlHWWGJm46LQGell5'

access_token = '1425159876-T5yoGiyxFk2sAdsZNjGVLRa94988APPcV4TI7R6'
access_token_secret = 'JsCnvZPbnn93qefEM187dPnUcdCn5pby220IiU3D1aKam'

auth =tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
query = raw_input("Type the query .\n")
#print(query)

public_tweets = api.search(query)

for tweet in public_tweets:
    print('------------------------------------------------------------------')
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('------------------------------------------------------------------')
