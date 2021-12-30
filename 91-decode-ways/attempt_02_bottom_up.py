# bottom-up
# use int() to start, maybe create helper functions later
# trying size as the inner loop

class Solution:
    def numDecodings(self, s: str) -> int:
        # handle base case of leading '0'
        if s[0] == '0':
            return 0
        # build memo array, implicitly set base case
        memo = [[0] * len(s) for i in range(3)]
        memo[1][0] = 1
        memo[2][0] = 1
        # DEBUG PRINTING
        print('memo:')
        for row in memo:
            print(row)
        ################
        # work up to full string
        for j in range(1, len(s), 1):
            for i in range(1, 3, 1):
                print('i: ', i)
                print('j: ', j)
                print('s[j - i + 1: j + 1]: ', s[j - i + 1: j + 1])
                if self.is_valid(s[j - i + 1: j + 1]):
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
                else:
                    memo[i][j] = memo[i - 1][j]
                # DEBUG PRINTING
                print('memo:')
                for row in memo:
                    print(row)
                ################
        return memo[2][len(s) - 1]
    
    def is_valid(self, s):
        if len(s) == 2:
            return int(s) > 9 and int(s) < 27
        elif len(s) == 1:
            return int(s) > 0 and int(s) < 10
        else:
            print('*** DEBUG: passed weird string to is_valid()')





        # for char in s:
        #     print(f'ord({char}) = {ord(char)}')
        #     print(f'mod 48: {ord(char) % 48}')