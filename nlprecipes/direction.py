from collections import OrderedDict

class Direction:
  def __init__(self, tools, primary_methods, secondary_methods, times, unparsed):
    self.tools = tools
    self.primary_methods = primary_methods
    self.secondary_methods = secondary_methods
    self.times = times
    self.unparsed = unparsed

  def object_notation(self):
    direction_dict = OrderedDict()
    direction_dict['unparsed'] = self.unparsed
    direction_dict['tools'] = self.tools
    direction_dict['primary_methods'] = self.primary_methods
    direction_dict['secondary_methods'] = self.secondary_methods
    direction_dict['times'] = self.times
    return direction_dict
