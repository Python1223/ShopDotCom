import tensorflow as tf
from tensorflow import keras
from typing import Optional


class VGG16(keras.models.Model):
    """
        Custom VGG-16 model meant for fine-tuning
            MODES:
                TRAINING -> __mode is set to TRAINING while training the model
                PREDICTION -> __mode is set to TRAINING while training the model

                In PREDICTION mode, the embedding of input image is also extracted out
     """

    __MODES: tuple[str] = ('TRAINING', 'PREDICTION')

    def __init__(self) -> None:
        super(VGG16, self).__init__()
        self.VGG16_layer: keras.applications.VGG16 = keras.applications.VGG16(include_top=False,
                                                                              weights="imagenet",
                                                                              input_tensor=None,
                                                                              input_shape=None,
                                                                              pooling=None,
                                                                              classifier_activation=None)
        for layer in self.VGG16_layer.layers:
            layer.trainable = False

        self.FC_layer1: keras.layers.Flatten = keras.layers.Flatten()
        self.Dense_layer1: keras.layers.Dense = keras.layers.Dense(units=100, activation="relu")
        self.Dense_layer2: keras.layers.Dense = keras.layers.Dense(units=100, activation="relu")
        self.Dropout_layer2: keras.layers.Dense = keras.layers.Dropout(rate=0.2, name="Dropout_layer2Op")
        self.Dense_layer3: keras.layers.Dense = keras.layers.Dense(units=17, activation="softmax", name="Softmax")

        self.__image_embedding: Optional[tf.Tensor] = None
        self.__mode: str = VGG16.__MODES[0]

    def get_image_embedding(self) -> tf.Tensor:
        return self.__image_embedding

    def set_mode(self, mode_index=0) -> None:
        assert 0 <= mode_index <= 1

        self.__mode = VGG16.__MODES[mode_index]

    def call(self, inputs, training=None, mask=None) -> tf.Tensor:

        vgg_op: tf.Tensor = self.VGG16_layer(inputs)
        fc_layer1_op = self.FC_layer1(vgg_op)
        dense_layer1_op = self.Dense_layer1(fc_layer1_op)
        dense_layer2_op = self.Dense_layer2(dense_layer1_op)
        dropout_layer2_op = self.Dropout_layer2(dense_layer2_op)

        if self.__mode == 'PREDICTION':
            self.__image_embedding = dropout_layer2_op

        dense_layer3_op = self.Dense_layer3(dropout_layer2_op)
        return dense_layer3_op
