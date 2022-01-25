class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # define a couple helper variables
        m = len(matrix)
        n = len(matrix[0])
        # if m == n == 1:
        #     return matrix[0][0] == target
        # define binary search function
        def bin(l, r):
            # handle unsuccessful base case
            if l > r:
                return False
            # convert linear midpoint to row x col
            mid = l + ((r - l) // 2)
            temp = mid
            row = 0
            col = n - 1
            while mid > n:
                row += 1
                mid -= n
            while mid > 0:
                col += 1
                mid -= 1
            col %= n
            # handle successful base case
            if matrix[row][col] == target:
                return True
            # handle recursive exploration
            if matrix[row][col] < target:
                return bin(temp + 1, r)
            else:
                return bin(l, temp - 1)
        return bin(1, m * n)



    