import random
from datetime import datetime

class Stanzas:
  def __init__(self):
    random.seed(datetime.now)

  def print_stanza(self, length, options, nouns, verbs, adjectives, adverbs):
    for x in range(0, length):
      options[random.randint(0, 40000) % len(options)](nouns, verbs, adjectives, adverbs);
    print '\n'

