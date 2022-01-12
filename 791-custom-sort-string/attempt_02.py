# after browsing the solution, decided to try similar implementation
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # loop through order and append occurences from s to return vessel
        return_str = ''
        for char in order:
            return_str += (self.counter(s, char) * char)
        # add unspecified chars to the end
        for char in s:
            if char not in order:
                return_str += char
        return return_str

    def counter(self, s, k):
        count = 0
        for char in s:
            if char == k:
                count += 1
        return count