class Solution:
    def groupAnagrams(self, strs):
        counts = {}
        for word in strs:
            cts = [0] * 26
            for char in word:
                cts[ord(char) % ord('a')] += 1
            cts = tuple(cts)
            if cts in counts:
                counts[cts].append(word)
            else:
                counts[cts] = [word]
        # group anagrams together
        res = []
        for key in counts:
            res.append(counts[key])
        return res