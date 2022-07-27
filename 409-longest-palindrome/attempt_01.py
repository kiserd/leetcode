class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqs = {}
        odd_count = 0
        even_count = 0
        for char in s:
            if char in freqs:
                # if frequency is odd so far, add new char to even count and
                # "move" one odd count over to even
                if freqs[char] % 2 == 1:
                    odd_count -= 1
                    even_count += 2
                else:
                    odd_count += 1
                freqs[char] += 1
            else:
                odd_count += 1
                freqs[char] = 1
        # if we have any odd counts, we can add one lone char to middle
        if odd_count:
            return even_count + 1
        return even_count
