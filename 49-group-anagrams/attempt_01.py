# first naive attempt using sorting - see if this jogs up some ideas
class Solution:
    def groupAnagrams(self, strs):
        # loop through strings and add sorted string to dict
        dict = {}
        for wd in strs:
            std = sorted(wd)
            std = ''.join(std)
            if std in dict:
                dict[std].append(wd)
            else:
                dict[std] = [wd]
        # loop back through and produce array of anagrams
        res = []
        for key in dict.keys():
            res.append(dict[key])
        return res



# my first guess is to build a hashmap based on the sum of the ASCII
# codes of the characters. Although this would have unwanted collisions

# sorting each string seems unwise, but the sort time would be considered
# constant (due to the upper bound on strs[i].length).

# for each elt of strs, we need to know two things:
#   (1) do the characters of elt match a previous string
#   (2) do the characters of elt match a future string