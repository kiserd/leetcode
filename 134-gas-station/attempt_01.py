from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rt_net_gas = [0] * len(gas)
        total = 0
        max_surplus = 0
        for idx in range(len(gas) - 1, -1, -1):
            total += (gas[idx] - cost[idx])
            rt_net_gas[idx] = total
            max_surplus = max(max_surplus, idx, key=lambda x: rt_net_gas[x])
        if total < 0:
            return -1
        return max_surplus
