#!/usr/bin/python2.7

import json
import tweepy # pip install tweepy

config = None

class FollowListener(tweepy.StreamListener):
	
	def __init__(self, api):
		self.api = api

	def on_status(self, status):
		print 'Responding to ' + status.user.screen_name
		text = 'I don\'t know what you want @' + status.user.screen_name + ' :('
		self.api.update_status(text)

def main():
	global config
	
	with open('/root/python/sheplusplusteamgen/config.json', 'r') as f:
		data = f.read()
		config = json.loads(data)
	
	auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
	auth.set_access_token(config['access_token'], config['access_token_secret'])
	api = tweepy.API(auth)
	listener = FollowListener(api)
	stream = tweepy.Stream(auth = api.auth, listener=listener)

	print 'Listening'
	stream.filter(track=['@ShePlusPlusTeam'])

main()
