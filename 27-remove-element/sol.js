/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    // work array from outside in
    let beg = 0;
    let end = nums.length - 1;
    let k = 0;
    // handle edge case
    if (nums.length == 1 && nums[0] !== val) k++;
    while (beg < end) {
        // handle case where elements both belong
        if (nums[beg] !== val && nums[end] == val) {
            beg++;
            k++;
            end--;
            if (beg == end && nums[beg] !== val) k++;
        }
        // handle case where only beginning belongs
        else if (nums[beg] !== val) {
            beg++;
            k++;
            if (beg == end && nums[beg] !== val) k++;
        }
        // handle case where only end belongs
        else if (nums[end] == val) end--;
        // handle case where elements need swapped
        else {
            const temp = nums[beg];
            nums[beg] = nums[end];
            nums[end] = temp;
            beg++;
            k++;
            end--;
            if (beg == end && nums[beg] !== val) k++;
        }
    }
    return k;
}