class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # create a couple helper collections and vars
        vowels = ['a', 'e', 'i', 'o', 'u']
        k = len(vowels)
        vowel_to_idx = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        following = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }
        # build memo array with implicit base cases
        memo = [[None] * k for _ in range(n)]
        for i in range(k):
            memo[n - 1][i] = 1
        # iterate through n chars, recording permutations
        for i in range(n - 2, -1, -1):
            for j in range(k - 1, -1, -1):
                res = 0
                for char in following[vowels[j]]:
                    res += memo[i + 1][vowel_to_idx[char]]
                memo[i][j] = res
        return sum(memo[0]) % ((10**9) + 7)
