import tensorflow as tf

def model1(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(50, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model2(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(100, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model3(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(9, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model4(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(6, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(4, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model5(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(4, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

