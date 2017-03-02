import nltk
from ingredient import Ingredient
from direction import Direction
from nltk.util import ngrams
from nltk.corpus import stopwords
import re
import string
import recipe_lists
from fractions import Fraction
from itertools import tee, izip

stop_words = set(stopwords.words('english'))

def parse_ingredients(ingredientStrings):
	list_ingredients = []
	for ingredientStr in ingredientStrings:
		tokens = nltk.word_tokenize(ingredientStr.encode('utf8'))
		matched_indices = set()

		try:
			matched_quantity = Fraction(tokens[0])
			matched_indices.add(0)
		except ValueError:
			matched_quantity = None

		matched_measurement = None
		for measurement in recipe_lists.measurements:
			measurement_pattern = r'(?i)\b' + re.escape(measurement)
			(matched_unigram, unigram_index) = match_unigrams(tokens, measurement_pattern)
			if matched_unigram:
				matched_measurement = matched_unigram
				matched_indices.add(unigram_index)

		matched_preparations = []
		for preparation in recipe_lists.preparations:
			preparation_pattern = r'(?i)\b' + re.escape(preparation)
			(matched_unigram, unigram_index) = match_unigrams(tokens, preparation_pattern)
			if matched_unigram:
				matched_preparations.append(matched_unigram)
				matched_indices.add(unigram_index)

			(matched_bigram, bigram_index) = match_bigrams(tokens, preparation)
			if matched_bigram:
				matched_preparations.append(matched_bigram)
				matched_indices.update([bigram_index, bigram_index + 1])

			(matched_trigram, trigram_index) = match_trigrams(tokens, preparation)
			if matched_trigram:
				matched_preparations.append(matched_trigram)
				matched_indices.update([trigram_index, trigram_index + 1, trigram_index + 2])

		matched_preparation = ', '.join(matched_preparations)

		matched_descriptors = []
		pos_tokens = nltk.pos_tag(tokens)
		pos_match = ['JJ', 'RB']
		for idx, pos_token in enumerate(pos_tokens):
			if pos_token[1] in pos_match:
				if idx not in matched_indices and pos_token[0] not in recipe_lists.not_descriptors:
					matched_descriptors.append(pos_token[0])
					matched_indices.add(idx)
		matched_descriptor = ' '.join(matched_descriptors)

		for idx, token in enumerate(tokens):
			if token in string.punctuation or token.lower() in stop_words:
				matched_indices.add(idx)

		matched_indices_list = sorted(list(matched_indices))
		(start_index, end_index) = find_largest_hole(matched_indices_list, len(tokens))
		matched_name = ' '.join(tokens[start_index:end_index])

		new_Ingredient = Ingredient(matched_name, matched_quantity, matched_measurement, matched_descriptor, matched_preparation, ingredientStr)
		list_ingredients.append(new_Ingredient)
	return list_ingredients

def match_unigrams(tokens, match_pattern):
	for idx, token in enumerate(tokens):
		if re.search(match_pattern, token):
			return (token, idx)
	return (None, None)

def match_bigrams(tokens, match_string):
	match_tuple = tuple(match_string.split(' '))
	bigrams = ngrams(tokens, 2)
	for idx, bigram in enumerate(bigrams):
		if bigram == match_tuple:
			return (match_string, idx)
	return (None, None)

def match_trigrams(tokens, match_string):
	match_tuple = tuple(match_string.split(' '))
	trigrams = ngrams(tokens, 3)
	for idx, trigram in enumerate(trigrams):
		if trigram == match_tuple:
			return (match_string, idx)
	return (None, None)

def find_largest_hole(indices, tokens_length):
	largest_difference = 0
	start_index = 0
	end_index = 0

	if indices[0] > 0:
		start_index = 0
		end_index = indices[0]
		largest_difference = indices[0] + 1

	for a, b in pairwise(indices):
		if b - a >= largest_difference:
			start_index = a + 1
			end_index = b
			largest_difference = b - a

	if tokens_length - indices[-1] >= largest_difference:
		start_index = indices[-1] + 1
		end_index = tokens_length

	return (start_index, end_index)

def pairwise(iterable):
  a, b = tee(iterable)
  next(b, None)
  return izip(a, b)