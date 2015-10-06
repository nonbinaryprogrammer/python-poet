from verbs import Verbs
from nouns import Nouns
from adverbs import Adverbs
from adjectives import Adjectives
from sentences import Sentences
from stanzas import Stanzas

verbs = Verbs()
nouns = Nouns()
adjectives = Adjectives()
adverbs = Adverbs()
sentences = Sentences()
stanzas = Stanzas()

options = {0 : sentences.print_sentence_with_metaphor,
    1: sentences.print_singular_the_sentence,
    2: sentences.print_singular_a_sentence,
    3: sentences.print_plural_sentence,
    4: sentences.print_plural_action_on_singular_sentence,
    5: sentences.print_plural_action_on_plural_sentence,
    6: sentences.print_singular_action_on_plural_sentence,
    7: sentences.print_singular_action_on_singular_sentence
    }

def print_poem(numstanzas, numlines, stanzas, options, nouns, verbs, adjectives, adverbs):
  for x in range(0, numstanzas):
    stanzas.print_stanza(numlines, options, nouns, verbs, adjectives, adverbs)

print_poem(4, 3, stanzas, options, nouns, verbs, adjectives, adverbs)
