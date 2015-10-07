from dictionary import Words
from sentences import Sentences
from stanzas import Stanzas

words = Words()
sentences = Sentences()
stanzas = Stanzas()

options = {0 : sentences.print_sentence_with_simile,
    1: sentences.print_singular_the_sentence,
    2: sentences.print_singular_a_sentence,
    3: sentences.print_plural_sentence,
    4: sentences.print_plural_action_on_singular_sentence,
    5: sentences.print_plural_action_on_plural_sentence,
    6: sentences.print_singular_action_on_plural_sentence,
    7: sentences.print_singular_action_on_singular_sentence
    }

def print_poem(numstanzas, numlines, stanzas, options, words):
  for x in range(0, numstanzas):
    stanzas.print_stanza(numlines, options, words)

print_poem(4, 3, stanzas, options, words)
