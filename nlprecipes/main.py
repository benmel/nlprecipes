import parser
import scraper

def run(url):
  print "Starting to get HTML"
  raw_html = scraper.get_html(url)
  print "parsing HTML"
  ingredients, directions, recipe_name = scraper.parse_html(raw_html)
  parser.parse_ingredients(ingredients)
  parser.parse_directions(directions)