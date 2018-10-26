from flask import Flask, render_template, redirect, url_for
from forms import SearchForm
import requests
import json
import unicodedata
import twitter_tools as tt
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'

@app.route('/search', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search', name=form.query.data))
    return render_template('search.html', form=form)

@app.route('/search/<name>')
def search(name):
    info = name
    tt.tweet_search(info)
    return render_template('map.html')

@app.route('/hello/<name>')
def hello(name):
    info = requests.get['query']
    return info.text

if __name__ == '__main__':
    app.run(debug=True)
