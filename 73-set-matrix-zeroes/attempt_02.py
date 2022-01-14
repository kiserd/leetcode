# took a peek at the solution and it appears the best solution isn't anything
# revolutionary.
class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # define some convenient helper variables
        m = len(matrix)
        n = len(matrix[0])
        zero_first_row = False
        # start with a naive loop
        for i in range(m):
            if matrix[i][0] == 0:
                zero_first_row = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # loop back through and replace with 0's
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        if zero_first_row:
            for i in range(m):
                matrix[i][0] = 0






# we will need to eventually check every element of the matrix, so time will
# most likely come out to O(mn)

# I keep thinking that recursion might be a worth-while approach
# when checking a elt, we want to know a couple things:
#   if the element is a "native" zero
#   if the element is a non-zero value that was already zero'd out
#   if the element is a non-zero value that has not been zero'd out (ignore)