/**
 * @param {number[]} cost
 * @return {number}
 */
// top-down
 var minCostClimbingStairs = function(cost) {
    const dp = (i) => {
        // console.log('i: ', i);
        // handle base cases
        if (i < 2) return 0;
        // handle recursive case
        if (!memo[i]) {
            memo[i] = Math.min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2]);
        }
        // console.log('memo: ', memo);
        return memo[i];
    }
    const memo = {};
    return dp(cost.length);
    
};