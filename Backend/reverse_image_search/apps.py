from django.apps import AppConfig
from reverse_image_search.lsh.lsh import LSH
from tensorflow import keras


class ReverseImageSearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reverse_image_search'

    def ready(self) -> None:
        pipeline_parameters: dict = {
            'image_tensor_shape': (200, 200),
            'vgg16': keras.models.load_model(filepath="./fine_tuned_vgg16"),
            'n_components': 50,
        }
        LSH.generate_embeddings(pipeline_parameters=pipeline_parameters)
