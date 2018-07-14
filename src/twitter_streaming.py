#Imports
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

#Variables
access_token = config['DEFAULT']['access_token']
access_token_secret = config['DEFAULT']['access_token_secret']
consumer_key = config['DEFAULT']['consumer_key']
consumer_secret = config['DEFAULT']['consumer_secret']

#Basic listener that prints received tweets to stdout
class StdOutListener (StreamListener):
    def on_data (self, data):
        print (data)
        return True

    def on_error (self, status):
        print (status)

if __name__ == '__main__':

    #Handles Twitter authentification and the connection to Twitter Streaming API
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    #Filters Twitter Stream to capture data by the keywords provided
    stream.filter(track = ['python', 'javascript', 'ruby'])
