#####imports lists of words, sentence structures, and system arguments
from dictionary import Words
from sentences import Sentences
from sys import argv
import random
from datetime import datetime

words = Words()
sentences = Sentences()

options = {0 : sentences.print_sentence_with_simile,
    1: sentences.print_singular_the_sentence,
    2: sentences.print_singular_a_sentence,
    3: sentences.print_plural_sentence,
    4: sentences.print_plural_action_on_singular_sentence,
    5: sentences.print_plural_action_on_plural_sentence,
    6: sentences.print_singular_action_on_plural_sentence,
    7: sentences.print_singular_action_on_singular_sentence,
    8: sentences.print_singular_action_with_adverb_sentence,
    9: sentences.print_plural_action_with_adverb_sentence
    }

def print_poem(numstanzas, numlines, options, words):
  for x in range(0, numstanzas):
    for x in range(0, numlines):
      options[random.randint(0, 40000) % len(options)](words);
    print '\n'


if len(argv) < 3:
  print_poem(4, 3, options, words)
else:
  print_poem(int(argv[1]), int(argv[2]), options, words)
