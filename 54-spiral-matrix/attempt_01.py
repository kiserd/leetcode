# could clean things up a bit, but want to move on -- get the point

class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        res = []
        row = 0
        col = 0
        v_row = 0
        v_col = 1
        while matrix[row][col] is not None:
            for line in matrix:
                print(line)
            res.append(matrix[row][col])
            matrix[row][col] = None
            if v_row == 0:
                if -1 < col + v_col < n and matrix[row][col + v_col] is not None:
                    col += v_col
                else:
                    if v_col:
                        v_row, v_col = v_col, v_row
                    else:
                        v_row, v_col = v_col, v_row
                    row += v_row
                    col += v_col
            else:
                if -1 < row + v_row < m and matrix[row + v_row][col] is not None:
                    row += v_row
                else:
                    if v_row:
                        v_col, v_row = -v_row, v_col
                    else:
                        v_col, v_row = v_row, v_col
                    col += v_col
                    row += v_row
        return res
        
            

