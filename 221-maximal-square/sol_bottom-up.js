/**
 * @param {character[][]} matrix
 * @return {number}
 */
// bottom-up
// one variable represents length of side, other represents starting indices
var maximalSquare = function(matrix) {
    // establish helper variables for readability
    // console.log('matrix: ', matrix);
    const m = matrix[0].length;
    const n = matrix.length;
    // build memoization array
    // memo[i][j] represents biggest square where i,j is bottom-right
    const memo = [];
    for (let i = 0; i < n + 1; i++) {
        const innerArr = [];
        for (let j = 0; j < m + 1; j++) innerArr.push(-1);
        memo.push(innerArr);
    }
    // console.log('memo: ', memo);
    // set base cases
    for (let i = 0; i < m + 1; i++) memo[0][i] = 0;
    for (let i = 0; i < n + 1; i++) memo[i][0] = 0;
    // loop through, building memo
    let max = 0;
    for (let i = 1; i < n + 1; i++) {
        for (let j = 1; j < m + 1; j++) {
            // initialize a couple helper variables
            // console.log('i: ', i);
            // console.log('j: ', j);
            const left = memo[i][j - 1];
            const top = memo[i - 1][j];
            const topLeft = memo[i - 1][j - 1];
            // handle case where i, j is a '1'
            if (matrix[i - 1][j - 1] === '1') {
                // handle case where top left surrounding are squares
                if (left > 0 && top > 0 && topLeft > 0) {
                    memo[i][j] = (Math.sqrt(Math.min(left, top, topLeft)) + 1) ** 2;
                }
                else {
                    memo[i][j] = 1
                }
                if (memo[i][j] > max) max = memo[i][j];
            }
            // handle case where i, j is a '0'
            else memo[i][j] = 0;
            // console.log('memo: ', memo);
        }
    }
    return max;
};