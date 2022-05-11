class TwoSum:

    def __init__(self):
        self.nums = []
        self.mapping = {}

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        # handle case of previously explored target
        if value in self.mapping and self.mapping[value]['success']:
            return True
        if value not in self.mapping:
            self.mapping[value] = {'success': None, 'pairs': set()}
        for num in self.nums:
            if num in self.mapping[value]['pairs']:
                self.mapping[value]['success'] = True
                return True
            else:
                self.mapping[value]['pairs'].add(value - num)
        self.mapping[value]['success'] = False
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
