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
from model1 import create_mlp_model

def train_model():
    # Load data
    df, X_train, y_train, X_test, y_test = load_adult_ac1()

    # Get input dimension from the training data
    input_dim = X_train.shape[1]

    # Create and compile the model
    model = create_mlp_model(input_dim)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=64, batch_size=32, validation_data=(X_test, y_test))

    # Evaluate the model on the test set
    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test Loss: {loss:.4f}, Test Accuracy: {accuracy:.4f}')

    model.save('Ours-1.h5')
    print("Model saved as 'Ours-1.h5'")

if __name__ == "__main__":
    train_model()
