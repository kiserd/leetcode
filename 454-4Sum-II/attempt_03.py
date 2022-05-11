# made an attempt to incorporate dp into problem, does not seem
# to improve time complexity
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        # put all nums in arr and sort them
        arrs = [nums1, nums2, nums3, nums4]
        m = len(arrs)
        n = len(arrs[0])
        # define func to build first half of mapping
        counts = {}
        dp = {}

        def builder(i, target):
            # handle base case
            if i == m // 2:
                counts[target] = counts.get(target, 0) + 1
                dp[(i, target)] = [target]
                return [target]
            # handle recursive exploration
            if (i, target) not in dp:
                targets = []
                for j in range(n):
                    for tgt in builder(i + 1, target - arrs[i][j]):
                        targets.append(tgt)
                dp[(i, target)] = targets
            else:
                for tgt in dp[(i, target)]:
                    counts[tgt] += 1
            return dp[(i, target)]

        # define function to match first half of mapping to pairs
        dp2 = {}

        def finder(i, target):
            # handle base case
            if i == m:
                return counts.get(target, 0)
            # handle recursive exploration
            if (i, target) not in dp2:
                res = 0
                for j in range(n):
                    res += finder(i + 1, target + arrs[i][j])
                dp2[(i, target)] = res
            return dp2[(i, target)]

        # kick off builder and finder functions
        builder(0, 0)
        return finder(m // 2, 0)
