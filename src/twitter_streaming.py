#Imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables
access_token = "Enter your access token"
access_token_secret = "Enter your access token secret"
consumer_key = "Enter your api key"
consumer_secret = "Enter your api secret"

#Basic listener that prints received tweets to stdout
class StdOutListener (StreamListener):
    def on_data (self, data):
        print (data)
        return True

    def on_error (self, status):
        print (status)

if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track = ['python', 'javascript', 'ruby'])
