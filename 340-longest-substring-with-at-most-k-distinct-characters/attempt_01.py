class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # handle edge cases
        if k == 0: return 0
        if len(s) == 1: return 1
        # prepare working variables
        st = 0
        ed = 1
        last_occurence = {s[st]: 0}
        num_distinct = 1
        longest = 1
        while ed < len(s):
            # update helper
            last_occurence[s[ed]] = ed
            # handle case of new char
            if s[ed] not in s[st:ed]:
                # handle case where max distinct reached
                if num_distinct == k:
                    st += 1
                    while st - 1 != last_occurence[s[st - 1]]:
                        st += 1
                # handle case where max distinct not reached
                else:
                    num_distinct += 1
            # potentially update longest substring
            longest = max(longest, len(s[st:ed + 1]))
            # update ed for next iteration
            ed += 1
        return longest
            
