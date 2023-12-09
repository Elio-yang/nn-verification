import tensorflow as tf
from tensorflow.keras import layers


def create_mlp_model(input_dim,taplha):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(16, input_dim=input_dim, activation=tf.keras.layers.LeakyReLU(alpha=taplha)),
        tf.keras.layers.Dense(16, activation=tf.keras.layers.LeakyReLU(alpha=taplha)),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model



# class DemoModel1(tf.keras.Model):
#     def __init__(self,input_dim):
#         super(DemoModel1, self).__init__()
#         self.dense1 = tf.keras.layers.Dense(32, input_dim=input_dim, activation=tf.nn.relu)
#         self.dense2 = tf.keras.layers.Dense(64, activation=tf.nn.relu)
#         self.dense3 = tf.keras.layers.Dense(128, activation=tf.nn.relu)

#         self.dense4 = tf.keras.layers.Dense(128, activation=tf.nn.sigmoid)
#         self.dense5 = tf.keras.layers.Dense(64, activation=tf.nn.sigmoid)
#         self.dense6 = tf.keras.layers.Dense(32, activation=tf.nn.sigmoid)
#         self.dense7 = tf.keras.layers.Dense(16, activation=tf.nn.sigmoid)

#         self.dense8 = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)

#     def call(self, inputs):

#         x = self.dense1(inputs)
#         x = self.dense2(x)
#         x = self.dense3(x)

#         x = self.dense4(x)
#         x = self.dense5(x)
#         x = self.dense6(x)
#         x = self.dense7(x)
#         x = self.dense8(x)

#         return x


if __name__ == "__main__":
    input_dim = 16  
    model = create_mlp_model(input_dim)
    model.summary()