import random
from datetime import datetime

class Sentences:
  def __init__(self):
    random.seed(datetime.now)

  def get_rand(self, word):
    num = random.randint(0, 3000) % (len(word))

    return word[num]

  def get_simile(self, adj, noun):
    num1 = random.randint(0, 87345) % (len(adj))
    num2 = random.randint(0, 6598374) % (len(noun))

    simile = "as " + adj[num1] + " as a " + noun[num2]
    return simile

  def print_sentence_with_simile(self, nouns, verbs, adjectives, adverbs):
    print self.get_rand(["a", "the"]) + " " + self.get_rand(nouns.singular_nouns) + " " + self.get_rand(verbs.singular_verbs) + " " + self.get_simile(adjectives.adjectives, nouns.singular_nouns)

  def print_singular_the_sentence(self, nouns, verbs, adjectives, adverbs):
    print self.get_rand(["a", "the"]) + " " + self.get_rand(nouns.singular_nouns) + " " + self.get_rand(verbs.singular_verbs)

  def print_singular_a_sentence(self, nouns, verbs, adjectives, adverbs):
    print self.get_rand(["a", "the"]) + " " + self.get_rand(nouns.singular_nouns) + " " + self.get_rand(verbs.singular_verbs)

  def print_plural_sentence(self, nouns, verbs, adjectives, adverbs):
    print self.get_rand(nouns.plural_nouns) + " " + self.get_rand(verbs.plural_verbs)

  def print_plural_action_on_singular_sentence(self, nouns, verbs, adjectives, adverbs):
    print self.get_rand(nouns.plural_nouns) + " " + self.get_rand(verbs.plural_verbs) + " " + self.get_rand(["a", "the"]) + " " + self.get_rand(nouns.singular_nouns)

  def print_plural_action_on_plural_sentence(self, nouns, verbs, adjectives, adverbs):
    print self.get_rand(nouns.plural_nouns) + " " + self.get_rand(verbs.plural_verbs) + " " + self.get_rand(nouns.plural_nouns)

  def print_singular_action_on_singular_sentence(self, nouns, verbs, adjectives, adverbs):
    print self.get_rand(["a", "the"]) + " " + self.get_rand(nouns.singular_nouns) + " " + self.get_rand(verbs.singular_verbs) + " " + self.get_rand(["a", "the"]) + " " + self.get_rand(nouns.singular_nouns)

  def print_singular_action_on_plural_sentence(self, nouns, verbs, adjectives, adverbs):
    print self.get_rand(["a", "the"]) + " " + self.get_rand(nouns.singular_nouns) + " " + self.get_rand(verbs.singular_verbs) + " " + self.get_rand(nouns.plural_nouns)

