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
        // handle case where memo is not populated
        if (memo[i][days] === false) {
            let min = Infinity;
            for (let j = i + 1; j <= jd.length; j++) {
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
    for (let i = 0; i <= jd.length; i++) {
        const innerArr = [];
        for (let j = 0; j <= d; j++) {
            // handle base case of no jobs left and no days left
            if (i === jd.length && j === d) innerArr.push(0);
            // handle base case of no days left
            else if (j === d) innerArr.push(Infinity);
            // handle base case of not enough jobs to fill days
            else if (jd.length - i < d - j) innerArr.push(Infinity);
            // handle base case of one remaining job
            else if (i === jd.length - 1) innerArr.push(jd[jd.length - 1]);
            else innerArr.push(false);
        }
        memo.push(innerArr);
    }
    return memo;
}

const diff = minDifficulty([11, 111, 22, 222, 33, 333, 44, 444], 6);
console.log('result: ', diff);
const arr = [11, 111, 22, 222, 33, 333, 44, 444];
let sum = 0;
for (let i = 0; i < arr.length; i++) sum += arr[i];
console.log(sum);
console.log(sum - 333 - 44);
