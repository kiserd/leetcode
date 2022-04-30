from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        visited = set()
        helper = OrderedDict()
        for idx, char in enumerate(s):
            if char in visited:
                if char in helper:
                    del helper[char]
            else:
                helper[char] = idx
                visited.add(char)
        if helper:
            return helper.popitem(last=False)[1]
        return -1
