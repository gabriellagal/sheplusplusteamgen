#!/usr/bin/python2.7

import tweepy

from common import Shuffler, load_config

def get_api(cfg):
	auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
	auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
	return tweepy.API(auth)

def main():
	# Fill in the values noted in previous step here
	cfg = load_config()
	api = get_api(cfg)
	shuffler = Shuffler()
	tweet = "Here's a team name suggestion" + shuffler.shuffle()
	status = api.update_status(status = tweet) 
	# Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
	main()





