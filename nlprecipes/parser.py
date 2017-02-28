import nltk
from ingredient import Ingredient
from direction import Direction
from nltk.util import ngrams
import re
import string
import recipe_lists
from fractions import Fraction

def parse_ingredients(ingredientStrings):
	list_ingredients = []
	for ingredientStr in ingredientStrings:
		tokens = nltk.word_tokenize(ingredientStr.encode('utf8'))
		try:
			matched_quantity = Fraction(tokens[0])
		except ValueError:
			matched_quantity = None

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

		matched_descriptors = []
		pos_tokens = nltk.pos_tag(tokens)
		pos_match = ['JJ', 'RB']
		for pos_token in pos_tokens:
			if pos_token[1] in pos_match:
				if pos_token[0] != matched_measurement and pos_token[0] not in matched_preparations and pos_token[0] not in recipe_lists.not_descriptors:
					matched_descriptors.append(pos_token[0])
		matched_descriptor = ' '.join(matched_descriptors)

		matched_name = None

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
