import sys
sys.path.append('../../')
from z3 import *
from utils.verif_utils import *
import numpy as np 

# simple single layer linear network
def z3_layer(x):
    fl_x = np.array([FP('fl_x%s' % i, Float32()) for i in range(4)])  
    
    for i in range(len(x)):
        fl_x[i] = ToReal(x[i])
    
    y1 = 4.32*fl_x[0] + 0.123
    y2 = 4.45*fl_x[1] - 3.24
    y3 = 1.034*fl_x[2] + 1.22
    y4 = 2.134*fl_x[3] + 0.087
    
    v = y1+y2+y3+y4 # send to sigmoid
    return v

x = np.array([Int('x%s' % i) for i in range(4)])
x_ = np.array([Int('x_%s' % i) for i in range(4)])

y = z3_layer(x)
y_ = z3_layer(x_)


s = Solver()

# input constraints
s.add(x[0] == x_[0])
s.add(x[1] != x_[1])
s.add(x[2] == x_[2])
s.add(x[3] == x_[3])

# input range
s.add(-100<=x[0],x[0]<=100)
s.add(-100<=x[1],x[1]<=100)
s.add(-100<=x[2],x[2]<=100)
s.add(-100<=x[3],x[3]<=100)

s.add(x[0]!=0)
s.add(x[1]!=0)
s.add(x[2]!=0)
s.add(x[3]!=0)

s.add(x_[0]!=0)
s.add(x_[1]!=0)
s.add(x_[2]!=0)
s.add(x_[3]!=0)

# output constraints
s.add(Or(And(y < 0, y_ > 0), And(y > 0, y_ < 0)))

s.set("timeout", 100*1000)

# verify
res = s.check()
print(res)
if res == sat:
    m = s.model()
    for i in range(4):
        print(m[x[i]],m[x_[i]])