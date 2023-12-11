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
from models import model1, model2, model3, model4, model5, model6, model7, model8, model9, model10, model11, model12

def train_model(model_name,model_imp):
    # Load data
    df, X_train, y_train, X_test, y_test = load_adult_ac1()

    # Get input dimension from the training data
    input_dim = X_train.shape[1]

    print(f'Input dimension: {input_dim}')

    # Create and compile the model
    model = model_imp(input_dim)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=128, batch_size=32, validation_data=(X_test, y_test))

    # Evaluate the model on the test set
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')

    file_name = '/u/xqg5sq/workspace/nn-verification/fairify/models/adult/AC-'+str(model_name)+'.h5'
    model.save(file_name)
    print(f"Model saved as {file_name}")

if __name__ == "__main__":
    train_model(1,model1)
    train_model(2,model2)
    train_model(3,model3)
    train_model(4,model4)
    train_model(5,model5)
    train_model(6,model6)
    train_model(7,model7)
    train_model(8,model8)
    train_model(9,model9)
    train_model(10,model10)
    train_model(11,model11)
    train_model(12,model12)
