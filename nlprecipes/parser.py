import nltk
from ingredient import Ingredient
from direction import Direction
from nltk.corpus import stopwords
from nltk.util import ngrams
import re
import string
import recipe_lists

stops = set(stopwords.words("english"))

def parse_ingredients(ingredientStrings):
	print "-- parsing ingredients --"
	list_ingredients = []
	for ingredientStr in ingredientStrings:
		utf8 = ingredientStr.encode('utf8').lower().translate(None, string.punctuation)
		tokens = nltk.word_tokenize(utf8)

		matched_measurement = None
		for measurement in recipe_lists.measurements:
			measurement_pattern = r'(?i)\b' + re.escape(measurement)
			matched_unigram = match_unigrams(tokens, measurement_pattern)
			if matched_unigram:
				matched_measurement = matched_unigram
				break

		matched_preparations = []
		for preparation in recipe_lists.preparations:
			preparation_pattern = r'(?i)\b' + re.escape(preparation)
			matched_unigram = match_unigrams(tokens, preparation_pattern)
			if matched_unigram:
				matched_preparations.append(matched_unigram)
			matched_bigram = match_bigrams(tokens, preparation)
			if matched_bigram:
				matched_preparations.append(matched_bigram)
			matched_trigram = match_trigrams(tokens, preparation)
			if matched_trigram:
				matched_preparations.append(matched_trigram)
		matched_preparation = ', '.join(matched_preparations)

		import pdb;pdb.set_trace()

		matched_name = ''
		matched_quantity = 1
		matched_descriptor = ''

		new_Ingredient = Ingredient(matched_name, matched_quantity, matched_measurement, matched_descriptor, matched_preparation, ingredientStr)
		list_ingredients.append(new_Ingredient)
	return list_ingredients

def match_unigrams(tokens, match_pattern):
	for token in tokens:
		if re.search(match_pattern, token):
			return token

def match_bigrams(tokens, match_string):
	match_tuple = tuple(match_string.split(' '))
	bigrams = nltk.ngrams(tokens, 2)
	if match_tuple in bigrams:
		return match_string

def match_trigrams(tokens, match_string):
	match_tuple = tuple(match_string.split(' '))
	trigrams = nltk.ngrams(tokens, 3)
	if match_tuple in trigrams:
		return match_string

def parse_directions(directionStrings):
	print "-- parsing directions --"
	list_directions = []
	for directionStr in directionStrings:
		utf8 = directionStr.encode('utf8').lower().translate(None, string.punctuation)
		tokenized = nltk.word_tokenize(utf8)
		tagged = nltk.pos_tag(tokenized)
		#new_Direction = Direction(name, quantity, measurement, descriptor, preparation, unparsed)
		#list_directions.append(new_Direction)
	return list_directions