import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from PIL import Image
from Backend.reverse_image_search.dl_model_classes.vgg16.vgg16 import VGG16
import training_parameters


def get_training_input_and_output_tensors() -> tuple[tf.Tensor, tf.Tensor]:
    input_dataframe: pd.DataFrame = pd.read_csv("Backend/reverse_image_search/training/training_data/ImageInput.csv")
    n: int = len(input_dataframe)

    input_tensor: list = list()
    output_tensor: list = list()

    for index in range(n):
        image_url: str = input_dataframe.iloc[index, 1]
        image_category: int = input_dataframe.iloc[index, 2]

        image: Image = Image.open(image_url)
        image_nparray: np.ndarray = np.asarray(image.resize((200, 200)))
        input_tensor.append(image_nparray)

        curr_output: list[int] = [0] * 17
        curr_output[image_category] = 1
        output_tensor.append(curr_output)

    input_tensor_np: np.ndarray = np.array(input_tensor) / 255
    output_tensor_np: np.ndarray = np.array(output_tensor)

    input_tensor_tf: tf.Tensor = tf.convert_to_tensor(input_tensor_np)
    output_tensor_tf: tf.Tensor = tf.convert_to_tensor(output_tensor_np)

    return input_tensor_tf, output_tensor_tf


def train(model: keras.models.Model, input_tensor: tf.Tensor, output_tensor: tf.Tensor) -> keras.models.Model:
    model.compile(
        optimizer=training_parameters.optimizer(learning_rate=training_parameters.learning_rate),
        loss=training_parameters.loss,
        metrics=training_parameters.metrics
    )

    model.fit(
        x=input_tensor,
        y=output_tensor,
        batch_size=training_parameters.batch_size,
        epochs=training_parameters.epochs,
        verbose=training_parameters.verbose
    )

    return model


def save_model(model: keras.models.Model, filepath: str) -> None:
    keras.models.save_model(model=model, filepath=filepath, overwrite=True)


def main() -> None:
    training_input_and_output_tensors: tuple[tf.Tensor, tf.Tensor] = get_training_input_and_output_tensors()
    input_tensor: tf.Tensor = training_input_and_output_tensors[0]
    output_tensor: tf.Tensor = training_input_and_output_tensors[1]

    vgg16: VGG16 = VGG16()
    fine_tuned_vgg16: VGG16 = train(model=vgg16, input_tensor=input_tensor, output_tensor=output_tensor)
    filepath: str = '../fine_tuned_vgg16'

    save_model(model=fine_tuned_vgg16, filepath=filepath)


if __name__ == "__main__":
    main()
