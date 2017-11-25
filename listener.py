#!/usr/bin/python2.7

import json
import re
import tweepy # pip install tweepy

config = None

class ListenerImpl(tweepy.StreamListener):
	
	def __init__(self, api):
		self.api = api

	def on_status(self, status):
		if status.user.screen_name == 'ShePlusPlusTeam':
			print 'Stop tweeting yourself plz'
			return

		print 'Responding to ' + status.user.screen_name
		text = 'I don\'t know what you want @' + status.user.screen_name + ' :('

		tokens = re.findall(r'\w+', status.text.lower())
		
		if 'team' in tokens and 'name' in tokens:
			text = 'I can\'t generate team names just yet @' + status.user.screen_name
		try:
			self.api.update_status(text, status.id)
		except Exception, e:
			print 'Twitter error :(', e 

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
