/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    // initialize variable to track next open spot
    let nextAvailable = 1;
    // loop through nums, placing distinct elts at beginning
    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i - 1]) {
            nums[nextAvailable] = nums[i];
            nextAvailable++;
        }
    }
    return nextAvailable;
};