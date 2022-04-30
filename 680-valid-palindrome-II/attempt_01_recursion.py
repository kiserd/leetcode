class Solution:
    def validPalindrome(self, s: str) -> bool:
        # define recursive helper function
        def is_pal(left, right, delete_used):
            # handle successful base case
            if right <= left:
                return True
            # handle unsuccessful base case
            if delete_used and s[left] != s[right]:
                return False
            # handle recursive exploration
            if s[left] == s[right]:
                return is_pal(left + 1, right - 1, delete_used)
            # handle case where we delete a char
            else:
                return is_pal(left + 1, right, True) or is_pal(left, right - 1, True)
        # call recursive helper function
        return is_pal(0, len(s) - 1, False)
