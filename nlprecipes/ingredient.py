from collections import OrderedDict

class Ingredient:
  def __init__(self, name, quantity, measurement, descriptor, preparation, unparsed):
    self.name = name
    self.quantity = quantity
    self.measurement = measurement
    self.descriptor = descriptor
    self.preparation = preparation
    self.unparsed = unparsed
    self.changed = False

  def object_notation(self):
    ingredient_dict = OrderedDict()
    ingredient_dict['unparsed'] = self.unparsed
    ingredient_dict['name'] = self.name
    ingredient_dict['quantity'] = str(self.quantity)
    ingredient_dict['measurement'] = self.measurement
    ingredient_dict['descriptor'] = self.descriptor
    ingredient_dict['preparation'] = self.preparation
    return ingredient_dict

  def updated(self):
    updated_ingredient = []

    if self.quantity:
      updated_ingredient.append(str(self.quantity))
    if self.measurement:
      updated_ingredient.append(self.measurement)
    if self.name:
      updated_ingredient.append(self.name)

    return ' '.join(updated_ingredient)
