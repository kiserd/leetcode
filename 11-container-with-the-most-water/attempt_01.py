class Solution:
    def maxArea(self, height) -> int:
        max_vol = -1
        l = 0
        r = len(height) - 1
        while l < r:
            # potentially update max_vol
            max_vol = max(max_vol, (r - l) * min(height[l], height[r]))
            # update container walls for next iteration
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_vol

# less-than-rigorous proof. Should use contradiction.. mostly trying to tease
# out the concepts in my mind.

# Let l, r represent index of the left and right container walls.
# Let h_l and h_r represent heights of the left and right container walls.
# Let v_l,r represent the volume of the container formed by walls at the l and
# r indices

# Suppose h_l < h_r. We have v_l,r = (r - l) * h_l.

# Similarly, we have the following:

# v_l+1,r = (r - l - 1) * h_alpha   where 0 <= h_alpha <= h_r
# v_l,r-1 = (r - l - 1) * h_beta    where 0 <= h_beta  <= h_l

# v_l,r-1 <= v_l,r because r - l - 1  < r - l and 0 <= h_beta <= h_l

# Thus, moving the smallest container wall will always result in less volume