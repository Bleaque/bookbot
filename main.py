from stats import num_words
from stats import get_book_text

def main():
	a = "books/frankenstein.txt"
	bookcontents = get_book_text(a)
	test = num_words(bookcontents)
	print(f"{test} words found in the document")

main()
