from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    query = StringField('query', validators=[DataRequired(), Length(min=2, max =50)])
    submit = SubmitField('Search')

import folium
import shutil,os

def maper1(x,y,text):

    map1=folium.Map(location=[1,1],zoom_start=1,tiles='Stamen Terrain')

    fg = folium.FeatureGroup('Tweets')

    for i in range(len(x)):
        fg.add_child(folium.Marker(loation = [x[i],y[i]],popup = (folium.Popup(text[i]))))

    map1.add_child(fg)

    map1.save(outfile = 'map1.html')
    shutil.copy('map1.html','/templates')

import tweepy
from datetime import datetime, date, time, timedelta


searched_tweets = []

def tweet_search(query):
    api = get_api()
    x = []
    y=[]
    text =[]

    searched_tweets = []
    max_tweets = 1000
    while len(searched_tweets) < max_tweets:
        remaining_tweets = max_tweets - len(searched_tweets)
        new_tweets = api.search(q=query, count=remaining_tweets)
        print('found',len(new_tweets),'tweets')
        if not new_tweets:
            print('no tweets found')
            break
        searched_tweets.extend(new_tweets)

    for tweet in searched_tweets:
        if tweet.coordinates is not None:
            x.append(tweet.coordinates[0])
            y.append(tweet.coordinates[1])
            text.append(tweet.text)



    maper.maper1(x, y, text)


def get_api():
    consumer_key = '6gSZ5GDRI97IFLW0qctBvICeP'
    consumer_secret = 'ybCcMEgL56RNoZHRM51nP4jAF8xrZeyjGUc7beODQkqAeHskMp'

    access_token = '2429275932-SjwISH2T0mBjFiyNEITBYLXiAyg8fOyCWaG7Zr6'
    access_token_secret = 'QjUndYKfNtE5R2iker1ouFeNrEkk9iqwfmAwrDB86a27N'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return tweepy.API(auth)

from flask import Flask, render_template, redirect, url_for
import requests
import json
import unicodedata
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search', name=form.query.data))
    return render_template('search.html', form=form)

@app.route('/search/<name>')
def search(name):
    info = name
    tweet_search(info)
    return render_template('map.html')

@app.route('/hello/<name>')
def hello(name):
    info = requests.get['query']
    return info.text

if __name__ == '__main__':
    app.run(debug=True)
