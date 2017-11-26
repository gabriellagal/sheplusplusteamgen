import random
import json
from random import shuffle

def load_config(path = './config.json'):
	with open(path, 'r') as f:
		return json.loads(f.read())

def normalise(word):
	word = word.rstrip('\n')
	word = word[0].upper() + word[1:]
	return word

def load_words(fn):
	with open(fn, mode="r") as f:
		return [normalise(word) for word in f]

class Shuffler(object):

	def __init__(self):
		self.sections = [load_words("data/" + fn) for fn in ["adjective.txt", "noun.txt", "team.txt"]]

	def shuffle(self):
		return ' '.join([random.choice(words) for words in self.sections])
