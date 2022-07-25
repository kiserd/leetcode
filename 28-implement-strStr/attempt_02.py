class Solution:
    def strStr(self, haystack, needle):
        # handle edge case
        if not needle:
            return 0
        # utilize 2-pointer approach
        left = 0
        while left <= len(haystack) - len(needle):
            if haystack[left] == needle[0]:
                right = 0
                while haystack[left + right] == needle[right]:
                    if right == len(needle) - 1:
                        return left
                    else:
                        right += 1
            # didn't find full needle
            left += 1
        return -1
        