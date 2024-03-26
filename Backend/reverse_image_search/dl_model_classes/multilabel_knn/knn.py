import numpy as np
import tensorflow as tf
from exceptions import InvalidInputTensorShapeException, InvalidHyperParameterException
from utils.heap_node import HeapNode
from utils.min_heap import MinHeap
from utils.euclidean_distance import EuclideanDistance


class KNN:
    """ Multi Label KNN Classifier """

    def __init__(self, k: int) -> None:
        """
            Inputs: feature Tensor -> Input Embeddings; label Tensor -> Input Labels
            Hyper-parameters: k -> Number of nearest neighbours to consider
            n -> Number of samples
        """

        self.__k: int = k
        # self.__validate_inputs(feature_tensor=self.__feature_tensor,
        #                        label_tensor=self.__label_tensor,
        #                        k=self.__k,
        #                        n=self.__n)

    def predict_k_nearest_neighbours(self, feature_tensor_list: list[tf.Tensor], input_feature_tensor: tf.Tensor) -> int:
        """ Predicts label given an input feature tensor """

        min_heap: MinHeap = MinHeap(max_length=self.__k)
        k_nearest_neighbours: list[tf.Tensor] = list()

        for feature_tensor in feature_tensor_list:
            euclidean_distance: float = EuclideanDistance.get_euclidean_distance(feature_tensor,
                                                                                 input_feature_tensor)

            heap_node: HeapNode = HeapNode(neighbour_id=1, feature_tensor=feature_tensor, euclidean_distance=euclidean_distance)
            min_heap.insert(heap_node=heap_node)

        for _ in range(self.__k):
            neighbour: HeapNode = min_heap.pop()


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
