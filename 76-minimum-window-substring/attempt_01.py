# not an optimal approach
from copy import copy


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # define process windows function
        def process_windows(sz, cts):
            chars_left = len(t)
            bg = 0
            ed = 0
            while ed < len(s):
                ch1 = s[bg]
                ch2 = s[ed]
                if cts.get(ch2, None) is not None:
                    if cts[ch2] > 0:
                        chars_left -= 1
                    cts[ch2] -= 1
                    # handle edge case
                    if ed - bg + 1 == sz and not chars_left:
                        return s[bg:ed+1]
                ed += 1
                if ed - bg + 1 > sz:
                    if cts.get(ch1, None) is not None:
                        if cts[ch1] >= 0:
                            chars_left += 1
                        cts[ch1] += 1
                    bg += 1
                if not chars_left:
                    return s[bg:ed+1]
            return ''

        res = len(t)
        # init counts representing t's char frequences
        counts = {}
        for ch in t:
            counts[ch] = counts.get(ch, 0) + 1
        # kick off helper function for potential sizes
        sz = len(t)
        while sz <= len(s):
            res = process_windows(sz, copy(counts))
            if res:
                return res
            sz += 1
        return ''
