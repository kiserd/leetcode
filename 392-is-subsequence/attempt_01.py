class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        for idx, char in enumerate(t):
            if char == s[0]:
                ptr1 = idx
                ptr2 = 0
                while ptr1 < len(t):
                    if ptr2 == len(s) - 1 and s[ptr2] == t[ptr1]:
                        return True
                    if s[ptr2] == t[ptr1]:
                        ptr2 += 1
                    ptr1 += 1
        return False
