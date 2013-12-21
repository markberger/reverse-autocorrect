reverse-autocorrect
===================

reverse-autocorrrect is a small Python app that is meant to break
sentences. The idea originated from the autocorrect on smartphones,
which often miscorrects words to form funny or shocking sentences.
reverse-autocorrect is an attempt to form those funny or shocking
sentences by breaking sentences that are otherwise correct.

To run the program, type:
```
python main.py
```

I used [nose](http://nose.readthedocs.org/en/latest/) to run the tests. If
you would like to run the tests yourself, type:
```
nosetests
```

---

Many of the concepts and ideas in this small program were inspired by
Peter Norvig's [web page on spellcheck](http://norvig.com/spell-correct.html).
I also use Norvig's [corpus](http://norvig.com/big.txt), a concatenation of
Project Gutenberg books.
