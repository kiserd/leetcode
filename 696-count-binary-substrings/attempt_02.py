class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        left = 0
        right = 0
        prev = None
        res = 0
        for char in s:
            if char != prev:
                res += min(left, right)
                left, right = right, 1
            else:
                right += 1
            prev = char
        return res + min(left, right)