import sys
from stats import num_words
from stats import get_book_text
from stats import count_letters
from stats import make_pretty

def main():
	if len(sys.argv) != 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)	
	a = sys.argv[1]
	bookcontents = get_book_text(a)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {a}...")
	test = num_words(bookcontents)
	print("----------- Word Count ----------")
	print(f"Found {test} total words")
	print("--------- Character Count -------")
	cletter = count_letters(bookcontents)
	x=make_pretty(cletter)
	for items in x:
		character_string = items["char"]
		if character_string.isalpha():
			print(f'{items["char"]}: {items["num"]}')
	print("============= END ===============")
main()
