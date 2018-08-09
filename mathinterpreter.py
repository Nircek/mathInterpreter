class MathInterpreter:
  def explodeFirst(self, s):
    p = s.find('+')
    m = s.find('-')
    if p == -1:
      if m == -1:
        return False
      else:
        self.sep(s, m)
    else:
      if m == -1:
        self.sep(s, p)
      else:
        self.sep(s, min(m, p))
    return True
  def __init__(self, s):
    if not self.explodeFirst(s):
      self.p = True
      self.a = s
  def sep(self, s, o, l=1):
    self.p = False
    self.a = MathInterpreter(s[:o])
    self.b = MathInterpreter(s[o+l:])
    self.z = s[o:o+l]
