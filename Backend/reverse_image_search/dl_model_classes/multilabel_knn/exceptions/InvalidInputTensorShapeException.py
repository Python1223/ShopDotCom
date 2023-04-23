class InvalidInputTensorShapeException(Exception):
    """ Invalid Input Tensor Exception is raised when inputs tensors are not of the shape (_, N) and (_, N) """

    def __init__(self) -> None:
        self.__message: str = "Input Tensors must of shape (N, _) and (N, _)"
        super().__init__(self.__message)
