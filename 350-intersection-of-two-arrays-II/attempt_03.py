class Solution:
    def intersect(self, nums1, nums2):
        # define some vars to help with processing
        counts = [0] * 1001
        count = 0
        smallest = nums1
        largest = nums2
        # attempt to optimize a bit
        if len(smallest) > len(largest):
            smallest, largest = largest, smallest
        # work through smallest array, populating counts
        for num in smallest:
            counts[num] += 1
            count += 1
        # work through largest array, adding intersections to res
        res = []
        idx = 0
        while count and idx < len(largest):
            if counts[largest[idx]]:
                counts[largest[idx]] -= 1
                count -= 1
                res.append(largest[idx])
            idx += 1
        return res
