class Direction:
  def __init__(self, ingredients, tools, methods, preparations, times, unparsed):
    self.ingredients = ingredients
    self.tools = tools
    #below are the primary cooking methods
    self.methods = methods
    #below are the secondary cooking methods
    self.preparations = preparations
    self.times = times
    self.unparsed = unparsed
