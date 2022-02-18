class Solution:
    def groupAnagrams(self, strs):
        helper = {}
        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) % 65] += 1
            if helper.get(arr, False):
                helper[arr].append(word)
            else:
                helper[arr] = [word]
        return helper.values()