from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniques = OrderedDict()
        encountered = set()
        for i, char in enumerate(s):
            if char in uniques:
                encountered.add(char)
                del uniques[char]
            else:
                if char not in encountered:
                    uniques[char] = i
        if not uniques:
            return -1
        return uniques.popitem(last=False)[1]
