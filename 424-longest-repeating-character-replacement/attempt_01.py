class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        ptr1 = 0
        ptr2 = 0
        ct = 0
        res = 0
        while ptr2 < len(s):
            counts[ord(s[ptr2]) % ord('A')] += 1
            dom_count = max(counts)
            if ptr2 - ptr1 + 1 - dom_count <= k:
                res = max(res, ptr2 - ptr1 + 1)
            else:
                counts[ord(s[ptr1]) % ord('A')] -= 1
                ptr1 += 1
            ptr2 += 1
        return res
