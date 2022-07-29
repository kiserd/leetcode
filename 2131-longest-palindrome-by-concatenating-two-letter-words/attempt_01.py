from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # use helper data structures to track things
        middle_pals = set()
        helper = {}
        res = 0
        for word in words:
            # handle pal words
            if word[0] == word[1]:
                if word in middle_pals:
                    middle_pals.remove(word)
                    res += 4
                else:
                    middle_pals.add(word)
            # handle non-pal words
            else:
                if helper.get(word, 0) > 0:
                    helper[word] -= 1
                    res += 4
                else:
                    rev = word[1] + word[0]
                    helper[rev] = helper.get(rev, 0) + 1
        if middle_pals:
            res += 2
        return res
