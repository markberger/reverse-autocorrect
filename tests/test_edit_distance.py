import unittest
from weighted_edit_distance import WeightedEditDistance

class TestEditDistance(unittest.TestCase):

	def test_neighbors_consistant(self):
		# Check to make sure our key relationships are bidirectional
		# because we are using this map to represent a bidirectional
		# graph.
		ed = WeightedEditDistance()
		for neighbor in ed._neighbors:
			for edge in ed._neighbors[neighbor]:
				self.assertTrue(neighbor in ed._neighbors[edge])

	def test_key_distance(self):
		ed = WeightedEditDistance()
		self.assertEqual(ed._key_distance('q', 'q'), 0)
		self.assertEqual(ed._key_distance('q', 'w'), 1)
		self.assertEqual(ed._key_distance('u', 'n'), 2)
		self.assertEqual(ed._key_distance('q', 'p'), 9)

		# '~' is not in our graph, so we should get the default maximum
		# used for characters we don't know about.
		self.assertEqual(ed._key_distance('h', '~'), ed._MAX_DISTANCE)

	def test_edit_distance(self):
		ed = WeightedEditDistance()
		self.assertEqual(ed.edit_distance('led', 'bed'), 4)
		self.assertEqual(ed.edit_distance('bed', 'led'), 4)
		self.assertEqual(ed.edit_distance('a', 'ab'), 10)
		self.assertEqual(ed.edit_distance('ab', 'a'), 10)

		# Counts the two 'p's in 'apple' as insertions.
		# Edit distance between 'l' and 'd' is 6.
		# Edit distance between 'e' and 'd' is 1.
		# Total edit distance is 20 + 6 + 1 = 27.
		self.assertEqual(ed.edit_distance('apple', 'add'), 27)
		self.assertEqual(ed.edit_distance('add', 'apple'), 27)
