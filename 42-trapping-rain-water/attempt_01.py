class Solution:
    def trap(self, height) -> int:
        max_rt = [0] * len(height)
        max_lt = [0] * len(height)
        for i in range(1, len(height)):
            max_lt[i] = max(height[i - 1], max_lt[i - 1])
        for i in range(len(height) - 2, -1, -1):
            max_rt[i] = max(height[i + 1], max_rt[i + 1])
        res = 0
        for i, num in enumerate(height):
            if num < max_lt[i] and num < max_rt[i]:
                res += min(max_lt[i], max_rt[i]) - num
        return res
        