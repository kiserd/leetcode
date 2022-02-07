# big kicker here was using dict instead of array
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # define recursive function
        def dp(t: int, dice_left: int):
            # handle base case(s)
            if dice_left == 0:
                return 1 if t == 0 else 0
            # handle recursive exploration
            if (t, dice_left) not in memo:
                ways = 0
                # can't violate property below
                ceiling = min(t - 1, dice_left * k - k)
                for new_t in range(max(0, t - k), ceiling + 1):
                    ways += dp(new_t, dice_left - 1)
                memo[(t, dice_left)] = ways
            return memo[(t, dice_left)]
        # build memo array and kick off function
        memo = {}
        return dp(target, n) % ((10 ** 9) + 7)
    
    # property:
    # target <= n * k
    
    # target - die_val <= (n - 1) * k
    #        - die_val <= (n - 1) * k - target
    #          die_val >= -(n - 1) * k + target
    #          die_val >= -nk + k + target
