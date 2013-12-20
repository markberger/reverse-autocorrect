from reverse_autocorrect import ReverseAutocorrect

def main():
	print 'Welcome to Reverse Autocorrect'
	sentence = raw_input("Please enter a sentence: ")
	ra = ReverseAutocorrect()
	print ra.generate_sentence(sentence)

if __name__ == "__main__":
	main()