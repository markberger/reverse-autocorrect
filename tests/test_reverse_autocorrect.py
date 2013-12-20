import os
import unittest

from reverse_autocorrect import ReverseAutocorrect

class TestReverseAutocorrect(unittest.TestCase):

	def test_read_corpus(self):
		f = open('_test_file', 'w')
		f.write('Testing testing I\'ll i\'ll word\n')
		f.close()

		ra = ReverseAutocorrect()
		model, _ = ra._read_corpus('_test_file')
		os.remove('_test_file')
		self.assertEqual(model['testing'], 3)
		self.assertEqual(model['i\'ll'], 3)
		self.assertEqual(model['word'], 2)
		self.assertEqual(model['blank'], 1)

	def test_generate_possible_words(self):
		ra = ReverseAutocorrect()
		canidates = set(['a'])
		canidates = ra._generate_possible_words(canidates, 1)
		self.assertEqual(len(canidates), 78)

		canidates = set(['ab'])
		canidates = ra._generate_possible_words(canidates, 1)
		self.assertEqual(len(canidates), 129)

	def test_generate_words(self):
		ra = ReverseAutocorrect()
		words = ra._generate_words('capital', 2)
		self.assertEqual(len(words), 6)
		self.assertTrue('capitis' in words)
		self.assertTrue('capitol' in words)
		self.assertTrue('capitals' in words)
		self.assertTrue('cubital' in words)
		self.assertTrue('capitale' in words)
		self.assertTrue('capitally' in words)
