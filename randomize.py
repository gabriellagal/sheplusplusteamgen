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
    		words.append(word.rstrip('\n')
    	return random.choice(words) 

def shuffle_all():
	return shuffleadj() + ' ' + shufflenoun() + ' ' + shuffleteam()
