import numpy as np
import tensorflow as tf
from exceptions import InvalidInputTensorShapeException, InvalidHyperParameterException
from utils.heap_node import HeapNode
from utils.min_heap import MinHeap
from utils.euclidean_distance import EuclideanDistance


class MultiLabelKNN:
    """ Multi Label KNN Classifier """

    def __init__(self, feature_tensor: tf.Tensor, label_tensor: tf.Tensor, k: int) -> None:
        """
            Inputs: feature Tensor -> Input Embeddings; label Tensor -> Input Labels
            Hyper-parameters: k -> Number of nearest neighbours to consider
            n -> Number of samples
        """

        self.__feature_tensor: tf.Tensor = feature_tensor
        self.__label_tensor: tf.Tensor = label_tensor
        self.__k: int = k
        self.__n: int = self.__feature_tensor.shape[0]
        self.__validate_inputs(feature_tensor=self.__feature_tensor,
                               label_tensor=self.__label_tensor,
                               k=self.__k,
                               n=self.__n)
        self.__labels: set[int] = set(MultiLabelKNN.__convert_tensor_to_list_of_ints(self.__label_tensor))
        self.__int_label_tensor: list[int] = list(MultiLabelKNN.__convert_tensor_to_list_of_ints(self.__label_tensor))

    def predict_label(self, input_feature_tensor: tf.Tensor) -> int:
        """ Predicts label given an input feature tensor """

        min_heap: MinHeap = MinHeap(max_length=self.__k)

        for feature_tensor, label in zip(self.__feature_tensor, self.__int_label_tensor):
            euclidean_distance: float = EuclideanDistance.get_euclidean_distance(feature_tensor,
                                                                                 input_feature_tensor)

            heap_node: HeapNode = HeapNode(euclidean_distance=euclidean_distance,
                                           label=label)
            min_heap.insert(heap_node=heap_node)

        label_count_dict: dict = {label: 0 for label in self.__labels}
        for _ in range(self.__k):
            heap_node: HeapNode = min_heap.pop()
            label_count_dict[heap_node.get_label()] += 1

        predicted_label: int = max(label_count_dict)
        return predicted_label

    @staticmethod
    def __validate_input_tensors(feature_tensor: tf.Tensor, label_tensor: tf.Tensor) -> None:
        """ Validates input tensors """

        feature_tensor_shape: tf.TensorShape() = feature_tensor.shape
        label_tensor_shape: tf.TensorShape() = label_tensor.shape

        if not (len(feature_tensor_shape) == len(label_tensor_shape) == 2 and
                feature_tensor_shape[0] != label_tensor_shape[0]):
            raise InvalidInputTensorShapeException.InvalidInputTensorShapeException

    @staticmethod
    def __validate_hyper_parameters(k: int, n: int) -> None:
        if not (0 < k < n):
            raise InvalidHyperParameterException.InvalidHyperParameterException

    @staticmethod
    def __validate_inputs(feature_tensor: tf.Tensor, label_tensor: tf.Tensor, k: int, n: int) -> None:

        MultiLabelKNN.__validate_input_tensors(feature_tensor, label_tensor)
        MultiLabelKNN.__validate_hyper_parameters(k, n)

    @staticmethod
    def __convert_tensor_to_list_of_ints(tensor: tf.Tensor) -> list[int]:
        int_tensor: tf.Tensor = tf.cast(x=tensor, dtype=tf.int64)
        numpy_array: np.ndarray = np.array(int_tensor)
        list_int: list[int] = list(numpy_array)

        return list_int
