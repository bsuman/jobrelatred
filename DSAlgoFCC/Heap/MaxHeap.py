from Heap import Heap


class MaxHeap(Heap):
    """
    MaxHeap Invariant
    The root of the tree stores the max value, then the heap is called a maxHeap
    Each parent has value higher for maxHeap than the children
    """

    def __init__(self):
        self._heap = []

    def push(self, value):
        self._heap.append(value)
        self._heapify_up(len(self._heap)-1)

    def pop(self):
        if len(self._heap) == 1:
            return self._heap.pop()
        elif len(self._heap) >0:
            item = self._heap[0]
            self._heap[0] = self._heap.pop()
            self._heapify_down()
            return item
        else:
            return "Heap Empty!!"

    def peek(self):
        if len(self._heap) > 0:
            return self._heap[0]
        else:
            return "Heap Empty!!"

    def _heapify_up(self, index):
        while True:
            parent_index = (index - 1) // 2
            if parent_index >= 0 and self._heap[parent_index] < self._heap[index]:
                self._heap[parent_index], self._heap[index] = self._heap[index], self._heap[parent_index]
                index = parent_index
            else:
                break;

    def _heapify_down(self):
        index = 0
        size = len(self._heap)
        while True:
            left = 2*index + 1
            right = 2*index + 2
            min_index = index
            if left < size and self._heap[left] > self._heap[min_index]:
                min_index = left
            if right < size and self._heap[right] > self._heap[min_index]:
                min_index = right
            if min_index != index:
                self._heap[index], self._heap[min_index] = self._heap[min_index], self._heap[index]
                index = min_index
            else:
                break;




