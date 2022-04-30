class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # define recursive outer helper function
        def process(tl, br):
            while br > tl:
                rotate(tl, br)
                tl += 1
                br -= 1

        # define inner helper function
        def rotate(tl, br):
            for offset in range(br - tl):
                temp = matrix[tl][tl + offset]
                matrix[tl][tl + offset] = matrix[br - offset][tl]
                matrix[br - offset][tl] = matrix[br][br - offset]
                matrix[br][br - offset] = matrix[tl + offset][br]
                matrix[tl + offset][br] = temp

        # kick off function(s)
        process(0, len(matrix[0]) - 1)
