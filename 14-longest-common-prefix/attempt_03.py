class Solution:
    def longestCommonPrefix(self, strs):
        res = ''
        # out loop: iterate through indices
        for idx in range(len(strs[0])):
            # set char to compare and loop through input strings
            char = strs[0][idx]
            for s in strs:
                # handle case where common prefix pattern broken
                if idx == len(s) or s[idx] != char:
                    return res
            # all strings were equal, so append current char
            res += char
        return res