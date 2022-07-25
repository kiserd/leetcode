class Solution:
    def groupAnagrams(self, strs):
        map = {}
        for s in strs:
            counts = [0] * 26
            for char in s:
                counts[ord(char) % ord('a')] += 1
            counts = tuple(counts)
            map[counts] = map.get(counts, []) + [s]
        res = []
        for key in map:
            res.append(map[key])
        return res
