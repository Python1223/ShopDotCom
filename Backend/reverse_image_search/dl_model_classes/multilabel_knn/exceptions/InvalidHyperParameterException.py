class InvalidHyperParameterException(Exception):
    """ Invalid Hyper Parameter Exception is raised when hyperparameter is not within a specific range"""

    def __init__(self) -> None:
        self.__message = "Hyper-parameter value must be in the range (0,N)\n N -> Total number of samples"
        super().__init__(self.__message)
