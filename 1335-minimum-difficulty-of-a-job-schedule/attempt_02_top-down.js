/**
 * @param {number[]} jobDifficulty
 * @param {number} d
 * @return {number}
 */
// top-down
var minDifficulty = function(jobDifficulty, d) {
    // rename jobDifficulty array for readability
    const jd = jobDifficulty;
    // handle case where we have too many days
    if (d > jd.length) return -1;
    // build recursive function
    const dp = (i, days) => {
        // handle base case of final day
        if (days === d - 1) {
            memo[i][days] = getMax(jd, i, jd.length);
            return memo[i][days];
        }
        // handle case where memo is not populated
        if (memo[i][days] === false) {
            let min = Infinity;
            for (let j = i + 1; j <= jd.length - (d - days) + 1; j++) {
                const result = getMax(jd, i, j) + dp(j, days + 1);
                if (result < min) min = result;
            }
            memo[i][days] = min;
        }
        return memo[i][days];
        
    }
    // build memoization array
    const memo = buildMemo(jd, d);
    return dp(0, 0);
};

const getMax = (arr, beg, end) => {
    let max = -Infinity;
    for (let i = beg; i < end; i++) {
        if (arr[i] > max) max = arr[i];
    }
    return max;
}

const buildMemo = (jd, d) => {
    const memo = [];
    for (let i = 0; i < jd.length; i++) {
        const innerArr = [];
        for (let j = 0; j < d; j++) innerArr.push(false);
        memo.push(innerArr);
    }
    return memo;
}


// const arr = [11, 111, 22, 222, 33, 333, 44, 444];
// const d = 6

const arr = [6, 5, 4, 3, 2, 1]
const d = 2
const diff = minDifficulty(arr, d);
console.log('result: ', diff);
