# 
class Solution:
    def groupAnagrams(self, strs):
        # loop through each string and create dict of counts
        dict = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            if tuple(counts) in dict:
                dict[tuple(counts)].append(s)
            else:
                dict[tuple(counts)] = [s]
        return dict.values()



# my first guess is to build a hashmap based on the sum of the ASCII
# codes of the characters. Although this would have unwanted collisions

# could be some thought to manipulating the ASCII values in another way..

# solution is to use counts. Should have guessed this from the custom sort
# solution