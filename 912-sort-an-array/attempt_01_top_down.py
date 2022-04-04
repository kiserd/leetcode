class Solution:
    def sortArray(self, nums):
        # define merge sort function
        def merge_sort(arr):
            # handle base case
            if len(arr) < 2:
                return arr
            # handle recursive case
            mid = (len(arr) - 1) // 2
            left = merge_sort(arr[:mid+1])
            right = merge_sort(arr[mid+1:])
            return merge(arr, left, right)

        def merge(arr, left, right):
            # merge the sorted lists together
            idx = 0
            left_ptr = 0
            right_ptr = 0
            while idx < len(arr):
                # handle case of no more right elements
                if right_ptr == len(right):
                    arr[idx] = left[left_ptr]
                    left_ptr += 1
                # handle case of no more left elements
                elif left_ptr == len(left):
                    arr[idx] = right[right_ptr]
                    right_ptr += 1
                elif left[left_ptr] < right[right_ptr]:
                    arr[idx] = left[left_ptr]
                    left_ptr += 1
                else:
                    arr[idx] = right[right_ptr]
                    right_ptr += 1
                idx += 1
            return arr
        return merge_sort(nums)