class Solution:
    def twoSum(self, numbers, target: int):
        # i tracks index of first potential number in our pair
        i = 0
        upper_bound = len(numbers) - 1
        # use binary search to find potential partner
        while numbers[i] <= target:
            # only process distinct "starting" number
            if numbers[i] != numbers[i - 1]:
                tgt = target - numbers[i]
                # kick off binary search
                st, ed = i + 1, upper_bound
                while st <= ed:
                    mid = st + ((ed - st) // 2)
                    # handle case of successful hit
                    if numbers[mid] == tgt:
                        return [i + 1, mid + 1]
                    # adjust start and end indices
                    if numbers[mid] < tgt:
                        st = mid + 1
                    else:
                        upper_bound = mid - 1
                        ed = mid - 1
            # binary search failed, try new starting number
            i += 1
        # all search avenues fruitless, indicate to calling function
        return False
