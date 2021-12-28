# bottom-up
# attempt to solve in O(n) while using O(1) space
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        # initialize next steps
        one_step = cost[len(cost) - 2]
        two_steps = cost[len(cost) - 1]
        # loop back down to starting steps
        for i in range(len(cost) - 3, -1, -1):
            current_step = None
            # handle case where taking one steps is less costly
            if one_step < two_steps:
                current_step = cost[i] + one_step
            # handle case where taking two steps is less costly
            else:
                current_step = cost[i] + two_steps
            # adjust saved values back one step
            two_steps = one_step
            one_step = current_step
        # return min of starting on the first or second step
        return min(one_step, two_steps)