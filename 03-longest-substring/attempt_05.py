class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        beg = 0
        res = 0
        for idx, char in enumerate(s):
            if char in last:
                if last.get(char) >= beg:
                    beg = last.get(char) + 1
                last[char] = idx
            else:
                last[char] = idx
            res = max(res, idx - beg + 1)
        return res