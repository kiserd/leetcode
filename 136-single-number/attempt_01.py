# constant space solution would be to XOR each element of nums.. because
# num XOR num == 0
# num1 XOR num2 XOR num1 == (num1 XOR num1) XOR num2
# only remaining amount would be the non-duplicated element
class Solution:
    def singleNumber(self, nums) -> int:
        tracker = {}
        for num in nums:
            if num not in tracker:
                tracker[num] = 1
            else:
                del tracker[num]
        return next(iter(tracker))