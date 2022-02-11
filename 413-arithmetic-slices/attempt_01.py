class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        count = 2
        prev = -10000
        diff = -10000
        res = 0
        for num in nums:
            if num - prev == diff:
                count += 1
            else:
                if count > 2:
                    # do stuff
                    for i in range(3, count + 1):
                        res += (count - i + 1)
                # reset count and diff
                count = 2
                diff = num - prev
            # set prev for next iter
            prev = num
        # tidy up
        if count > 2:
            for i in range(3, count + 1):
                res += (count - i + 1)
        return res
