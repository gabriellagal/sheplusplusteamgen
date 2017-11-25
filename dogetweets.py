import tweepy
import random
from random import shuffle

def shuffleadj():
    with open("adjective.txt", mode="r") as adjmix:
      words = []
      for word in adjmix:
        words.append(word.rstrip('\n'))
      return random.choice(words) 

def shufflenoun():
    with open("noun.txt", mode="r") as nounmix:
      words = []
      for word in nounmix:
        words.append(word.rstrip('\n'))
      return random.choice(words) 

def shuffleteam():
    with open("team.txt".rstrip(), mode="r") as teammix:
      words = []
      for word in teammix:
        words.append(word)
      return random.choice(words) 





def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "FxTN3P2LTXwv2yV0x7i2biEQb",
    "consumer_secret"     : "qy9ovcHsOnnIrfsNUGvo3hrWUt0NybzZ6zMgdaRsRVEpwQ6sry",
    "access_token"        : "934377774713856000-X6F11aI90IbKhBUqMe40sHDmPu3C5ec",
    "access_token_secret" : "H4mhxOVm9AGruXCkNga5O7I5UhgB7dmbBTe2tyxtSQFva" 
    }

  api = get_api(cfg)
  tweet = "New team name: " + shuffleadj() + ' ' + shufflenoun() + ' ' + shuffleteam()
  status = api.update_status(status = tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()





