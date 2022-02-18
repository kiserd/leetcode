class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
        return -1