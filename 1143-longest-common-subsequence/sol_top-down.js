/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
// top down
var longestCommonSubsequence = function(text1, text2) {
    const dp = (i, j) => {
        // base cases built in, move on to recursive case
        if (memo[i][j] < 0) {
            // handle case where current elements match
            if (text1[i] === text2[j]) memo[i][j] = 1 + dp(i + 1, j + 1);
            // handle case where current elements do not match
            else memo[i][j] = Math.max(dp(i + 1, j), dp(i, j + 1));
        }
        return memo[i][j];
    }
    // create memoization 2D array
    const memo = [];
    for (let i = 0; i < text1.length + 1; i++) {
        const innerArr = [];
        for (let j = 0; j < text2.length + 1; j++) innerArr.push(-1);
        memo.push(innerArr);
    }
    // set base cases
    for (let i = 0; i < text2.length + 1; i++) memo[memo.length - 1][i] = 0;
    for (let i = 0; i < text1.length + 1; i++) memo[i][memo[0].length - 1] = 0;
    // call recursive function
    return dp(0, 0);
};