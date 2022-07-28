class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # define helper function
        def process_char(stack, char):
            if char == '#':
                if stack:
                    stack = stack[:-1]
            else:
                stack += char
            return stack

        # init stacks and process chars
        s_stack = ''
        t_stack = ''
        idx = 0
        while idx < len(s) or idx < len(t):
            if idx < len(s):
                s_stack = process_char(s_stack, s[idx])
            if idx < len(t):
                t_stack = process_char(t_stack, t[idx])
            idx += 1
        return s_stack == t_stack
