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
  directions = direction_parser.parse_directions(directions)
  recipes = recipe.Recipe(recipe_name, ingredients, directions)  
  #transformation.transform(recipes, 'healthy_to_unhealthy')
  for d in ingredients:
  	print d.__dict__
  print "parsing direction"
  for d in directions:
  	print d.__dict__
 