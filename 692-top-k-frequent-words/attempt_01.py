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
        heap = self.MaxHeap
        for key in dict:
            node = self.HeapNode(key, dict[key])
            heap.add(node)


    class HeapNode:
        def __init__(self, word, count):
            self.word = word
            self.count = count
    
    class MaxHeap:
        def __init__(self, k):
            self.heap = []
        
        def add(self, node):
            # push node into next available spot
            self.heap.append(node)
            # bubble node up into appropriate spot
            idx = len(self.heap) - 1
            while (self.has_parent(idx) and self.parent_is_less(idx)):
                parent_idx = self.get_parent_index(idx)
                temp = self.heap[parent_idx]
                self.heap[parent_idx] = self.heap[idx]
                self.heap[idx] = temp
                idx = parent_idx
        
        def remove(self):
            last = self.heap[len(self.heap) - 1]
            root = self.heap[0]
            self.heap[0] = last
            idx = 0
            while self.has_child(idx, True) and self.child_is_more(idx, True) or \
                self.has_child(idx, False) and self.child_is_more(idx, False):


        def get_parent_index(self, index):
            return (index - 1) // 2
        
        def has_parent(self, index):
            return index != 0
        
        def parent_is_less(self, index):
            parent_index = self.get_parent_index(index)
            return self.heap[parent_index].count < self.heap[index].count
        
        def child_is_more(self, index, left=True):
            if left:
                return self.heap[(index * 2) + 1].count > self.heap[index].count
            else:
                return self.heap[(index * 2) + 2].count > self.heap[index].count

        
        def has_child(self, index, left=True):
            if left:
                return (index * 2) + 1 > len(self.heap) - 1
            else:
                return (index * 2) + 2 > len(self.heap) - 1
        
        def get_child_index(self, index, left=True):
            if left:
                return (index * 2) + 1
            else:
                return (index * 2) + 2
        
