import tensorflow as tf
from sklearn.decomposition import PCA
from reverse_image_search import utils
from reverse_image_search.dl_model_classes.vgg16.vgg16 import VGG16
from reverse_image_search.dl_model_classes.multilabel_knn.multi_label_knn import MultiLabelKNN
from ItemManagement.models import ItemModel


class ReverseImageSearchMLPipeline:
    """ ML Pipeline that handles prediction of similar items given an input image """

    def __init__(self, pipeline_parameters: dict) -> None:
        """
            Pipeline Parameters
                __image_tensor_shape : Shape of image tensors across the pipeline
                __vgg16 : Fine-tuned VGG16 keras mode
        """

        self.__image_tensor_shape: tuple[int, int] = pipeline_parameters['image_tensor_shape']
        self.__vgg16: VGG16 = pipeline_parameters['vgg16']
        self.__pca: PCA = PCA(n_components=pipeline_parameters['n_components'])
        # self.__knn_dict = pipeline_parameters['knn_dict']

        # array of knn
        # self.multilabel_knn: MultiLabelKNN = MultiLabelKNN(
        #     feature_tensor=pipeline_parameters['feature_tensor'],
        #     label_tensor=pipeline_parameters['label_tensor'],
        #     k=pipeline_parameters['k'])

    def generate_embeddings(self, input_image_url: str) -> tuple[int, tf.Tensor]:
        image_tensor: tf.Tensor = utils.convert_image_to_tensor(image_url=input_image_url,
                                                                size=self.__image_tensor_shape)
        image_tensor /= 255
        image_output: tuple[int, tf.Tensor] = self.__vgg16(input_tensor=image_tensor, mode='PREDICTION')
        image_label: int = image_output[0]
        image_embedding: tf.Tensor = self.__pca.fit_transform(image_output[1])

        return image_label, image_embedding

    def get_recommendations(self, input_image_url: str) -> list[int]:
        image_label: int
        image_embedding: tf.Tensor
        image_label, image_embedding = self.__generate_embeddings(input_image_url=input_image_url)

        neighbours: list[ItemModel] =
        knn = ReverseImageSearchMLPipeline.get_knn(label=image_label)
        recommendations: list[int] = [neighbour.item_id for neighbour in knn.get_nearest_neighbours()]
        return recommendations
