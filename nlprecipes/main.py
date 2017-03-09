import parser
import scraper
import direction_parser
import recipe
import transformation
def run(url,transformation_type):
  print "Starting to get HTML"
  raw_html = scraper.get_html(url)
  print "parsing HTML"
  ingredients, directions, recipe_name = scraper.parse_html(raw_html)
  ingredients = parser.parse_ingredients(ingredients)
  directions = direction_parser.parse_directions(directions)
  recipes = recipe.Recipe(recipe_name, ingredients, directions)  
  transformation.transform(recipes, transformation_type)
  for d in ingredients:
  	print d.__dict__
  for d in directions:
  	print d.__dict__


def parse(url, print_type):
  print "Starting to get HTML"
  raw_html = scraper.get_html(url)
  print "parsing HTML"
  ingredients, directions, recipe_name = scraper.parse_html(raw_html)
  ingredients = parser.parse_ingredients(ingredients)
  directions = direction_parser.parse_directions(directions)
  recipes = recipe.Recipe(recipe_name, ingredients, directions)  
  if print_type == "Object":
    for d in ingredients:
      print d.__dict__
    for d in directions:
      print d.__dict__
  elif print_type == "Human":
    print "Human readable string......"
  return recipes

def transform(recipes,transformation_type, print_type):
  print "Performing Transformation"
  transformation.transform(recipes, transformation_type)
  if print_type == "Object":
    print "object format....."
  elif print_type == "Human":
    print "Human readable string......"
 