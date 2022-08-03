class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        bg = 0
        res = 0
        for idx, ch in enumerate(s):
            # char has occured on/after bg
            if last.get(ch, -1) >= bg:
                res = max(res, idx - 1 - bg + 1)
                bg = last[ch] + 1
                last[ch] = idx
            # either first occurence of char or occurs prior to bg
            else:
                last[ch] = idx
                res = max(res, idx - bg + 1)
        return res
