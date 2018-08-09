from mathinterpreter import *

s = '(-2+(3)-5)*10'
m = MathInterpreter(s)
print(s, '\n', m.view(), sep='')
print(m.calc())
# prints:
# (-2+(3)-5)*10
# *(-(+(-(0, 2), 3), 5), 10)
# -40.0
