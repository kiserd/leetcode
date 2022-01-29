class Solution:
    def twoSum(self, numbers, target: int):
        i = 0
        while True:
            tgt = target - numbers[i]
            if self.bin(i + 1, len(numbers) - 1, numbers, tgt):
                return [numbers[i], tgt]
            i += 1

    
    def bin(st, ed, nums, tgt):
        # handle base case
        if st > ed:
            return False
        mid = st + ((ed - st) // 2)
        if nums[mid] == tgt:
            return True
        if nums[mid] < tgt:
            return bin(mid + 1, ed, nums, tgt)
        else:
            return bin(st, mid - 1, nums, tgt)
