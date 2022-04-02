class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # define recursive function
        def dp(r, c):
            # handle base case
            if r == 1 and c == 1:
                return 0
            # handle recursive case
            if not memo.get((r, c), False):
                # get the prev symbol
                prev = dp(r - 1, (c + 1) // 2)
                # handle case of prev symbol == 1
                if prev:
                    memo[(r, c)] = c % 2
                # handle case of prev symbol == 0
                else:
                    if c % 2 == 0:
                        memo[(r, c)] = 1
                    else:
                        memo[(r, c)] = 0
            return memo[(r, c)]
        # build memo array and call function
        memo = {}
        return dp(n, k)
