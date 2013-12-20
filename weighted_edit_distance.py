from Queue import Queue

class WeightedEditDistance():

	# Distance used for an insertion or a deletion.
	_insert_distance = 10

	# If we can't find a key after exhausting our BFS, we return
	# this value.
	_MAX_DISTANCE = 15

	# The keys on the keyboard as a dict of key -> set(neighboring keys).
	# We use this to represent a bidirectional graph.
	_neighbors = {
			'a': set(['q', 'w', 's', 'z']),
			'b': set(['v', 'g', 'h', 'n']),
			'c': set(['x', 'd', 'f', 'v']),
			'd': set(['s', 'x', 'c', 'f', 'r', 'e']),
			'e': set(['w', 's', 'd', 'r']),
			'f': set(['d', 'c', 'v', 'g', 't', 'r']),
			'g': set(['f', 'v', 'b', 'h', 'y', 't']),
			'h': set(['g', 'b', 'n', 'j', 'u', 'y']),
			'i': set(['u', 'j', 'k','o']),
			'j': set(['h', 'n', 'm', 'k', 'i', 'u']),
			'k': set(['j', 'm', 'l', 'o', 'i']),
			'l': set(['k', 'o', 'p', ':']),
			'm': set(['n', 'j', 'k']),
			'n': set(['b', 'h', 'j', 'm']),
			'o': set(['i', 'k', 'l', 'p']),
			'p': set(['o', 'l', ':']),
			'q': set(['a', 'w']),
			'r': set(['e', 'd', 'f', 't']),
			's': set(['a', 'z', 'x', 'd', 'e', 'w']),
			't': set(['r', 'f', 'g', 'y']),
			'u': set(['y', 'h', 'j', 'i']),
			'v': set(['c', 'f', 'g', 'b']),
			'w': set(['q', 'a', 's', 'e']),
			'x': set(['z', 's', 'd', 'c']),
			'y': set(['t', 'g', 'h', 'u']),
			'z': set(['a', 's', 'x']),
			'\'': set([':']),
			':': set(['p', 'l', '\''])
		}

	def _key_distance(self, a, b):
		assert len(a) == 1 and type(a) is str
		assert len(b) == 1 and type(b) is str
		a = a.lower()
		b = b.lower()

		# We do a breath-first-search to determine the distance
		# between two keys. We to compute these values when
		# initializing the class because the results are finite.
		q = Queue()
		used = set()
		q.put((a, 0))
		while not q.empty():
			i = q.get()
			if i[0] == b:
				return i[1]
			for neighbor in self._neighbors[i[0]]:
				if neighbor not in used:
					used.add(neighbor)
					q.put((neighbor, i[1]+1))
		return self._MAX_DISTANCE


	def edit_distance(self, A, B):
		return self._edit_distance(A, B, 0)

	def _edit_distance(self, A, B, distance):
		"""
		We return the weighted edit distance between word A and
		word B. The weighted edit distance is defined as the edit
		distance between the two words, where each edit is weighted
		by the distance between the two letters on the keyboard.

		For example:
			A = bed
			B = led

		The distance between 'b' and 'l' on the keyboard is 4, so the
		edit distance between 'bed' and 'led' is 4.
		"""

		if A == "":
			return distance + len(B)*self._insert_distance
		if B == "":
			return distance + len(A)*self._insert_distance

		if A[0] == B[0]:
			return self._edit_distance(A[1:], B[1:], distance)

		kd = self._key_distance(A[0], B[0])
		d1 = self._edit_distance(A[1:], B[1:], distance+kd)
		d2 = self._edit_distance(A, B[1:], distance+self._insert_distance)
		d3 = self._edit_distance(A[1:], B, distance+self._insert_distance)
		return min(d1, d2, d3)

