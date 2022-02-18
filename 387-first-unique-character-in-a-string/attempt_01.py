from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniques = OrderedDict()
        dups = set()
        for i, char in enumerate(s):
            if char not in dups:
                if char in uniques:
                    uniques.pop(char)
                    dups.add(char)
                else:
                    uniques[char] = i
        if len(uniques) == 0: return -1
        return uniques.popitem(last=False)[1]
