import nltk
from ingredient import Ingredient
from direction import Direction
from nltk.corpus import stopwords
import re
import string
import recipe_lists
import parser

def parse_directions(directionStrings):
	list_directions = []
	for directionStr in directionStrings:
		utf8 = directionStr.encode('utf8').lower().translate(None, string.punctuation)
		tokens = nltk.word_tokenize(utf8)
		preparations = []
		tools = []
		methods = []
		times = []
		for word in recipe_lists.preparations:
			preparation_pattern = r'(?i)\b' + re.escape(word)
			matched_unigram = parser.match_unigrams(tokens, preparation_pattern)
			if matched_unigram[0]:
					preparations.append(matched_unigram[0])
			matched_bigram = parser.match_bigrams(tokens, word)
			if matched_bigram[0]:
				preparations.append(matched_bigram[0])
		for word in recipe_lists.tools:

			tools_pattern = r'(?i)\b' + re.escape(word)
			matched_unigram = parser.match_unigrams(tokens, tools_pattern)
			if matched_unigram[0]:
				tools.append(matched_unigram[0])
			matched_bigram = parser.match_bigrams(tokens, word)
			if matched_bigram[0]:
				
				tools.append(matched_bigram[0])
		for word in recipe_lists.methods:
			methods_pattern = r'(?i)\b' + re.escape(word)
			matched_unigram = parser.match_unigrams(tokens, methods_pattern)
			if matched_unigram[0]:
					methods.append(matched_unigram[0])
		for word in recipe_lists.time_words:	
			match_timed = match_time(tokens, word)
			if match_timed:
				times = times + (match_timed)
		new_direction = Direction(tools, methods,preparations,times, directionStr)
		list_directions.append(new_direction)
	return list_directions

#this function pulls out the time unit and preceding number
def match_time(tokens, match_string):	
	times = []
	previous = tokens[0]
	for t in tokens:
		if t==match_string:
			times.append([previous,t])
		previous= t
	return times
