class Solution:
    def sumSubarrayMins(self, arr):
        # append a zero to help with processing
        arr = [0] + arr
        # stack keeps track of indices
        s = [0]
        # array holding value for subarray ending in i
        res = [0] * len(arr)
        sum = 0
        for i in range(1, len(arr)):
            # we can continue popping values greater than our current value
            # because we only really need to use values smaller than our
            # current and our current val will be placed on the stack
            while arr[s[-1]] > arr[i]:
                s.pop()
            # now we have the index of the last val that was less than our
            # current element
            j = s[-1]
            # see discussion for explanation of this formula -- or below
            val =  res[j] + (i - j) * arr[i]
            res[i] = val
            s.append(i)
            sum += val
        return sum % (10**9 + 7)


# the most recent element (j) that is less than our current element (i) can
# be used to find the answer for (i).
# Since arr[j] is less than arr[i], the subarrays that are equal to those for
# i only have additional elements that do not factor into the min (we already
# know this). The other subarrays will only contain elements that are greater
# than arr[i], so we know the min for all of those is simply arr[i]

# obviously, take a look back at the discussion for an explanation complete
# with visuals and what-not