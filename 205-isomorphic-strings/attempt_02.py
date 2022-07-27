class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        helper = {}
        mapped = set()
        for idx, char in enumerate(s):
            if char in helper:
                if helper[char] != t[idx]:
                    return False
            else:
                if t[idx] in mapped:
                    return False
                helper[char] = t[idx]
                mapped.add(t[idx])
        return True
