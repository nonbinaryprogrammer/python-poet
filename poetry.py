from verbs import Verbs
from nouns import Nouns
from adverbs import Adverbs
from adjectives import Adjectives
from sentences import Sentences
import random
from datetime import datetime

random.seed(datetime.now)

verbs = Verbs()
nouns = Nouns()
adjectives = Adjectives()
adverbs = Adverbs()
sentences = Sentences()

def get_rand(word):
  num = random.randint(0, 3000) % (len(word))

  return word[num]

def get_metaphor(adj, noun):
  num1 = random.randint(0, 87345) % (len(adj))
  num2 = random.randint(0, 6598374) % (len(noun))

  metaphor = "as " + adj[num1] + " as a " + noun[num2]
  return metaphor

def print_sentence_with_metaphor(nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs) + " " + get_metaphor(adjectives.adjectives, nouns.singular_nouns)

def print_singular_the_sentence(nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs)

def print_singular_a_sentence(nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs)

def print_plural_sentence(nouns, verbs, adjectives, adverbs):
  print get_rand(nouns.plural_nouns) + " " + get_rand(verbs.plural_verbs)

def print_plural_action_on_singular_sentence(nouns, verbs, adjectives, adverbs):
  print get_rand(nouns.plural_nouns) + " " + get_rand(verbs.plural_verbs) + " " + get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns)

def print_plural_action_on_plural_sentence(nouns, verbs, adjectives, adverbs):
  print get_rand(nouns.plural_nouns) + " " + get_rand(verbs.plural_verbs) + " " + get_rand(nouns.plural_nouns)

def print_singular_action_on_singular_sentence(nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs) + " " + get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns)

def print_singular_action_on_plural_sentence(nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs) + " " + get_rand(nouns.plural_nouns)

def print_stanza(length, options, nouns, verbs, adjectives, adverbs):
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
