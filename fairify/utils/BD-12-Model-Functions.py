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

# def model12(input_dim):
#     model = tf.keras.Sequential([
#         tf.keras.layers.Dense(5, input_dim=input_dim, activation='relu'),
#         tf.keras.layers.Dense(5, activation='relu'),
#         tf.keras.layers.Dense(15, activation='relu'),
#         tf.keras.layers.Dense(5, activation=tf.keras.layers.LeakyReLU(alpha=talpha)),
#         tf.keras.layers.Dense(5, activation='relu'),
#         tf.keras.layers.Dense(15, activation='relu'),
#         tf.keras.layers.Dense(5, activation='relu'),
#         tf.keras.layers.Dense(5, activation=tf.keras.layers.LeakyReLU(alpha=talpha)),
#         tf.keras.layers.Dense(5, activation='relu'),
#         tf.keras.layers.Dense(1, activation='sigmoid')
#     ])

#     return model

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
    y3 = relu(x3)

    x4 = w[3].T @ y3 + b[3]
    y4 = leaky_relu(alpha,x4)

    x5 = w[4].T @ y4 + b[4]
    y5 = relu(x5)

    x6 = w[5].T @ y5 + b[5]
    y6 = relu(x6)

    x7 = w[6].T @ y6 + b[6]
    y7 = relu(x7)

    x8 = w[7].T @ y7 + b[7]
    y8 = leaky_relu(alpha, x8)

    x9 = w[8].T @ y8 + b[8]
    y9 = relu(x9)

    x10 = w[9].T @ y9 + b[9]


    return x10


def z3_net(x, w, b):
    
    fl_x = np.array([FP('fl_x%s' % i, Float32()) for i in range(16)])  
    
    for i in range(len(x)):
        fl_x[i] = ToReal(x[i])
        
    x1 = w[0].T @ fl_x + b[0]
    y1 = z3Relu(x1)
    
    x2 = w[1].T @ y1 + b[1]
    y2 = z3Relu(x2)

    x3 = w[2].T @ y2 + b[2]
    y3 = z3Relu(x3)

    x4 = w[3].T @ y3 + b[3]
    y4 = z3LeakyRelu(x4,alpha)

    x5 = w[4].T @ y4 + b[4]
    y5 = z3Relu(x5)

    x6 = w[5].T @ y5 + b[5]
    y6 = z3Relu(x6)

    x7 = w[6].T @ y6 + b[6]
    y7 = z3Relu(x7)

    x8 = w[7].T @ y7 + b[7]
    y8 = z3LeakyRelu(x8,alpha)

    x9 = w[8].T @ y8 + b[8]
    y9 = z3Relu(x9)

    x10 = w[9].T @ y9 + b[9]
    
    return x10



