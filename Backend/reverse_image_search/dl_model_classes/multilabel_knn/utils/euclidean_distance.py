import tensorflow as tf


class EuclideanDistance:

    @staticmethod
    def get_euclidean_distance(tensor1: tf.Tensor, tensor2: tf.Tensor) -> float:
        """ Returns Euclidean Distance between 2 tensors """

        squared_difference: tf.Tensor = (tensor1 - tensor2) ** 2
        summed_squared_difference: tf.Tensor = tf.reduce_sum(squared_difference)
        euclidean_distance: float = float(summed_squared_difference.numpy()) ** 0.5

        return euclidean_distance
