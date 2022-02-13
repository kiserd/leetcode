# had to take a look at discussion for help with this one
# plan to return later
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugs = [1]
        i = j = k = 0
        count = 1
        while count < n:
            new_ug = min(ugs[i] * 2, ugs[j] * 3, ugs[k] * 5)
            if new_ug == ugs[i] * 2:
                i += 1
            elif new_ug == ugs[j] * 3:
                j += 1
            else:
                k += 1
            if new_ug != ugs[-1]:
                ugs.append(new_ug)
                count += 1
        return ugs[-1]
