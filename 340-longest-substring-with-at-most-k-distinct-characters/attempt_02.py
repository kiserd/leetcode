# use OrderedDict to reduce lookup time of reset character for st
# make sure OrderedDict always has the next reset character at the front of
# the queue
from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # handle edge cases
        if k == 0: return 0
        if len(s) == 1: return 1
        # prepare working variables
        st = 0
        ed = 1
        tracker = OrderedDict()
        tracker[s[st]] = 0
        longest = 1
        while ed < len(s):
            # handle case of repeated char
            if s[ed] in tracker:
                del tracker[s[ed]]
            # update ordered dict
            tracker[s[ed]] = ed
            # handle case where max distinct reached
            if len(tracker) == k + 1:
                st = tracker.popitem(last=False)[1] + 1
            # potentially update longest substring
            longest = max(longest, len(s[st:ed + 1]))
            # update ed for next iteration
            ed += 1
        return longest
            
