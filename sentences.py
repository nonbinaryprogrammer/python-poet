### #imports functions from the python libraries that we need
# imports the random function for choosing random numbers
import random
# imports the date and time for use in the random function
from datetime import datetime

class Sentences:
  def __init__(self):
    # like in the poetry.py file, this makes the random function more random
    random.seed(datetime.now)

  # this function gets a random word from the list of words that we give it
  def get_rand(self, word):
    # gets a random number between 0 and 3000, then gets the remainder from
    # deviding that number by the number of words in the list so that the random
    # number is within the length of the list
    num = random.randint(0, 3000) % (len(word))

    # this spits out the word that we chose back to where the function is
    # called, where it will then be printed
    return word[num]

  # defines the structure for a simile that can be included in a sentence
  # it gets the dictionary of words when it is run
  def get_simile(self, words):
    # gets one random number to pick a noun, and one random number to pick an
    # adjective
    num1 = random.randint(0, 87345) % (len(words.adjectives))
    num2 = random.randint(0, 6598374) % (len(words.singular_nouns))

    # adds the random words together to make one string
    simile = "as " + words.adjectives[num1] + " as a " + words.singular_nouns[num2]
    # returns the string from the function to be printed where the function was
    # called.
    return simile

  # prints a sentence using the get_simile function
  def print_sentence_with_simile(self, words):
    # prints the string that is all the partial strings with random words added
    # together. The random function gets called to pick the random words. We add
    # spaces between each word for formatting
    print self.get_rand(["a", "the"]) + " " + self.get_rand(words.singular_nouns) + " " + self.get_rand(words.singular_verbs) + " " + self.get_simile(words)

  # prints a sentense with singular nouns and verbs chosen
  def print_singular_sentence(self, words):
    print self.get_rand(["a", "the"]) + " " + self.get_rand(words.singular_nouns) + " " + self.get_rand(words.singular_verbs)

  # prints a sentence with plural nouns and verbs chosen
  def print_plural_sentence(self, words):
    print self.get_rand(words.plural_nouns) + " " + self.get_rand(words.plural_verbs)

  # prints a sentence where one plural noun performs an action on another noun
  def print_plural_action_on_singular_sentence(self, words):
    print self.get_rand(words.plural_nouns) + " " + self.get_rand(words.plural_verbs) + " " + self.get_rand(["a", "the"]) + " " + self.get_rand(words.singular_nouns)

  # prints a sentence where one plural noun performs an action on a plural noun
  def print_plural_action_on_plural_sentence(self, words):
    print self.get_rand(words.plural_nouns) + " " + self.get_rand(words.plural_verbs) + " " + self.get_rand(words.plural_nouns)

  # prints a sentence where one noun performs an action on another noun
  def print_singular_action_on_singular_sentence(self, words):
    print self.get_rand(["a", "the"]) + " " + self.get_rand(words.singular_nouns) + " " + self.get_rand(words.singular_verbs) + " " + self.get_rand(["a", "the"]) + " " + self.get_rand(words.singular_nouns)

  # prints a sentence where one noun performs an action a plural noun
  def print_singular_action_on_plural_sentence(self, words):
    print self.get_rand(["a", "the"]) + " " + self.get_rand(words.singular_nouns) + " " + self.get_rand(words.singular_verbs) + " " + self.get_rand(words.plural_nouns)

  # prints a sentence with a noun, action, and adverb
  def print_singular_action_with_adverb_sentence(self, words):
    print self.get_rand(["a", "the"]) + " " + self.get_rand(words.singular_nouns) + " " + self.get_rand(words.adverbs) + " " + self.get_rand(words.singular_verbs)
    
  # prints a sentence with a noun, action, and adverb
  def print_plural_action_with_adverb_sentence(self, words):
    print self.get_rand(words.plural_nouns) + " " + self.get_rand(words.adverbs) + " " + self.get_rand(words.plural_verbs)
