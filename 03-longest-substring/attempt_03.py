# returning to problem later on
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # handle edge case
        if len(s) == 1:
            return 1
        # dict to track last occurence of char
        d = {}
        # loop through characters
        st = 0
        curr = 0
        max = 0
        for i, c in enumerate(s):
            # handle case of first c or if c occured prior to curr substring
            if c not in d or d[c] < st:
                d[c] = i
                curr += 1
            # handle case where c occured in current substring
            else:
                if curr > max:
                    max = curr
                st = d[c] + 1
                curr = i - st + 1
                d[c] = i
        # one final check for updated max, so we don't check each iteration
        if curr > max:
            max = curr
        return max

# keep track of last time char showed up in dict