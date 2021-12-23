class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # use dictionary to track explored words
        dict = {}
        # loop through word list
        for word in words:
            # handle case where word has been encountered already
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1
        # loop through dict and add to max-heap
        heap = MaxHeap(k)
        for key in dict:
            # only handle case where node needs added
            node = HeapNode(key, dict[key])
            if heap.census < heap.capacity:
                heap.add(node)
            elif node.count > heap.min_count:
                heap.add(node)
            elif node.count == heap.min_count and node.word < heap.min_word:
                heap.add(node)
        # pop k items from top of max heap
        return_arr = []
        for i in range(k):
            return_arr.append(heap.remove().word)
        return return_arr

class HeapNode:
    def __init__(self, word, count):
        self.word = word
        self.count = count

class MaxHeap:
    def __init__(self, k):
        self.heap = []
        self.capacity = k
        self.census = 0
        self.min_count = 501
        self.min_word = ''
    
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
            temp = self.heap[idx_prt]
            self.heap[idx_prt] = self.heap[idx]
            self.heap[idx] = temp
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
            temp = self.heap[idx]
            if self.idx_is_less(idx_left, idx_right):
                self.heap[idx] = self.heap[idx_right]
                self.heap[idx_right] = temp
                idx = idx_right
            else:
                self.heap[idx] = self.heap[idx_left]
                self.heap[idx_left] = temp
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
    
    def prt_is_less(self, idx):
        prt_idx = self.get_prt_idx(idx)
        if self.heap[prt_idx].count < self.heap[idx].count:
            return True
    
    def has_child(self, idx, left=True):
        if left:
            return (idx * 2) + 1 < len(self.heap)
        else:
            return (idx * 2) + 2 < len(self.heap)
    
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
    
    def get_child(self, idx):
        idx_left, idx_right = self.get_child_idx(idx)
        arr = []
        if idx_left is not None:
            arr.append(self.heap[idx_left])
        else:
            arr.append(None)
        if idx_right is not None:
            arr.append(self.heap[idx_right])
        else:
            arr.append(None)
        return tuple(arr)
