#Python Twitter bot for @OpNestle
#Made by Berzerker
#v1.0
 
import tweepy
import sys
import time
import random
 
#Start of authorization
consumer_key='EYByxIjRyfnsTRF1ZCNPhJYtn'
consumer_secret='lp0zPBGjHx3FExsYP80PRJfEKHQHp7ZV0hoGJYOwi3ZYrPttgX'
access_key='4749114708-1q9mvNLkyxbWfSnQjSDBznM0gEGChxcPyIgCzlV'
access_secret='	lhPyNc9SS2o2RcLkPHhsZoT8C3PokKDpoeGl6xWhvuuZg'
auth=tweepy.OAuthHandler(consumer_key, consumer_secret, secure=True)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth, secure=True)
#End of authorization
 
#Post tweets
while True:
     tweetCount=0
     tweetNum=random.randint(1,5)
     tweetList={
          "tweet1": "Support @OpNestle by retweeting our tweets",
          "tweet2": "Just a few more reasons to hate #Nestle bit.ly/1Out9fE #OpNestle #Anonymous",
          "tweet3": "Help fund this operation with #bitcoin 1Bszq5SjfBheQdRG8ExLrykv23vEEFCsT1",
          "tweet4": "Case against #Nestle using child labor http://bit.ly/1Ov8x6R",
          "tweet5": "Please boycott #Nestle #OpNestle #A Anonymous",
     }
     if tweetNum==1:
          tweetContent=tweetList["tweet1"]
          api.status_update(tweetContent)
          print("Tweet sent!")
          tweetCount=tweetCount+1
     elif tweetNum==2:
          tweetContent=tweetList["tweet2"]
          api.status_update(tweetContent)
          print("Tweet sent!")
          tweetCount=tweetCount+1
     elif tweetNum==3:
          tweetContent=tweetList["tweet3"]
          api.status_update(tweetContent)
          print("Tweet sent!")
          tweetCount=tweetCount+1
     elif tweetNum==4:
          tweetContent=tweetList["tweet4"]
          api.status_update(tweetContent)
          print("Tweet sent!")
          tweetCount=tweetCount+1
     elif tweetNum==5:
          tweetContent=tweetList["tweet5"]
          api.status_update(tweetContent)
          print("Tweet sent!")
          tweetCount=tweetCount+1
     time.sleep(300)
     print("Tweets sent: ",tweetCount)
