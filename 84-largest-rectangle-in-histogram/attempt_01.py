class Solution:
    def largestRectangleArea(self, heights) -> int:
        # start with dummy element on the stack
        s = [(-1, -1)]
        res = 0
        for idx in range(len(heights)):
            # work to get our stack strictly increasing
            # when we find that a previous element was less than
            # or equal to our current element, we process the top
            # elements
            while heights[idx] <= s[-1][1]:
                _, height = s.pop()
                # the max volume for the top element is calculated
                # using the width between (top stack idx, idx)
                res = max(res, (idx - s[-1][0] - 1) * height)
            s.append((idx, heights[idx]))
        # now stack is monotomic increasing, so we process the stack in
        # reverse. We use [idx, len(heights) - 1] as our width and the
        # top element's height as height
        idx = len(s) - 1
        while idx > 0:
            res = max(res, (len(heights) - s[idx - 1][0] - 1) * s[idx][1])
            idx -= 1
        return res
