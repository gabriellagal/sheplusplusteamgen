#!/usr/bin/python2.7

import json
import tweepy # pip install tweepy

config = None

class ListenerImpl(tweepy.StreamListener):
	
	def __init__(self, api):
		self.api = api

	def on_status(self, status):
		print 'Responding to ' + status.user.screen_name
		text = 'I don\'t know what you want @' + status.user.screen_name + ' :('
		self.api.update_status(text)

class Listener(object):

	def __init__(self, path = '/root/python/sheplusplusteamgen/config.json'):
		with open(path, 'r') as f:
			data = f.read()
			self.config = json.loads(data)
	
	def listen(self, term = '@ShePlusPlusTeam'):
		auth = tweepy.OAuthHandler(self.config['consumer_key'], self.config['consumer_secret'])
		auth.set_access_token(self.config['access_token'], self.config['access_token_secret'])
		api = tweepy.API(auth)
		listener = ListenerImpl(api)
		stream = tweepy.Stream(auth = api.auth, listener=listener)

		print 'Listening'
		stream.filter(track=['@ShePlusPlusTeam'])
		

def main():
	listener = Listener()
	listener.listen()

if __name__ == '__main__':
	main()
