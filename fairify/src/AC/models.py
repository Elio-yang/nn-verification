import tensorflow as tf

def model1(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
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
        tf.keras.layers.Dense(50, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model4(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(100, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(100, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model5(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model6(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(12, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(12, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model

def model7(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(4, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model8(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(5, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model9(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(3, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(3, activation='relu'),
        tf.keras.layers.Dense(3, activation='relu'),
        tf.keras.layers.Dense(3, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model10(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(5, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model11(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

def model12(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(5, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(5, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model
