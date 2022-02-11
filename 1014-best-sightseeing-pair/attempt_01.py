# class Solution:
#     def maxScoreSightseeingPair(self, values) -> int:
#         max_right = -60000
#         max_val = -60000
#         for i in range(len(values) - 1, 0, -1):
#             max_right = max(max_right, values[i] - i)
#             max_val = max(max_val, values[i - 1] + i - 1 + max_right)
#         return max_val


class Solution:
    def maxScoreSightseeingPair(self, values) -> int:
        max_left = 0
        max_val = 0
        for i, num in enumerate(values):
            max_val = max(max_val, num - i + max_left)
            max_left = max(max_left, num + i)
        return max_val

# took the approach of determining max_right or max_left as we proceed through
# the array. However, there is a way to process things without keeping track
# of i