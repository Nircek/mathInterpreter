class MathInterpreter:
  def explode(self, s, o):
    i = -1
    l = 1
    for e in o:
      j = s.find(e)
      if i == -1:
        i = j
        l = len(e)
      else:
        if j < i and j != -1:
          i = j
          l = len(e)
    if i == -1:
      return False
    else:
      self.sep(s, i, l)
      return True
  
  def __init__(self, s):
    if self.explode(s, ('+', '-')):
      pass
    elif self.explode(s, ('*', '/')):
      pass
    else:
      self.p = True
      self.a = s
  def sep(self, s, o, l=1):
    self.p = False
    self.a = MathInterpreter(s[:o])
    self.b = MathInterpreter(s[o+l:])
    self.z = s[o:o+l]
  def __str__(self):
    return self.view()
  def view(self):
    if self.p:
      return self.a
    else:
      return self.z + '(' + self.a.view() + ', ' + self.b.view() + ')'
