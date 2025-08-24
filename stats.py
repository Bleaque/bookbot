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

def count_letters(file_contents):
	cletter = {}
	for letter in file_contents:
		x = letter.lower()
		if x in cletter:
			cletter[x] += 1
		else:
			cletter[x] = 1
	return cletter

def sort_on(items):
	return items["num"]

def make_pretty(cletter):
	tidy_list=[]
	for char, count in cletter.items():
		tidy_dict = {"char":char, "num": count}
		tidy_list.append(tidy_dict)
	tidy_list.sort(reverse=True, key=sort_on)
	return tidy_list
				
