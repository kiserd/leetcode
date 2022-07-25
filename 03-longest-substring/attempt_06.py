class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        beg = 0
        res = 0
        for idx, char in enumerate(s):
            # handle case where we update beg
            if last.get(char, -1) >= beg:
                beg = last.get(char) + 1
            # update last and res
            last[char] = idx
            res = max(res, idx - beg + 1)
        return res