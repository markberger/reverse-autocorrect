import collections
import re
import string
from random import randrange

from weighted_edit_distance import WeightedEditDistance


class ReverseAutocorrect():

	_corpus = 'big.txt'

	def __init__(self):
		model, dictionary = self._read_corpus(self._corpus)
		self._model = model
		self._dict = dictionary
		self._wed = WeightedEditDistance()

	def _read_corpus(self, f):
		f = open(f)
		text = f.read()
		f.close()
		r = re.compile("\w[\w']*\w|\w")
		model = collections.defaultdict(lambda: 1)
		dictionary = set()
		for word in r.finditer(text.lower()):
			word = word.group(0)
			model[word] += 1
			dictionary.add(word)
		return model, dictionary

	def generate_sentence(self, sentence):
		"""
		We randomly pick a word from the given sentence and then replace that
		word according to _calculate_replacement_word. We then return the
		sentence.
		"""
		sentence = sentence.split()
		i = randrange(0, len(sentence))
		sentence[i] = self._calculate_replacement_word(sentence[i].lower())
		return " ".join(sentence)

	def _calculate_replacement_word(self, word):
		# Our algorithm for calculating replacement words is expensive
		# based on the length of the word, so we limit possible expensive
		# calculations.
		if len(word) >= 6:
			degree = 1
		else:
			degree = 2
		possible_words = self._generate_words(word, degree)
		canidates = []
		for w in possible_words:
			ed = self._wed.edit_distance(word, w)
			canidates.append((ed * self._model[w], w))
		canidates.sort()
		return canidates[0][1]

	def _generate_words(self, word, degree):
		"""
		We get a list of all possible words within an edit distance of
		degree from word and then check those words against our dictionary.
		All of the words that are in our dictionary are returned in a set.
		"""
		canidates = set([word])
		canidates = self._generate_possible_words(canidates, degree)
		possible = set()
		for w in canidates:
			if w in self._dict:
				possible.add(w)
		if word in possible:
			possible.remove(word)
		return possible

	def _generate_possible_words(self, possible, degree):
		"""
		We recursively generate all possible combinations of letters
		that are within an edit distance of degree from the given
		words in the set possible.
		"""
		if degree == 0:
			return possible

		new_possibilities = set()
		for word in possible:
			for i in range(0, len(word)):
				if word[i] in string.lowercase:
					for letter in string.lowercase:
						# Substituting one letter
						tmp_word = word[:i] + letter + word[i+1:]
						new_possibilities.add(tmp_word)

						# Adding an additional letter
						tmp_word = word[:i] + letter + word[i:]
						new_possibilities.add(tmp_word)

					# Removing a letter
					tmp_word = word[:i] + word[i+1:]
					new_possibilities.add(tmp_word)
			for l in string.lowercase:
				new_possibilities.add(word + l)

		return self._generate_possible_words(possible.union(new_possibilities), degree - 1)

