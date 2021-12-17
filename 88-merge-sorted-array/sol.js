/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    // temp variable to harbor potentially displaced nums1 elements
    let temp = [];
    for (let i = 0; i < m; i++) {
        temp.push(nums1[i]);
    }
    // indices tracking nums1 and temp current element
    let i = 0;
    let j = 0;
    // work through arrays sorting into nums1
    while (i < n || j < m) {
        if (j === m || nums2[i] < temp[j]) {
            nums1[i + j] = nums2[i];
            i++;
        }
        else {
            nums1[i + j] = temp[j];
            j++;
        }
    }
};