class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # process chars of t into a map to occurence indices
        helper = {}
        for idx, char in enumerate(t):
            helper[char] = helper.get(char, []) + [idx]
        # process s using the help of our helper mapping
        last_idx = -1
        for char in s:
            idx = 0
            char_found = False
            while not char_found and idx < len(helper.get(char, [])):
                if helper[char][idx] > last_idx:
                    last_idx = helper[char][idx]
                    char_found = True
                idx += 1
            if not char_found:
                return False
        return True
