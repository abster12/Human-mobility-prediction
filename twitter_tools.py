import tweepy
from datetime import datetime, date, time, timedelta

searched_tweets = []

def tweet_search(query):
    api = get_api()

    searched_tweets = []
    max_tweets = 1500
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
        new_tweets = api.search(q=query, count=remaining_tweets)
        print('found',len(new_tweets),'tweets')
        if not new_tweets:
            print('no tweets found')
            break
        searched_tweets.extend(new_tweets)

    return searched_tweets

def get_api():
    consumer_key = '6gSZ5GDRI97IFLW0qctBvICeP'
    consumer_secret = 'ybCcMEgL56RNoZHRM51nP4jAF8xrZeyjGUc7beODQkqAeHskMp'

    access_token = '2429275932-SjwISH2T0mBjFiyNEITBYLXiAyg8fOyCWaG7Zr6'
    access_token_secret = 'QjUndYKfNtE5R2iker1ouFeNrEkk9iqwfmAwrDB86a27N'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)
