class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # handle edge case
        if not needle:
            return 0
        # only iterate through possible beginning indices
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1
