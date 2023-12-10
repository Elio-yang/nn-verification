#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# reinterpret network symbolically using z3 variables.
import sys
from z3 import *
import numpy as np 
import pandas as pd 
import collections
import time
import datetime

from utils.verif_utils import *



alpha = 0.01
def layer_net(x, w, b):
    layers = []    
    for i in range(len(w)):
        x1 = w[i].T @ x + b[i]
        y1 = x1 if i == len(w)-1 else relu(x1)
        layers.append(y1)
        x = y1
    return layers

def net(x, w, b):
    x1 = w[0].T @ x + b[0]
    y1 = relu(x1)
    
    x2 = w[1].T @ y1 + b[1]
    y2 = relu(x2)

    x3 = w[2].T @ y2 + b[2]
    y3 = leaky_relu(alpha,x3)

    x4 = w[3].T @ y3 + b[3]
    y4 = relu(x4)

    x5 = w[4].T @ y4 + b[4]

    return x5


def z3_net(x, w, b):
    
    fl_x = np.array([FP('fl_x%s' % i, Float32()) for i in range(16)])  
    
    for i in range(len(x)):
        fl_x[i] = ToReal(x[i])
        
    x1 = w[0].T @ fl_x + b[0]
    y1 = z3Relu(x1)
    
    x2 = w[1].T @ y1 + b[1]
    y2 = z3Relu(x2)

    x3 = w[2].T @ y2 + b[2]
    y3 = z3LeakyRelu(x3,alpha)

    x4 = w[3].T @ y3 + b[3]
    y4 = z3Relu(x4)

    x5 = w[4].T @ y4 + b[4]
    
    return x5



