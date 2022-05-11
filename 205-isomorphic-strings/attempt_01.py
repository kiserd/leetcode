class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # define helper data structure
        helper = {}
        already_mapped = set()
        # process s
        for idx, char in enumerate(s):
            if char in helper:
                if helper[char] != t[idx]:
                    return False
            else:
                if t[idx] in already_mapped:
                    return False
                helper[char] = t[idx]
                already_mapped.add(t[idx])
        return True
