import tweepy
#Ques1 Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
#An access_token is a unique string of letters and numbers that you pass with every API call, so
# WePay knows you are authorized to make that call.

#Each access_token is associated with:
#   1.Your API application.
#   2.The user you are acting on behalf of (for merchants, this is yourself).
#   3.The permissions your app has for that user.

#access_token='1006749734667804672-Ph2jaNXdvhEBo5yq7pJE57PmKSFBiN'

#Ques2 Get the IP address of some common sites like Google, Facebook by using DNS lookup.

'''C:\Users\Anjali>nslookup yahoo.com
Server:  UnKnown
Address:  fd00:0:6:5::7

Non-authoritative answer:
Name:    yahoo.com
Addresses:  2001:4998:c:1023::4
          2001:4998:58:1836::11
          2001:4998:58:1836::10
          2001:4998:44:41d::4
          2001:4998:c:1023::5
          2001:4998:44:41d::3
          98.137.246.7
          98.138.219.232
          72.30.35.10
          98.137.246.8
          98.138.219.231
          72.30.35.9


C:\Users\Anjali>nslookup google.com
Server:  UnKnown
Address:  fd00:0:6:5::7

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4007:809::200e
          172.217.31.206'''

#Ques 3 Using Tweepy library try to extract tweets from Twitter.
consumer_key='rWy3JbTpXYyAvMFgsg0VjrEDb'
consumer_secret = 'otlz7qXPH9KkxzDRnNh1YcrpbaEqfRPYsnNXEEmdW9Y8RxyBXi'
access_token='1006749734667804672-Ph2jaNXdvhEBo5yq7pJE57PmKSFBiN'
access_token_secret='CyAPoP8KQgW7T4WDO4xqLwmuNFME3KGCgaKV0Y4cThqQz'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

tweets = api.search('#NotWithoutMyDog',lang="en",count=10,tweet_mode="extended")
print(tweets)
for tweet in tweets:
    print('--------------------------')
    print(tweet.full_text)
    print('---------------------------\n')

#Ques4 What is a difference between library and API . Figure it out with examples.
'''API is a part of library which defines how an application communicates with external code
.
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices,
 along with a large collection of high-level mathematical functions to operate on these arrays.'''

#Ques5 Try to access Spotify API . Find out some library for it and play some music.
#pip install pyspotify==1.2
import soundcloud

# create a client object with access token
client = soundcloud.Client(access_token='1006749734667804672-Ph2jaNXdvhEBo5yq7pJE57PmKSFBiN')

# create an array of track ids
tracks = map(lambda id: dict(id=id), [290, 291, 292])

# get playlist
playlist = client.get('/me/playlists')[0]

# add tracks to playlist
client.put(playlist.uri, playlist={
    'tracks': tracks
})

