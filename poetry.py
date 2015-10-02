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

def print_singular_the_sentence(nouns, verbs, adjectives):
  print "The " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs)

def print_singular_a_sentence(nouns, verbs, adjectives):
  print "A " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs)

def print_plural_sentence(nouns, verbs, adjectives):
  print get_rand(nouns.plural_nouns) + " " + get_rand(verbs.plural_verbs)

def print_plural_action_on_singular_sentence(nouns, verbs, adjectives):
  print get_rand(nouns.plural_nouns) + " " + get_rand(verbs.plural_verbs) + " a " + get_rand(nouns.singular_nouns)

def print_plural_action_on_plural_sentence(nouns, verbs, adjectives):
  print get_rand(nouns.plural_nouns) + " " + get_rand(verbs.plural_verbs) + " "
  + get_rand(nouns.plural_nouns)

def print_singular_action_on_singular_sentence(nouns, verbs, adjectives):
  print "The " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs) + " a " + get_rand(nouns.singular_nouns)

def print_singular_action_on_plural_sentence(nouns, verbs, adjectives):
  print "The " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs) + " " + get_rand(nouns.plural_nouns)

def print_stanza(length, options, nouns, verbs, adjectives):
  for x in range(0, length):
    options[random.randint(0, 40000) % len(options)](nouns, verbs, adjectives);

options = {0 : print_sentence_with_metaphor,
    1: print_singular_the_sentence,
    2: print_singular_a_sentence,
    3: print_plural_sentence,
    4: print_plural_action_on_singular_sentence,
    5: print_plural_action_on_plural_sentence,
    6: print_singular_action_on_plural_sentence,
    7: print_singular_action_on_singular_sentence
    }

print_stanza(3, options, nouns, verbs, adjectives)
