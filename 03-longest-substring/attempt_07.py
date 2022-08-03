class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        bg = 0
        res = 0
        for idx, ch in enumerate(s):
            # char IS in last occurence map
            if ch in last:
                if last[ch] < bg:
                    last[ch] = idx
                    res = max(res, idx - bg + 1)
                else:
                    res = max(res, idx - 1 - bg + 1)
                    bg = last[ch] + 1
                    last[ch] = idx
            # char is NOT in last occurence map
            else:
                last[ch] = idx
                res = max(res, idx - bg + 1)
        return res
