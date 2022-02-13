# working through problem from intuition
# try using less space
class Solution:
    def numDecodings(self, s: str) -> int:
        two_steps = 1
        one_step = 1 if s[-1] != '0' else 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                two_steps, one_step = one_step, 0
            elif s[i] == '1' or (s[i] == '2' and -1 < int(s[i + 1]) < 7):
                two_steps, one_step = one_step, one_step + two_steps
            else:
                two_steps, one_step = one_step, one_step
        return one_step
            