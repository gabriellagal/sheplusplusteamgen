import os
from markovbot import MarkovBot 

tweetbot = ShePlusBot()

dirname = os.path.dirname(os.path.abspath("C:/Python27/ShePlusBot/test.txt"))
book = os.path.join(dirname, 'test.txt')
tweetbot.read(book)

test_number_1 = tweetbot.generate_text(20, seedword =['a'])
print("tweetbot says:")
print(test_number_1)

cons_key = 'FxTN3P2LTXwv2yV0x7i2biEQb'
cons_secret = 'qy9ovcHsOnnIrfsNUGvo3hrWUt0NybzZ6zMgdaRsRVEpwQ6sry'
access_token = '934377774713856000-X6F11aI90IbKhBUqMe40sHDmPu3C5ec'
access_token_secret = 'H4mhxOVm9AGruXCkNga5O7I5UhgB7dmbBTe2tyxtSQFva'

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=1, keywords=None, prefix=None, suffix='#PyGaze')
