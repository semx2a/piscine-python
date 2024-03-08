import sys

def count_characters(text: str):
	pass

def main(argv):
	try:
		assert len(argv) <= 2, "Too many arguments, either provide no arguments or a single string."
		
		if len(argv) == 1:
			text = input("What is the text to count?\n")
		else
			text = argv[1]
		
	except AssertionError as msg:
		print(f"AssertionError: {msg}")
		exit(1)

if __name__ == "__main__":
	main(sys.argv)