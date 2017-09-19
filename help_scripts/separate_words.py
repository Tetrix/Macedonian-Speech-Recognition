import nltk
from nltk import word_tokenize, sent_tokenize
import re
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

def separate_unique_words():
	unique = []
	with open ('formatted_text_fresh.txt', 'r') as f:
		content = f.read()
		content = re.sub(r'[^\w\s]','',content).lower()

		words = word_tokenize(content)

		for i in words:
			if i not in unique:
				unique.append(i)
	return unique			


unique = separate_unique_words()


for w in unique:
	with open('separate_words.txt', 'a') as f:
		f.write(w + '\n')	