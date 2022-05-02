class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurence = {}
        start = 0
        res = 0
        for idx, char in enumerate(s):
            # handle case of char already encountered
            if char in last_occurence:
                # handle char occured in current substring
                if last_occurence[char] >= start:
                    res = max(res, idx - start)
                    start = last_occurence[char] + 1
            # regardless, update last occurence
            last_occurence[char] = idx
        return max(res, len(s) - start)
