def __init__(self):
  self

def get_rand(word):
  num = random.randint(0, 3000) % (len(word))

  return word[num]

def get_metaphor(adj, noun):
  num1 = random.randint(0, 87345) % (len(adj))
  num2 = random.randint(0, 6598374) % (len(noun))

  metaphor = "as " + adj[num1] + " as a " + noun[num2]
  return metaphor

def print_sentence_with_metaphor(self, nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs) + " " + get_metaphor(adjectives.adjectives, nouns.singular_nouns)

def print_singular_the_sentence(self, nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs)

def print_singular_a_sentence(self, nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs)

def print_plural_sentence(self, nouns, verbs, adjectives, adverbs):
  print get_rand(nouns.plural_nouns) + " " + get_rand(verbs.plural_verbs)

def print_plural_action_on_singular_sentence(self, nouns, verbs, adjectives, adverbs):
  print get_rand(nouns.plural_nouns) + " " + get_rand(verbs.plural_verbs) + " " + get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns)

def print_plural_action_on_plural_sentence(self, nouns, verbs, adjectives, adverbs):
  print get_rand(nouns.plural_nouns) + " " + get_rand(verbs.plural_verbs) + " " + get_rand(nouns.plural_nouns)

def print_singular_action_on_singular_sentence(self, nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs) + " " + get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns)

def print_singular_action_on_plural_sentence(self, nouns, verbs, adjectives, adverbs):
  print get_rand(["a", "the"]) + " " + get_rand(nouns.singular_nouns) + " " + get_rand(verbs.singular_verbs) + " " + get_rand(nouns.plural_nouns)

