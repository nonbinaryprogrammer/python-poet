import random
from datetime import datetime

#makes a list of words for us to choose from
words = ["tree", "stone", "forest", "rock", "codfish"]

#makes the random number generator random
random.seed(datetime.now)

#gets a random number between 0 and the length of the list of words
num = random.randint(0, 3000) % (len(words))
#prints the n-th word in the list
#where n is the randomly chosen number
print "Word 1: " + words[num];

#picks a second random number between 0 and the length of the list of words
num = random.randint(0, 3000) % (len(words))
#prints out the n-th word from the list
#where n is the randomly chosen number
print "Word 2: " + words[num];
