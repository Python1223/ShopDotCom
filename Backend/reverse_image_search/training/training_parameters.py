from tensorflow import keras

learning_rate: float = 0.0001
optimizer: keras.optimizers = keras.optimizers.Adam
loss: keras.losses = keras.losses.categorical_crossentropy
metrics: list[str] = ['accuracy']
epochs: int = 16
batch_size: int = 2
shuffle: bool = True
verbose: bool = True
