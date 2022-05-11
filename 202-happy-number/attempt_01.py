class Solution:
    def isHappy(self, n: int) -> bool:
        # initialize helper data struct
        encountered = set()
        # process n
        curr = n
        while curr not in encountered:
            # handle successful reduction to 1
            if curr == 1:
                return True
            # update encountered set
            encountered.add(curr)
            # reduce current num to squares of parts
            new = 0
            for num in str(curr):
                new += (int(num)**2)
            curr = new
        # reduction found cycle, indicate such
        return False
