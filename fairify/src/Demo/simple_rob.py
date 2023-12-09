import sys
sys.path.append('../../')
from z3 import *
from utils.verif_utils import *
import numpy as np 

def z3Exp(x):
    exp_taylor_series = 1 + x + x**2 / 2 + x**3 / 6 + x**4 / 24 + x**5 / 120 +x**6/720 + x**7/5040 + x**8/40320 + x**9/362880 + x**10/3628800
    return exp_taylor_series

def z3Softmax(x):
    return 

def layer_net(x):

    y1 = 4.32*x[0] + 0.123
    y2 = 4.45*x[1] - 3.24
    y3 = 1.034*x[2] + 1.22
    y4 = 2.134*x[3] + 0.087

    v = y1+y2+y3+y4 # send to sigmoid
    return v

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
sy = z3Exp(y)
y_ = z3_layer(x_)
sy_ = z3Exp(y_)

eps = 0.000001
delta = 2

s = Solver()

s.add(Abs(x[0]-x_[0])<delta)
s.add(Abs(x[1]-x_[1])<delta)
s.add(Abs(x[2]-x_[2])<delta)
s.add(Abs(x[3]-x_[3])<delta)

s.add(-100<=x[0],x[0]<=100)
s.add(-100<=x[1],x[1]<=100)
s.add(-100<=x[2],x[2]<=100)
s.add(-100<=x[3],x[3]<=100)

s.add( Abs(sy-sy_) > eps)
      

s.set("timeout", 100*1000)

res = s.check()
print(res)

tx =[]
tx_ =[]
if res == sat:
    m = s.model()
    for i in range(4):
        print(m[x[i]],m[x_[i]])
        tx.append(m[x[i]].as_long())
        tx_.append(m[x_[i]].as_long())
    
    ry = z3Exp( layer_net(tx))
    ry_ = z3Exp (layer_net(tx_))
    print("ry=",ry)
    print("ry_=",ry_)
    print("ry-ry_=",ry-ry_)
