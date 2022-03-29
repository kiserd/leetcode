class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rec(i, j):
            # handle base case
            if i >= j:
                return
            # handle recursive case
            s[i], s[j] = s[j], s[i]
            rec(i + 1, j - 1)
        rec(0, len(s) - 1)
