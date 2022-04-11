class MovingAverage:

    def __init__(self, size: int):
        self.q = [None] * size
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = size
        self.sum = 0

    def next(self, val: int) -> float:
        # handle case of empty queue
        if not self.size:
            self.q[self.tail] = val
            self.size += 1
        # handle case of non-empty queue
        else:
            # handle case where queue is NOT at capacity
            if self.size < self.capacity:
                self.size += 1
            # handle case where queue is at capacity
            else:
                self.sum -= self.q[self.head]
                self.head = (self.head + 1) % self.capacity
            # update tail pointer and value
            self.tail = (self.tail + 1) % self.capacity
            self.q[self.tail] = val
        # return average
        self.sum += val
        return self.sum / self.size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
