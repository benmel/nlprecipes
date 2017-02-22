import nltk
#from ingredient import Ingredient
#from direction import Direction
from nltk.corpus import stopwords
import string

stops = set(stopwords.words("english"))

def parse_ingredients(ingredientStrings):
	print "-- parsing ingredients --"
	list_ingredients = []
	for ingredientStr in ingredientStrings:
		utf8 = ingredientStr.encode('utf8').lower().translate(None, string.punctuation)
		tokenized = nltk.word_tokenize(utf8)
		tagged = nltk.pos_tag(tokenized)
		#new_Ingredient = Ingredient(name, quantity, measurement, descriptor, preparation, unparsed)
		#list_ingredients.append(new_Ingredient)
	return list_ingredients

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