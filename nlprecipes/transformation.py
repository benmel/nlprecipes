import nltk
from ingredient import Ingredient
from direction import Direction
from nltk.corpus import stopwords
import re
import string
import recipe_lists
import parser


def transform(Recipe, type):
	if type =="vegetarian_to_meat":
		return vege_to_meat
	elif type == "meat_to_vegetarian":
		return meat_to_vege
	elif type =="healthy_to_unhealthy":
		return health_to_unhealth
	elif type =="unhealthy_to_healthy":
		return unhealth_to_health
	elif type =='':
		return 
	elif type =='':
		return 
# assuming these are pass by reference
def vege_to_meat(Recipe):	
	direction = Recipe.directions
	ingredient = direction.ingredients
	for i in range(0, len(ingredient)):
		if ingredient[i].name in recipe_lists.vege:
			ingredient[i].name= recipe_lists.meat[0]
	direction.ingredients = ingredient
	Recipe.direction = direction
	return Recipe

def meat_to_vege(Recipe):
	direction = Recipe.directions
	ingredient = direction.ingredients
	for i in range(0, len(ingredient)):
		if ingredient[i].name in recipe_lists.meat:
			ingredient[i].name = recipe_lists.vege[0]
	direction.ingredients=ingredient
	Recipe.directions = direction
	return Recipe

def health_to_unhealth(Recipe):
	direction = Recipe.directions
	ingredient = direction.ingredients
	for item in ingredient:
		if item.name in recipe_lists.unhealthy:
			item.measurement = float(item.measurement/2)
	return Recipe
def unhealth_to_health(Recipe):
	direction = Recipe.directions
	ingredient = direction.ingredients
	for item in ingredient:
		if item.name in recipe_lists.unhealthy:
			item.measurement = item.measurement * 2
	return Recipe






