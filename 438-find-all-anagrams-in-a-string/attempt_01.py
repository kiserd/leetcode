from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # handle edge case
        if len(p) > len(s):
            return []
        # define function to count char occurences in string
        p_counts = [0] * 26
        s_counts = [0] * 26
        for idx in range(len(p)):
            p_counts[ord(p[idx]) % ord('a')] += 1
            s_counts[ord(s[idx]) % ord('a')] += 1
        # process s while updating s_counts and comparing to p_counts
        res = []
        idx = len(p)
        while idx < len(s):
            if s_counts == p_counts:
                res.append(idx - len(p))
            # update s_counts for next iteration
            s_counts[ord(s[idx - len(p)]) % ord('a')] -= 1
            s_counts[ord(s[idx]) % ord('a')] += 1
            idx += 1
        if s_counts == p_counts:
            res.append(idx - len(p))
        return res
