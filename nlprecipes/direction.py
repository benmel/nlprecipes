class Direction:
  def __init__(self, tools, methods, preparations, times, unparsed):
    self.tools = tools
    #below are the primary cooking methods
    self.methods = methods
    #below are the secondary cooking methods
    self.preparations = preparations
    self.times = times
    self.unparsed = unparsed
