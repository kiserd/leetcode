class Solution:
    def largestRectangleArea(self, heights) -> int:
        # define recursive function
        def rec(i, j):
            # handle base case
            if i > j:
                return 0
            # handle recursive case
            res = 0
            smallest_idx = 0
            smallest_elt = -1
            for idx in range(i, j + 1):
                if heights[idx] < smallest_elt:
                    smallest_elt = heights[idx]
                    smallest_idx = idx
            res = max(smallest_elt * (j - i + 1), rec(i, smallest_idx - 1), rec(smallest_idx + 1, j))
            return res
