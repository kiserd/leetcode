/**
 * @param {character[][]} matrix
 * @return {number}
 */
// top-down
var maximalSquare = function(matrix) {
    console.log('matrix: ', matrix);
    const dp = (i, j) => {
        // handle case where result is memoized
        if (memo[i][j] < 0) {
            // handle recursive calls in separate lines and attempt to
            const left = dp(i, j - 1);
            const top = dp(i - 1, j);
            const topLeft = dp(i - 1, j - 1);
            // handle case of '1' in current element
            if (matrix[i - 1][j - 1] === '1') {
                memo[i][j] = (Math.sqrt(Math.min(left, top, topLeft)) + 1) ** 2;
            }
            // handle case of '0' in current element
            else memo[i][j] = 0;
        }
        if (memo[i][j] > max) max = memo[i][j];
        return memo[i][j];
    }
    // establish helper variables for readability
    const n = matrix[0].length;
    const m = matrix.length;
    // build memoization array
    // memo[i][j] represents biggest square where i,j is bottom-right
    const memo = [];
    for (let i = 0; i < m + 1; i++) {
        const innerArr = [];
        for (let j = 0; j < n + 1; j++) innerArr.push(-1);
        memo.push(innerArr);
    }
    // set base cases
    for (let i = 0; i < n + 1; i++) memo[0][i] = 0;
    for (let i = 0; i < m + 1; i++) memo[i][0] = 0;
    // call recursive function
    console.log('memo: ', memo);
    let max = 0;
    dp(m, n);
    return max;
};