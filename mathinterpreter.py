class MathInterpreter:
  def set_brackets(self):
    # look for brackets and index them in self.br
    br = [[0,0]]
    p = 0
    while self.s[0] == '(' and self.s[-1] == ')': # while brackets are not needed
      self.s = self.s[1:-1] # remove them
	# look for the most global bracket
    for i in range(len(self.s)):
      e = self.s[i]
      if e == '(' or e == '[' or e == '{': # if it's the beginning of brackets
        p += 1 # increment level
        if p == 1: # if it's first level (global)
          br += [[i]] # index its beginning
      elif e == ')' or e == ']' or e == '}': # if it's the ending of brackets
        p -= 1 # decrement level
        if p == 0: # if it's floor level (it was first level)
          br[-1] += [i] # index its ending
    self.br = br + [[len(self.s), len(self.s)]]
  def find(self, f):
    for i in range(len(self.br)-1, 0, -1): # reverse iterating thru self.br
      j = self.s.find(f, self.br[i-1][1], self.br[i][0]) # look for f in our equation in previous brackets
      if j != -1: # if it is found
        return j # return its position
    return j # or -1 if it's not found
  def explode(self, o):
    self.set_brackets() # init searching
    i = -1
    l = 1
    for e in o:
      j = self.find(e) # look for operation
      if j > i: # if it's last
        i = j # index it
        l = len(e)
    if i == -1: # if we found nothing
      return False
    # if we have something
    self.sep(i, l) # separate this to operation and constants
    return True

  def __init__(self, s):
    self.s = s
    if s == '':
      self.p = True # '' is primitive
      self.a = '0' # '' is 0
      return
    if self.explode(('+', '-')): # if it contains + or - explode this
      pass
    elif self.explode(('*', '/')): # if it contains * or / explode this
      pass
    else: # if not
      self.p = True # it's primitive
      self.a = self.s # and set its value constant
  def sep(self, o, l=1): # seperate operation for
    self.p = False # we know operation is not primitive
    self.a = MathInterpreter(self.s[:o]) # set its left argument
    self.b = MathInterpreter(self.s[o+l:]) # set its right argument
    self.z = self.s[o:o+l] # set operation char
  def __str__(self):
    return self.view()
  def view(self):
    if self.p: # if it's primitive
      return self.a # return value
    # if not, return formatted version of its content
    return self.z + '(' + self.a.view() + ', ' + self.b.view() + ')'
  def calc(self):
    if self.p: # if it's primitive
      return float(self.a) # return value
    # if not, interpret operation char and return executed operation
    if self.z == '+':
        return self.a.calc()+self.b.calc()
    if self.z == '-':
        return self.a.calc()-self.b.calc()
    if self.z == '*':
        return self.a.calc()*self.b.calc()
    if self.z == '/':
        return self.a.calc()/self.b.calc()
