import random
from datetime import datetime
from dictionary import Words

#initializes the dictionary so that we can use the words
words = Words();
#makes the random number generator more random
random.seed(datetime.now)

#gets 3 random numbers between 0 and the length of each list of words
random1 = random.randint(0, 3000) % (len(words.plural_nouns))
random2 = random.randint(0, 3000) % (len(words.plural_verbs))
random3 = random.randint(0, 3000) % (len(words.plural_nouns))

#gets the n-th word from the list of words
#where n is the randomly chosen number above
noun1 = words.plural_nouns[random1]
verb1 = words.plural_verbs[random2]
noun2 = words.plural_nouns[random3]

#prints out each of the randomly chosen words with spaces between them
print noun1 + " " + verb1 + " " + noun2
