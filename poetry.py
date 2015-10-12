#####imports lists of words, sentence structures, and system arguments
# imports words from the dictionary file
from dictionary import Words
# imporst sentences from the sentences file
from sentences import Sentences
# imports the ability to take in arguments when running the file
from sys import argv
# imports the ability to get a random number
import random
# imports the current time
from datetime import datetime

# seeds the random function
# this makes the random function spit out different random numbers
# random is just like a math equations, if you put in the same number, you get
# out the same number. If we give it time, which changes, it will give us
# different numbers.
random.seed(datetime.now)

# this stores our dictionary of words in a variable called words so that we can
# use it more easily
words = Words()

# this stores our sentence structures in a variable called sentences so that we
# can print them more easily
sentences = Sentences()

# this is a list of all the sentence structure options that we can print. We use
# this list so that we can pick a random one to print when we write the poem
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

# this function gets called when we want to print the poem. It has inputs and
# outputs
# inputs: numstanzas - the number of stanzas that we want to print
#         numlines - the number of lines per stanza
#         options - the list of sentence options defined above
#         words - our dictionary of words
# outputs: prints the poem to the screen, or to a file
def print_poem(numstanzas, numlines, options, words):
  # this loops to print each stanza
  for x in range(0, numstanzas):
    # this loops to print each line in the stanza
    for x in range(0, numlines):
      # this picks a random sentence from our list of sentences to print
      options[random.randint(0, 40000) % len(options)](words);
    # this adds a new line after each stanza
    print '\n'

# this is where the print_poem function is called
# by default, it will print a poem with 4 stanzas and 3 lines per stanza
if len(argv) < 3:
  # this is where print_poem is called if custom line numbers have not been
  # defined.
  print_poem(4, 3, options, words)
# but if we add two numbers after the file name when we run this code, we can
# have it print a different number of stanzas and lines. These numbers get
# stored in argv. The first number is stored in argv[1] and the second number is
# stored in argv[2]
else:
  # this is where the print_poem function is called with custom line numbers
  print_poem(int(argv[1]), int(argv[2]), options, words)
