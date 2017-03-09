import parser
import scraper
import direction_parser
import recipe
import transformation

def parse(url):
  raw_html = scraper.get_html(url)
  ingredients, directions, recipe_name = scraper.parse_html(raw_html)
  ingredients = parser.parse_ingredients(ingredients)
  directions = direction_parser.parse_directions(directions)
  parsed_recipe = recipe.Recipe(recipe_name, ingredients, directions)
  return parsed_recipe

def transform(parsed_recipe, transformation_type):
  transformation.transform(parsed_recipe, transformation_type)
