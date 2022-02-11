# tidy things up a bit using different loop
# definitely some clever math that could be incorporated here
class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        count = 2
        res = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                count += 1
                if i == len(nums) - 1:
                    for j in range(3, count + 1):
                        res += (count - j + 1)
            else:
                if count > 2:
                    # do stuff
                    for j in range(3, count + 1):
                        res += (count - j + 1)
                # reset count
                count = 2
        return res
