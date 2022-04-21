class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        alphas = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] not in alphas or s[r] not in alphas:
                if s[l] not in alphas:
                    l += 1
                if s[r] not in alphas:
                    r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
