#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../../')

from random import shuffle
from z3 import *
from utils.input_partition import *
from utils.verif_utils import *
from utils.prune import *
from importlib import import_module

import tensorflow as tf
# from Demo.model1 import DemoModel1
# from Demo.model2 import DemoModel2

from Demo.model1 import create_mlp_model



def train_model1():
    # Load data
    df, X_train, y_train, X_test, y_test = load_adult_ac1()

    # Get input dimension from the training data
    input_dim = X_train.shape[1]
    print(input_dim)
    alpha = 0.01
    # Create and compile the model
    model = create_mlp_model(input_dim,alpha)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=64, batch_size=32, validation_data=(X_test, y_test))

    # Evaluate the model on the test set
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')

    model.save('Demo1.h5')
    print("Model saved as 'Demo1.h5'")

# def train_model2():
#     # Load data
#     df, X_train, y_train, X_test, y_test = load_bank()

#     # Get input dimension from the training data
#     input_dim = X_train.shape[1]

#     # Create and compile the model
#     model = DemoModel2(input_dim)
#     model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#     # Train the model
#     model.fit(X_train, y_train, epochs=32, batch_size=32, validation_data=(X_test, y_test))

#     # Evaluate the model on the test set
#     loss, accuracy = model.evaluate(X_test, y_test)
#     print(f'Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')

#     model.save('Demo2', save_format='tf')
#     print("Model saved as 'Demo2'")

if __name__ == "__main__":
    train_model1()
    # train_model2()
    