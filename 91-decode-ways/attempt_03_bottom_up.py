# bottom-up
# use int() to start, maybe create helper functions later
# working backward per problem hint
class Solution:
    def numDecodings(self, s: str) -> int:
        # build memo array, implicitly set base case
        memo = [0] * (len(s) + 1)
        memo[len(s)] = 1
        # work up to full string
        for i in range(len(s) - 1, -1, -1):
            # handle base case of leading 0
            if s[i] == '0':
                memo[i] = 0
            # handle case where two-char is in bounds
            elif i < len(s) - 1:
                # handle case where two-char is valid
                if self.is_valid(s[i: i + 2]):
                    memo[i] = memo[i + 1] + memo[i + 2]
                # handle case where two-char is invalid
                else:
                    memo[i] = memo[i + 1]
            # handle (maybe base) case of last non-zero substring 
            else:
                memo[i] = 1
        return memo[0]
    
    def is_valid(self, s):
        return int(s) > 9 and int(s) < 27