# Human-mobility-projector

Twitter has been an active source of data collection for the past few years. The location that is provided with the tweet is of great help when it comes to situations like natural disasters. Using the longtitude and latitude from the tweets we pin-point the location on the map as  either a safe location or the location of the victims. Using all the collected data during that disaster we get all the points where the tweets came from and then try to impose that data on a map to see either the safe locations, which help in predicting the type of terrain and quality of infrastructure present at that location to be marked as safe during a disaster, or help the rescue teams in co-ordinating the rescue operations. 

The idea is to combine all these data and make a predictive model which will make use of this data and then produce the most likely locations where people could be found. The people there may be unharmed because of the safe terrain or robust infrastructure.
This will help the rescue teams to collect all the people and help in recovery.

### Dataset

[Kaggle Dataset](https://www.kaggle.com/dryad/human-mobility-during-natural-disasters)

#### Review of work done

[Big Data in Natural Disaster Management: A Review](https://www.mdpi.com/2076-3263/8/5/165/pdf-vor)


### Running the web app

The webapp is made using flask and the maps are rendered using folium. This code is running fine on python 3.6 and does not run on python 3.7 due to incompatilibility of tweepy.

To the webapp clone this repository and use the Twitter api keys that you have recieved in the ```get_api()``` and if no please register an app [here](https://developer.twitter.com/en/apply-for-access) and obtain the keys.

Then enter 
```python application.py``` 
The web app will be live on a local server on ```/home``` .

For a better understanding of flask and how to use the twitter api for different types of searches please take a look at the article by [Dilan Coss](https://nearsoft.com/blog/how-to-create-an-api-and-web-applications-with-flask/)
