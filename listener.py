#!/usr/bin/python2.7

import json
import re
import tweepy # pip install tweepy
from common import Shuffler, load_config
 
config = None

class ListenerImpl(tweepy.StreamListener):
	
	def __init__(self, api):
		self.api = api
		self.shuffler = Shuffler()

	def on_status(self, status):
		if status.user.screen_name == 'ShePlusPlusTeam':
			print 'Stop tweeting yourself plz'
			return

		print 'Responding to ' + status.user.screen_name
		text = 'I don\'t know what you want @' + status.user.screen_name + ' :('

		tokens = re.findall(r'\w+', status.text.lower())
	
		shuffler = Shuffler()
	
		if 'team' in tokens and 'name' in tokens:
			text = 'You should call your team ' + self.shuffler.shuffle() +' @' + status.user.screen_name
		try:
			self.api.update_status(text, status.id)
		except Exception, e:
			print 'Twitter error :(', e

	def on_error(self, status_code):
		print 'Tweepy failure :(', status_code
		if status_code == 420:
			return

class Listener(object):

	def __init__(self):
		self.config = load_config()
	
	def listen(self, term = '@ShePlusPlusTeam'):
		auth = tweepy.OAuthHandler(self.config['consumer_key'], self.config['consumer_secret'])
		auth.set_access_token(self.config['access_token'], self.config['access_token_secret'])
		api = tweepy.API(auth)
		listener = ListenerImpl(api)
		stream = tweepy.Stream(auth = api.auth, listener=listener)

		print 'Listening'
		stream.filter(track=['@ShePlusPlusTeam'])
		print 'Closing'

def main():
	listener = Listener()
	listener.listen()

if __name__ == '__main__':
	main()
