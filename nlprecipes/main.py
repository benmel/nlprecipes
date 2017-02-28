import parser
import scraper

def run(url):
  raw_html = scraper.get_html(url)
  ingredients, directions, recipe_name = scraper.parse_html(raw_html)
  parser.parse_ingredients(ingredients)
