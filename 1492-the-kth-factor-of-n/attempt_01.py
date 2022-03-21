class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # try using two pointer approach
        l = 1
        r = n
        count = 0
        lo = []
        hi = []
        while l <= r:
            if n % l == 0:
                lo.append(l)
                if l < n // l:
                    hi.append(n // l)
                r = n // l - 1
                count += 1
                if count == k:
                    return lo[-1]
            l += 1
        # get result
        if len(lo) + len(hi) < k:
            return -1
        if len(lo) >= k:
            return lo[k - 1]
        return hi[-(k - len(lo))]