
import parser
import scraper
import direction_parser
import recipe
import transformation
def run(url):
  print "Starting to get HTML"
  raw_html = scraper.get_html(url)
  print "parsing HTML"
  ingredients, directions, recipe_name = scraper.parse_html(raw_html)
  ingredients = parser.parse_ingredients(ingredients)
  directions = direction_parser.parse_directions(directions,ingredients)
  recipes = recipe.Recipe(recipe_name, ingredients, directions)  
  transformation.transform(recipes, 'vegetarian_to_meat')
  import pdb; pdb.set_trace()

