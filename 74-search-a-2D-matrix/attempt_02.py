from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        # start by finding row (if it exists)
        lr = 0
        hr = m - 1
        found_row = False
        while not found_row and lr <= hr:
            mr = (lr + hr) // 2
            if matrix[mr][0] <= target <= matrix[mr][n - 1]:
                found_row = True
            elif target < matrix[mr][0]:
                hr = mr - 1
            else:
                lr = mr + 1
        if not found_row:
            return False
        # next, find column (if it exists)
        lc = 0
        hc = n - 1
        while lc <= hc:
            mc = (lc + hc) // 2
            if matrix[mr][mc] == target:
                return True
            if matrix[mr][mc] < target:
                lc = mc + 1
            else:
                hc = mc - 1
        return False
