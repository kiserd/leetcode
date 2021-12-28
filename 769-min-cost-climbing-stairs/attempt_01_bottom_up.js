/**
 * @param {number[]} cost
 * @return {number}
 */
// bottom up
var minCostClimbingStairs = function(cost) {
    // handle base cases
    if (cost.length < 3) return Math.min(cost[0], cost[1]);
    // loop through, building memo object
    const dp = [0, 0];
    for (let i = 2; i <= cost.length; i++) {
        dp[i] = Math.min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2]);
    }
    return dp[cost.length];
};