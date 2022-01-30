class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4) -> int:
        # define function to build hash table for first half of lists
        def buildHash(nums_list, i, num):
            nonlocal sums
            # handle base case
            if i == len(nums_list) // 2:
                # handle case of updating existing num
                if -num in sums:
                    sums[-num] += 1
                # handle case of new num
                else:
                    sums[-num] = 1
            # iterate through potential sums recursively
            else:
                for elt in nums_list[i]:
                    buildHash(nums_list, i + 1, num + elt)

        # define function that counts complements from second half of lists
        def countHits(nums_list, i, num):
            nonlocal sums
            # handle base case, num from all lists included
            if i == len(nums_list):
                if num in sums:
                    return sums[num]
                else:
                    return 0
            # handle recursive exploration
            else:
                count = 0
                for elt in nums_list[i]:
                    # accumulate positive amount, hash is recorded as negative
                    count += countHits(nums_list, i + 1, num + elt)
                return count

        # kick off functions
        sums = {}
        # build hash table for first half of lists
        buildHash([nums1, nums2, nums3, nums3], 0, 0)
        # find matching opposite (complement) amounts from second half of lists
        return countHits([nums1, nums2, nums3, nums4], 2, 0)
