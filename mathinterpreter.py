class MathInterpreter:
  def set_brackets(self):
    br = [[0,0]]
    p = 0
    while self.s[0] == '(' and self.s[-1] == ')':
      self.s = self.s[1:-1]
    for i in range(len(self.s)):
      e = self.s[i]
      if e == '(' or e == '[' or e == '{':
        p += 1
        if p == 1:
          br += [[i]]
      elif e == ')' or e == ']' or e == '}':
        p -= 1
        if p == 0:
          br[-1] += [i]
    self.br = br + [[len(self.s), len(self.s)]]
  def find(self, f):
    for i in range(len(self.br)-1, 0, -1):
      j = self.s.find(f, self.br[i-1][1], self.br[i][0])
      if j != -1:
        return j
    return j
  def explode(self, o):
    self.set_brackets();
    i = -1
    l = 1
    for e in o:
      j = self.find(e)
      if j > i:
        i = j
        l = len(e)
    if i == -1:
      return False
    else:
      self.sep(i, l)
      return True
  
  def __init__(self, s):
    self.s = s
    if s == '':
      self.p = True
      self.a = '0'
      return
    if self.explode(('+', '-')):
      pass
    elif self.explode(('*', '/')):
      pass
    else:
      self.p = True
      self.a = self.s
  def sep(self, o, l=1):
    self.p = False
    self.a = MathInterpreter(self.s[:o])
    self.b = MathInterpreter(self.s[o+l:])
    self.z = self.s[o:o+l]
  def __str__(self):
    return self.view()
  def view(self):
    if self.p:
      return self.a
    else:
      return self.z + '(' + self.a.view() + ', ' + self.b.view() + ')'
