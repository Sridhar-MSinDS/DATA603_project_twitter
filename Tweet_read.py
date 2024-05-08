
# Set up your credentials
consumer_key='9jRNIZ07ezhmkCn9CvEEqrdE4'
consumer_secret='UulpEQzkX8ji51wquf5kXJrjOXa0HMk5j7zTp4sFXSxkJsdY0j'
access_token ='1783702488266264576-SoEVqUTBmhf6kZnM5I8pwl41DbHlkZ'
access_secret='IdlhjD0QWWcoE5EUdc48ufgyaG4io5W1F6ATYo3cKSYWb'

import tweepy
print(tweepy.__version__)
from tweepy import OAuthHandler
from tweepy import StreamingClient
from tweepy import *
import socket
import json
class MyStreamListener(tweepy.StreamingClient):
	def On_tweet(self,tweet):
		print(tweet.text)

class TweetListener(tweepy.StreamingClient):
	def __init__(self,csocket):
		self.client_socket = csocket
		
	def on_data(self,data):
		try:
			msg= json.loads(data)
			printing(msg['text'].encode('utf-8'))
			self.client_socket.send(msg['text'].encode('utf-8'))
			return True
		except BaseException as e:
			print("Error",e)
		return True
	def on_error(self,status):
		print(status)
		return True
		
def sendData(c_socket):
	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_secret)
	twitter_stream = Stream(auth, TweetListener(c_socket))
	twitter_stream.filter(track=['guitar'])
	
if __name__ == '__main__':
	s = socket.socket()
	host = '127.0.0.1'
	port = 9996
	s.bind((host,port))
	print('listening on port 9996')
	s.listen(5)
	c,addr = s.accept()
	sendData(c)									
