class Solution:
    def plusOne(self, digits):
        carry = 1
        for idx in range(len(digits) - 1, -1, -1):
            curr = carry + digits[idx]
            if curr > 9:
                digits[idx] = curr % 10
                carry = 1
            else:
                digits[idx] = curr
                carry = 0
        # handle case where we overflow original array
        if carry == 1:
            digits = [1] + digits
        return digits
