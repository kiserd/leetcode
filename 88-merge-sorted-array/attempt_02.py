class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # process largest to smallest elements into nums1
        ptr1 = m - 1
        ptr2 = n - 1
        next_placement = n + m - 1
        while next_placement > -1:
            if ptr1 == -1:
                nums1[next_placement] = nums2[ptr2]
                ptr2 -= 1
            elif ptr2 == -1:
                nums1[next_placement] = nums1[ptr1]
                ptr1 -= 1
            elif nums1[ptr1] > nums2[ptr2]:
                nums1[next_placement] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[next_placement] = nums2[ptr2]
                ptr2 -= 1
            next_placement -= 1
