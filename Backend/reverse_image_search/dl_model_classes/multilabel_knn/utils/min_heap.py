from heap_node import HeapNode


class MinHeap:
    """ MinHeap """

    def __init__(self, max_length: int) -> None:
        self.__heap_array: list[HeapNode] = list()
        self.__max_length: int = max_length
        self.__current_length: int = 0

    def insert(self, heap_node: HeapNode) -> None:
        if self.__current_length == self.__max_length:
            self.pop()

        self.__heap_array.append(heap_node)
        self.__current_length += 1
        self.percolate_up()

    def pop(self) -> HeapNode:
        if self.__current_length == 0:
            raise Exception("Heap is currently empty")

        popped_heap_node: HeapNode = self.__heap_array[0]
        self.__heap_array[0] = self.__heap_array[self.__current_length - 1]
        self.__heap_array.pop(-1)
        self.__current_length -= 1
        self.percolate_down()

        return popped_heap_node

    def percolate_up(self) -> None:
        if self.__current_length == 0:
            return None

        child_index: int = self.__current_length - 1

        while child_index > 0:
            parent_index: int = (child_index - 1) // 2
            min_heap_node: HeapNode = min(self.__heap_array[parent_index], self.__heap_array[child_index])

            if min_heap_node is self.__heap_array[parent_index]:
                return None
            else:
                MinHeap.swap_elements_in_list(self.__heap_array, parent_index, child_index)
                child_index = parent_index

    def percolate_down(self) -> None:
        if self.__current_length == 0:
            return None

        parent_index: int = 0
        n = self.__current_length

        while True:
            child_index1: int = 2 * parent_index + 1
            child_index2: int = 2 * parent_index + 2

            if child_index1 < n and child_index2 < n:

                temp_heap_node: HeapNode = self.__heap_array[parent_index]
                self.__heap_array[parent_index] = min(self.__heap_array[parent_index],
                                                      self.__heap_array[child_index1],
                                                      self.__heap_array[child_index2])

                if temp_heap_node == self.__heap_array[parent_index]:
                    break
                elif temp_heap_node == self.__heap_array[child_index1]:
                    self.__heap_array[child_index2] = temp_heap_node
                    parent_index = child_index1
                    continue
                elif temp_heap_node == self.__heap_array[child_index2]:
                    self.__heap_array[child_index2] = temp_heap_node
                    parent_index = child_index2
                    continue

            elif child_index1 < n:
                temp_heap_node: HeapNode = self.__heap_array[parent_index]
                self.__heap_array[parent_index] = min(self.__heap_array[parent_index],
                                                      self.__heap_array[child_index1])

                if temp_heap_node == self.__heap_array[parent_index]:
                    break
                elif temp_heap_node == self.__heap_array[child_index1]:
                    self.__heap_array[child_index1] = temp_heap_node
                    parent_index = child_index1
                    continue

            else:
                break

    @staticmethod
    def swap_elements_in_list(list_: list, index1: int, index2: int) -> None:
        n = len(list_)
        if not((0 < index1 < n) and (0 < index2 < n)):
            raise Exception("Index out of bound")

        list_[index1], list_[index2] = list_[index2], list_[index1]
