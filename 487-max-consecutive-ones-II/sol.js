/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    // initialize tracking variables
    let left = 0;
    let right = 0;
    let max = 0;
    // loop through array
    for (let i = 0; i < nums.length; i++) {
        // handle case of 0
        if (nums[i] === 0) {
            // handle case where new max is found
            if (left + right > max) max = left + right;
            // start new max consecutive count
            left = right + 1;
            right = 0;
        }
        // handle case of 1
        if (nums[i] === 1) {
            right++;
        }
    }
    // test most recent count for new max
    if (left + right > max) max = left + right;
    // return to calling function
    return max;
};