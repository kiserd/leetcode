class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        factor1 = 1
        ptr1 = len(num1) - 1
        while ptr1 > -1:
            factor2 = 1
            ptr2 = len(num2) - 1
            while ptr2 > -1:
                part1 = factor2 * int(num2[ptr2])
                part2 = factor1 * int(num1[ptr1])
                res += (part1 * part2)
                ptr2 -= 1
                factor2 *= 10
            ptr1 -= 1
            factor1 *= 10
        return str(res)
