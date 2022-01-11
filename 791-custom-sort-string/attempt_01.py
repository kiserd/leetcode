class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # create a dict mapping chars of order to numeric value
        dict = {}
        rank = 1
        for char in order:
            dict[char] = rank
            rank += 1
        # invert our dict
        num_to_char = {v: k for k, v in dict.items()}
        # get array of s by rank
        no_rank = []
        arr = []
        for char in s:
            if char in dict:
                arr.append(dict[char])
            else:
                no_rank.append(char)
        # sort array
        arr.sort()
        # build return string
        return_str = ''
        for elt in arr:
            return_str += num_to_char[elt]
        for elt in no_rank:
            return_str += elt
        return return_str