/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 */
// bottom-up
var longestCommonSubsequence = function(text1, text2) {
    // build memoization array
    const memo = [];
    for (let i = 0; i < text1.length + 1; i++) {
        const innerArr = [];
        for (let j = 0; j < text2.length + 1; j++) innerArr.push(0);
        memo.push(innerArr);
    }
    // loop through from end to beginning
    for (let j = text2.length - 1; j > - 1; j--) {
        for (let i = text1.length - 1; i > -1; i--) {
            // handle case where current elements match
            if (text1[i] === text2[j]) {
                memo[i][j] = 1 + Math.max(memo[i + 1][j + 1]);
            }
            // handle case where current elements do NOT match
            else memo[i][j] = Math.max(memo[i + 1][j], memo[i][j + 1]);
        }
    }
    return memo[0][0];
};