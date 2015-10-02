from verbs import Verbs
from nouns import Nouns
from adjectives import Adjectives
import random
from datetime import datetime

random.seed(datetime.now)

verbs = Verbs()
nouns = Nouns()
adjectives = Adjectives()

def get_rand(word):
  num = random.randint(0, 3000) % (len(word))

  return word[num]

def get_metaphor(adj, noun):
  num1 = random.randint(0, 3000) % (len(adj))
  num2 = random.randint(0, 3000) % (len(noun))

  metaphor = "as " + adj[num1] + " as a " + noun[num2]
  return metaphor

def print_sentence_with_metaphor(nouns, verbs, adjectives):
  print "The " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs) + " " + get_metaphor(adjectives.adjectives, nouns.singular_nouns)

def print_singular_sentence(nouns, verbs):
  print "The " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs)

print_singular_sentence(nouns, verbs)
print_sentence_with_metaphor(nouns, verbs, adjectives)
print_singular_sentence(nouns, verbs)
