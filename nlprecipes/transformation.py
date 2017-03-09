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
		return vege_to_meat
	elif change == "meat_to_vegetarian":
		return meat_to_vege
	elif change =="healthy_to_unhealthy":
		return health_to_unhealth
	elif change =="unhealthy_to_healthy":
		return unhealth_to_health
	if type(change) is tuple:
		coming_from = change
		going_to = change
		return cuisine_change(coming_from, going_t, Recipe)

# assuming these are pass by reference

def replace_in_directions(directions, string, repl):
	for dire in direction:
		name_pattern = r'(?i)\b' + re.escape(string)
		dire.unparsed = re.sub(name_pattern, dire.unparsed, repl)


def general_ve_me(Recipe, from_list, to_list):
	directions = Recipe.directions
	ingredient = Recipe.ingredients
	for i in range(0, len(ingredient)):
		if ingredient[i].name in from_list:
			ingredient[i].name = to_list[0]
			replace_in_directions(directions, ingredient[i].name, to_list[0])

def general_health(Recipe, destination):
	direction = Recipe.directions
	ingredient = Recipe.ingredients
	for item in ingredient:
		if item.name in recipe_lists.unhealthy:
			if destination =='unhealthy':
				item.quantity = item.quantity * Fraction(2/1)
			else:
				item.quantity = item.quantity * Fraction(1/2)

def vege_to_meat(Recipe):	
	general_ve_me(Recipe, recipe_lists.vege, recipe_lists.meat)

def meat_to_vege(Recipe):
	general_ve_me(Recipe, recipe_lists.meat, recipe_lists.vege)

def health_to_unhealth(Recipe):
	general_health(Recipe, 'unhealthy')
def unhealth_to_health(Recipe):
	general_health(Recipe,'healthy')

# need to change the measurement amounts in the unparsed directions as well
def cuisine_change(coming_from, going_to, Recipe):
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
	for indt in ingredients:
		if indt.name in l:
			replace_in_directions(direction, indt.name, l[indt.name])
			indt.name = l[indt.name]
	return Recipe


