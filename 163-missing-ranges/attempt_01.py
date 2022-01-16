class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):
        # use two pointers
        nums.append(upper + 1)
        i = lower
        j = 0
        st = i
        ed = i
        res = []
        while i <= upper:
            # handle case where next element is not sequential
            if nums[j] != i:
                ed = nums[j] - 1
                # handle case of single elt range
                if st == ed:
                    res.append(str(st))
                else:
                    res.append(str(st) + '->' + str(ed))
                i = nums[j] + 1
                st = i
                j += 1
            # handle case where next elt is sequential
            else:
                j += 1
                i += 1
                st += 1
        return res
