class HeapNode:
    def __init__(self, word, count):
        self.word = word
        self.count = count

class MaxHeap:
    def __init__(self, size, arr=[]):
        self.heap = [None] * size
        self.length = len(arr)
        # if starter array passed, heapify the array
        if len(arr) > 0:
            # self.heapify(arr)
            pass
    
    def heapify(self, arr):
        # get starting subtree
        subtree = self.get_prt_idx(self.length - 1)
        # recursively explore subtrees
    
    def add(self, node):
        # handle case where node represents a new min and update census
        if node.count < self.min_count:
            self.min_count = node.count
            self.min_word = node.word
        if node.count == self.min_count and node.word > self.min_word:
            self.min_word = node.word
        self.census += 1
        # push node into next available spot
        self.heap.append(node)
        # establish working variables
        idx = len(self.heap) - 1
        idx_prt = self.get_prt_idx(idx)
        # if applicable, bubble node up into appropriate spot
        while (idx_prt is not None and self.needs_swapped(idx, idx_prt)):
            self.heap[idx], self.heap[idx_prt] = self.heap[idx_prt], self.heap[idx]
            idx = idx_prt
            idx_prt = self.get_prt_idx(idx)
    
    def remove(self):
        # update census
        self.census -= 1
        # handle edge case
        if len(self.heap) == 1:
            return self.heap.pop()
        # get root to return and replace with last node
        last = self.heap.pop()
        root = self.heap[0]
        self.heap[0] = last
        # get indices for processing
        idx = 0
        idx_left, idx_right = self.get_child_idx(idx)
        while self.needs_swapped(idx_left, idx) or self.needs_swapped(idx_right, idx):
            if self.idx_is_less(idx_left, idx_right):
                self.heap[idx], self.heap[idx_right] = self.heap[idx_right], self.heap[idx]
                idx = idx_right
            else:
                self.heap[idx], self.heap[idx_left] = self.heap[idx_left], self.heap[idx]
                idx = idx_left
            # update working variables
            idx_left, idx_right = self.get_child_idx(idx)
        return root

    def needs_swapped(self, idx, idx_prt):
        # handle case of None value in either index
        if idx is None or idx_prt is None:
            return False
        # handle case where child count is greater than parent's
        if self.heap[idx].count > self.heap[idx_prt].count:
            return True
        # handle case where counts are equal
        if self.heap[idx].count == self.heap[idx_prt].count:
            return self.heap[idx].word < self.heap[idx_prt].word
        else:
            return False

    def idx_is_less(self, idx1, idx2):
        # handle edge case of Nonetype
        if idx1 is None or idx2 is None:
            return False
        # handle case where count is less
        if self.heap[idx1].count < self.heap[idx2].count:
            return True
        # handle case where counts are equal
        if self.heap[idx1].count == self.heap[idx2].count:
            return self.heap[idx1].word > self.heap[idx2].word
        else:
            return False
    
    def get_prt(self, idx):
        prt_idx = self.get_prt_idx(idx)
        return self.heap[prt_idx]

    def get_prt_idx(self, idx):
        if idx != 0:
            return (idx - 1) // 2
        return None
    
    def get_child_idx(self, idx):
        arr = []
        if (idx * 2) + 1 < len(self.heap):
            arr.append((idx * 2) + 1)
        else:
            arr.append(None)
        if (idx * 2) + 2 < len(self.heap):
            arr.append((idx * 2) + 2)
        else:
            arr.append(None)
        return tuple(arr)