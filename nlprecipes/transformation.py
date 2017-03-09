import nltk
from ingredient import Ingredient
from direction import Direction
from nltk.corpus import stopwords
import re
import string
import recipe_lists
import parser
from fractions import Fraction

def transform(Recipe, change):
	if change =="vegetarian_to_meat":
		return vege_to_meat(Recipe)
	elif change == "meat_to_vegetarian":
		return meat_to_vege(Recipe)
	elif change =="healthy_to_unhealthy":
		return health_to_unhealth(Recipe)
	elif change =="unhealthy_to_healthy":
		return unhealth_to_health(Recipe)
	else:
		going_to = change
		return cuisine_change(going_to, Recipe)

# assuming these are pass by reference

def replace_in_directions(directions, string, repl):
	#import pdb; pdb.set_trace()
	for dire in directions:
		name_pattern = r'(?i)\b' + re.escape(string)
		#dire.unparsed = dire.unparsed.split()
		#import pdb; pdb.set_trace()
		dire.unparsed = re.sub(name_pattern, repl, dire.unparsed)

		#dire.unparsed = " ".join(dire.unparsed)


def general_ve_me(Recipe, from_list, to_list):
	directions = Recipe.directions
	ingredient = Recipe.ingredients
	for i in range(0, len(ingredient)):
		for word in from_list:
			name_pattern = r'(?i)\b' + re.escape(word)
			if re.search(name_pattern, ingredient[i].name):
				replace_in_directions(directions, word, to_list[0])
				ingredient[i].name = to_list[0]
				ingredient[i].changed = True

def general_health(Recipe, destination):
	direction = Recipe.directions
	ingredient = Recipe.ingredients
	for item in ingredient:
		for word in recipe_lists.unhealthy:		
			name_pattern = r'(?i)\b' + re.escape(word)
			if item.quantity!=None:
				if re.search(name_pattern, item.name) and destination=='unhealthy':
					item.quantity = item.quantity * Fraction(2,1)
					match_amount(direction, name_pattern, item.quantity)
					item.changed = True
				elif re.search(name_pattern, item.name) and destination=='healthy':
					item.quantity = item.quantity * Fraction(1,2)
					match_amount(direction, name_pattern, item.quantity)
					item.changed = True


def match_amount(direction, match_string, fraction):	
	for dirc in direction:
		tokens = dirc.unparsed.split()
		previous = tokens[0]
		for t in range(len(tokens)):
			if re.search(match_string, tokens[t]):
				tokens[t-1] = str(fraction)
				tokens = " ".join(tokens)
				break

def vege_to_meat(Recipe):	
	general_ve_me(Recipe, recipe_lists.vege, recipe_lists.meat)

def meat_to_vege(Recipe):
	general_ve_me(Recipe, recipe_lists.meat, recipe_lists.vege)

def health_to_unhealth(Recipe):
	general_health(Recipe, 'unhealthy')
def unhealth_to_health(Recipe):
	general_health(Recipe,'healthy')

# need to change the measurement amounts in the unparsed directions as well
def cuisine_change(going_to, Recipe):
	direction = Recipe.directions
	ingredient = Recipe.ingredients
	l = {}
	if going_to=="Chinese":
		l = recipe_lists.Chinese
	elif going_to =="Italian":
		l = recipe_lists.Italian
	elif going_to == 'Korean':
		l = recipe_lists.Korean
	elif going_to =='Indian':
		l = recipe_lists.Indian
	elif going_to == 'Mexican':
		l = recipe_lists.Mexican
	for indt in ingredient:
		for key in l:
			name_pattern = r'(?i)\b' + re.escape(key)
			if re.search(name_pattern, indt.name):
				replace_in_directions(direction, key, l[key])
				indt.name = l[key]
				indt.changed = True
	return Recipe


