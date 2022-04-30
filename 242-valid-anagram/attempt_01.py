class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = [0] * 26
        counts_t = [0] * 26
        if len(s) == len(t):
            for idx in range(len(s)):
                counts_s[ord(s[idx]) % ord('a')] += 1
                counts_t[ord(t[idx]) % ord('a')] += 1
            if counts_s == counts_t:
                return True
        return False
