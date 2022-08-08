public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // init helper dict
        Dictionary<int, int> helper = new Dictionary<int, int>();
        // iterate through array in search of hit
        for (int i = 0; i < nums.Length; i++) {
            // handle case where successful pair was already added
            int prior_idx;
            if (helper.TryGetValue(nums[i], out prior_idx)) {
                int[] res = new int[2];
                res[0] = prior_idx;
                res[1] = i;
                return res;
            }
            // handle case where no hit found
            else {
                helper[target - nums[i]] = i;
            }
        }
        int[] dummy_res = {-1, -1};
        return dummy_res;
    }
}