class Solution:
    def getRow(self, rowIndex: int):
        # build memo array
        prev_row = [1]
        i = 1
        while i < rowIndex + 1:
            curr_row = [None] * (i + 1)
            curr_row[0] = curr_row[-1] = 1
            j = 1
            while j < len(curr_row) - 1:
                curr_row[j] = prev_row[j - 1] + prev_row[j]
                j += 1
            prev_row = curr_row
            i += 1
        return prev_row