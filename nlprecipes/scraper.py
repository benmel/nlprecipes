import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        response = requests.get(url)
    except:
        print "Request failed."
        return ""
    if response.status_code != 200:
        print "Unsuccessful communication with server"
        return ""
    else:
        return response.content

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('h1', itemprop='name').string
    directions = soup.find_all('ol',itemprop="recipeInstructions")
    direction_list = []
    for ii in directions[0].children:
        if ii != u'\n':
         direction_list.append(ii.string.rstrip())
    ingredients = soup.find_all('span',itemprop="ingredients")
    ingredient_list = []
    for jj in ingredients:
        ingredient_list.append(jj.string)
    return ingredient_list, direction_list, name
