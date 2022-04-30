class Solution:
    def isPalindrome(self, s: str) -> bool:
        lt = 0
        rt = len(s) - 1
        while lt < rt:
            # bypass non-alphanumeric chars
            while lt < rt and not s[lt].isalnum():
                lt += 1
            while lt < rt and not s[rt].isalnum():
                rt -= 1
            # check for palindromic property
            if s[lt].lower() == s[rt].lower():
                lt += 1
                rt -= 1
            else:
                return False
        # string is palindrome, indicate such to calling fxn
        return True
