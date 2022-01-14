class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # define some convenient helper variables
        m = len(matrix)
        n = len(matrix[0])
        # start with a naive loop
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j]:
                            matrix[k][j] = None
                    for k in range(n):
                        if matrix[i][k]:
                            matrix[i][k] = None
        # loop back through and replace None with 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] is None:
                    matrix[i][j] = 0






# we will need to eventually check every element of the matrix, so time will
# most likely come out to O(mn)

# I keep thinking that recursion might be a worth-while approach
# when checking a elt, we want to know a couple things:
#   if the element is a "native" zero
#   if the element is a non-zero value that was already zero'd out
#   if the element is a non-zero value that has not been zero'd out (ignore)