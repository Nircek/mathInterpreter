import mathinterpreter as mi

s = '(-2+(3)-5)*10' # set equation to do
m = mi.MathInterpreter(s) # init object
print(s) # print equation [1]
print(m.view()) # view object's version of equation [2]
print(m.calc()) # print result of equation [3]
# prints:
# [1] (-2+(3)-5)*10
# [2] *(-(+(-(0, 2), 3), 5), 10)
# [3] -40.0
