import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from PIL import Image


def standardize_tensor(feature_tensor: tf.Tensor) -> tf.Tensor:
    """ Perform Standardization on a tensor """

    standard_scaler: StandardScaler = StandardScaler()
    standardized_feature_tensor: tf.Tensor = tf.convert_to_tensor(
        standard_scaler.fit_transform(feature_tensor))
    return standardized_feature_tensor


def convert_image_to_tensor(image_url: str, size: tuple[int, int]) -> tf.Tensor:
    """ Converts input image to tensor of given input shape """

    image: Image = Image.open(image_url)
    image_np_ndarray: np.ndarray = np.asarray(image.resize(size=size))
    image_tensor: tf.Tensor = tf.convert_to_tensor(image_np_ndarray)

    return image_tensor


