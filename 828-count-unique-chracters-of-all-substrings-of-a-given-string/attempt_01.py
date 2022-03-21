class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # keep track of last and second to last occurence of alpha chars
        last = [[-1, -1] for _ in range(26)]
        # we don't need the base case, because dp[-1] = 0
        dp = [0] * len(s)
        for i, char in enumerate(s):
            # create a couple helper variables for readability
            char_i = ord(char) % ord('A')
            last_i = last[char_i][-1]
            scd_last_i = last[char_i][-2]
            # count s[i] contributions to previous substrings via appending
            dp[i] = dp[i - 1] + i - last_i - (last_i - scd_last_i)
            # update our last occurence array
            last[char_i][0], last[char_i][1] = last[char_i][1], i
        return sum(dp)

# intuition: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/1505263/Single-pass-O(n)-time-and-O(1)-space-solution-with-detailed-explanation

# i - last_i: these are the new substrings that contain s[i] once, add them to
# dp[i - 1]

# last_i - scd_last_i: these are the new substrings that contain s[i] exactly
# twice, remove them from dp[i - 1]

# scd_last_i - 0: these are the new substrings that contain s[i] more than
# twice. These wouldn't have been counted in previous iteration substrings,
# so we don't need to do anything here