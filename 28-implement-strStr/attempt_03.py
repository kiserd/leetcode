class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # handle edge case
        if len(needle) > len(haystack):
            return -1
        # get char counts for needle
        cts_n = [0] * 26
        for ch in needle:
            cts_n[ord(ch) % ord('a')] += 1
        # init counts for haystack's sliding window
        cts_h = [0] * 26
        idx = 0
        while idx < len(needle):
            ch = haystack[idx]
            cts_h[ord(ch) % ord('a')] += 1
            idx += 1
        # process haystack using a sliding window
        bg = 0
        ed = len(needle) - 1
        while ed < len(haystack):
            # handle hit
            if cts_n == cts_h:
                if haystack[bg:ed+1] == needle:
                    return bg
            # move sliding window
            cts_h[ord(haystack[bg]) % ord('a')] -= 1
            bg += 1
            ed += 1
            if ed < len(haystack):
                cts_h[ord(haystack[ed]) % ord('a')] += 1
        return -1
