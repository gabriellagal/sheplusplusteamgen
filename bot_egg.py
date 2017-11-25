import os
from markovbot import MarkovBot 

tweetbot = ShePlusBot()

dirname = os.path.dirname(os.path.abspath("C:/Python27/ShePlusBot/test.txt"))
book = os.path.join(dirname, 'test.txt')
tweetbot.read(book)

test_number_1 = tweetbot.generate_text(20, seedword =['a'])
print("tweetbot says:")
print(test_number_1)

cons_key = ''
cons_secret = ''
access_token = '-'
access_token_secret = ''

tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=1, keywords=None, prefix=None, suffix='#PyGaze')
