# implementation of heap data structure
# heap is tree-based data structure which has an invariant true at every operation done on the data structure

# each element has a parent except the root

#

# Operations allowed on the heap:
#
# get_right_child()
# get_left_child()
# get_parent()

# for each element at index i, the left child is stored at (2*i)+1 position and right child is stored (2*i)+2

from abc import ABC, abstractmethod


class Heap(ABC):
    @abstractmethod
    def push(self, value):
        """
        push: elements are always added to the end of the heap, left to right
        """
        pass

    @abstractmethod
    def pop(self, value):
        """
         pop function removes and returns the root element
        """
        pass

    @abstractmethod
    def peek(self):
        """
        peek function returns the root element
        """
        pass

    @abstractmethod
    def _heapify_up(self, index):
        """
           function to ensure that the heap invariant is remains after modification to the heap.
        """
        pass

    @abstractmethod
    def _heapify_down(self):
        """
           function to ensure that the heap invariant is remains after modification to the root.
        """
        pass
