class Solution:
    def twoSum(self, numbers, target: int):
        st = 0
        ed = len(numbers) - 1
        while True:
            num = numbers[st] + numbers[ed]
            if num == target:
                return [st + 1, ed + 1]
            elif num < target:
                st += 1
            else:
                ed -= 1