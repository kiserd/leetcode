# note, this would be easier with max-heap capabilities

import heapq
class MedianFinder:

    def __init__(self):
        # left side is represented via max-heap containing 'low-half'
        # of numbers
        self.left = []
        # right side is represented via min-heap containing 'high-half'
        # of numbers
        self.right = []

    def addNum(self, num: int) -> None:
        # first add num to left (max-heap)
        heapq.heappush(self.left, -num)
        # pop the opposite of left's max to the right
        heapq.heappush(self.right, -heapq.heappop(self.left))
        # if unbalanced and favoring right, pop opposite of min to left
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # handle case where we return single element
        # 'low-half' will always be heavy by 1 element if odd sized
        # stream has been administered
        if len(self.left) > len(self.right):
            return -self.left[0]
        # handle case where we return an average
        return round((-self.left[0] + self.right[0]) / 2, 5)