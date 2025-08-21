def get_book_text(file_path):

	with open(file_path) as f:
		file_contents = f.read()
		return file_contents

def num_words(bookcontents):

	listofwords = bookcontents.split()
	count = 0
	for words in listofwords:
		count += 1
	return count


def main():
	a = "books/frankenstein.txt"
	bookcontents = get_book_text(a)
	test = num_words(bookcontents)
	print(f"{test} words found in the document")

main()
