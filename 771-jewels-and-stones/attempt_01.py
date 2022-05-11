class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        j_set = set()
        for jewel in jewels:
            j_set.add(jewel)
        for stone in stones:
            if stone in j_set:
                res += 1
        return res
