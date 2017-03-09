from collections import OrderedDict
import json

class Recipe:
  def __init__(self, name, ingredients, directions):
    self.name = name
    self.ingredients = ingredients
    self.directions = directions

  def object_notation(self):
    recipe_dict = OrderedDict()
    recipe_dict['name'] = self.name
    recipe_dict['ingredients'] = list(map(lambda x: x.object_notation(), self.ingredients))
    recipe_dict['directions'] = list(map(lambda x: x.object_notation(), self.directions))
    return json.dumps(recipe_dict, indent=4)

  def human_readable(self):
    recipe_output = [self.name, '\nIngredients:']

    for ingredient in self.ingredients:
      if not ingredient.changed:
        recipe_output.append(ingredient.unparsed)
      else:
        recipe_output.append(ingredient.updated())

    recipe_output.append('\nDirections:')
    for idx, direction in enumerate(self.directions):
      recipe_output.append(str(idx + 1) + '. ' + direction.unparsed)

    return '\n'.join(recipe_output)
