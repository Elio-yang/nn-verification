import tensorflow as tf

def create_mlp_model(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, input_dim=input_dim, activation='relu'),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    return model

if __name__ == "__main__":
    input_dim = 13  
    model = create_mlp_model(input_dim)
    model.summary()