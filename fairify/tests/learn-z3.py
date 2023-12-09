from z3 import *

s = Solver()

x=[Int('x%s' % i) for i in range(4)]
y=[Int('y%s' % i) for i in range(4)]
z=[Int('z%s' % i) for i in range(4)]

for i in range(4):
    s.add(x[i]>0)
    s.add(y[i]>0)
    s.add(z[i]>0)
    s.add(x[i] == y[i] + z[i])
    s.add(x[i] < 10)
    s.add(y[i] < 10)
    s.add(z[i] < 10)

print(s.check())

print(s.model())



