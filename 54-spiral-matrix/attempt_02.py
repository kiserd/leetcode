from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        vec_map = {
            (0, 1): (1, 0),
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1)
        }
        m = len(matrix)
        n = len(matrix[0])
        to_visit = set()
        for r in range(m):
            for c in range(n):
                to_visit.add((r, c))
        row = 0
        col = 0
        to_visit.remove((0, 0))
        vector = (0, 1)
        res = [matrix[0][0]]
        while to_visit:
            r_vec, c_vec = vector
            new_r = row + r_vec
            new_c = col + c_vec
            if (new_r, new_c) in to_visit:
                res.append(matrix[new_r][new_c])
                to_visit.remove((new_r, new_c))
                row = new_r
                col = new_c
            else:
                vector = vec_map[vector]
        return res
