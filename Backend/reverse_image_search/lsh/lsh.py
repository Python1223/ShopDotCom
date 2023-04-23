from pathlib import Path
from PIL import Image
import tensorflow as tf
import numpy as np
from reverse_image_search.ml_pipeline.ml_pipeline import ReverseImageSearchMLPipeline


class LSH:
    """
        Generate image embeddings for images already in storage, so that we need not generate image embeddings
        each time, we want to get  it against a given input image
    """

    @staticmethod
    def generate_embeddings(pipeline_parameters: dict) -> None:
        reverse_image_search_pipeline: ReverseImageSearchMLPipeline = ReverseImageSearchMLPipeline(pipeline_parameters=
                                                                                                   pipeline_parameters)
        input_path_prefix: Path = Path("Backend/ARTIFACTS/Media/Items")
        output_path_prefix: Path = Path("Backend/reverse_image_search/embeddings")

        for directory in input_path_prefix.iterdir():
            if directory.is_dir():
                for image_file in directory.iterdir():
                    if image_file.is_file():
                        input_filepath: Path = input_path_prefix / directory / image_file
                        image_embedding: tf.Tensor = LSH.__generate_image_embedding(filepath=input_filepath)

                        output_filename: str = "".join([image_file.stem, ".txt"])
                        output_filepath: Path = output_path_prefix / directory / output_filename

                        np.savetxt(output_filepath, image_embedding.numpy())

    @staticmethod
    def __generate_image_embedding(reverse_image_search_pipeline: ReverseImageSearchMLPipeline,
                                   filepath: Path) -> tf.Tensor:
        image_label: int
        image_embedding: tf.Tensor
        image_label, image_embedding = reverse_image_search_pipeline.generate_embeddings(input_image_url=str(filepath))
        return image_embedding
