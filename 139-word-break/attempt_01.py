# initial attempt, horrible score
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        # create helper variable to add additional base case
        min_word = self.get_min_word_length(wordDict)
        # print('min_word: ', min_word)
        # build recursive dp function
        def dp(i, j):
            #### DEBUG PRINTING ####
            # print('i: ', i)
            # print(f'j: {j}')
            # print(f's[i:j + 1]: {s[i:j + 1]}')
            # for row in memo:
            #     print(row)
            ########################
            
            # handle case of hit in memo array
            if memo[i][j] is not None:
                # print('returned: memo is not None')
                return memo[i][j]
            else:
                # handle case of word being too small for hit
                if j - i + 1 < min_word:
                    # print('returned: word too small')
                    memo[i][j] = False
                    return False
                # loop through wordDict, looking for direct match
                for word in wordDict:
                    # print('word in wordDict: ', word)
                    if word == s[i:j + 1]:
                        # print('returned: word hit ##########################')
                        memo[i][j] = True
                        return True
                # loop through remaining substrings starting with i
                hit_found = False
                for k in range(j, i, -1):
                    if dp(i, k - 1) and dp(k, j):
                        hit_found = True
                memo[i][j] = hit_found
                return hit_found
        # build memo and return result of recursive exploration
        memo = self.build_memo(len(s))
        return dp(0, len(s) - 1)


    def build_memo(self, n):
        memo = []
        for i in range(n + 1):
            memo.append([None] * (n + 1))
        return memo
    
    def get_min_word_length(self, wordDict):
        min = 21
        for word in wordDict:
            if len(word) < min:
                min = len(word)
        return min