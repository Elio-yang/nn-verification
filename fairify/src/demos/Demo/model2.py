import tensorflow as tf
from tensorflow.keras import layers


class DemoModel2(tf.keras.Model):
    def __init__(self,input_dim):
        super(DemoModel2, self).__init__()
        self.dense1 = tf.keras.layers.Dense(16, input_dim=input_dim, activation=tf.nn.relu)
        self.dense2 = tf.keras.layers.Dense(16, activation=tf.nn.relu)
        self.dense3 = tf.keras.layers.Dense(8, activation=tf.nn.relu)
        self.dense4 = tf.keras.layers.Dense(8, activation=tf.nn.sigmoid)
        self.dense5 = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)

    def call(self, inputs):

        x = self.dense1(inputs)
        x = self.dense2(x)
        x = self.dense3(x)

        x = self.dense4(x)
        x = self.dense5(x)

        return x


if __name__ == "__main__":
    input_dim = 16  
    model = DemoModel2(input_dim)
    model.summary()