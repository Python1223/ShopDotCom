class HeapNode:
    """ Custom HeapNode Class containing Euclidean Distance and label corresponding to
        an input tensor """

    def __init__(self, euclidean_distance: float, label: int) -> None:
        self.__euclidean_distance: float = euclidean_distance
        self.__label: int = label

    def get_euclidean_distance(self) -> float:
        return self.__euclidean_distance

    def get_label(self) -> int:
        return self.__label

    def __lt__(self, other) -> bool:
        return self.__euclidean_distance < other.get_euclidean_distance()
