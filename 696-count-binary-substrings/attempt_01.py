class Solution:
    def countBinarySubstrings(self, s: str):
        prev = 0
        curr = 1
        count = 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                count += min(prev, curr)
                prev = curr
                curr = 1
        # tidy up after final char
        count += min(prev, curr)
        return count
