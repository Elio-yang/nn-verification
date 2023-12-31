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

# def model4(input_dim):
#     model = tf.keras.Sequential([
#         tf.keras.layers.Dense(100, input_dim=input_dim, activation='relu'),
#         tf.keras.layers.Dense(100, activation='relu'),
#         tf.keras.layers.Dense(1, activation='sigmoid')
#     ])

#     return model

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
    return x3


def z3_net(x, w, b):
    
    fl_x = np.array([FP('fl_x%s' % i, Float32()) for i in range(16)])  
    
    for i in range(len(x)):
        fl_x[i] = ToReal(x[i])
        
    x1 = w[0].T @ fl_x + b[0]
    y1 = z3Relu(x1)
    
    x2 = w[1].T @ y1 + b[1]
    y2 = z3Relu(x2)

    x3 = w[2].T @ y2 + b[2]
    
    return x3




