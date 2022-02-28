class Solution:
    def matrixBlockSum(self, mat, k: int):
        # build cumulation matrix
        cumMat = [[None] * (len(mat[0])) for _ in range(len(mat))]
        cumMat[0][0] = mat[0][0]
        for j in range(1, len(mat[0])):
            cumMat[0][j] = mat[0][j] + cumMat[0][j - 1]
        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                if j != 0:
                    cumMat[i][j] = mat[i][j] + cumMat[i - 1][j] + cumMat[i][j - 1] - cumMat[i - 1][j - 1]
                else:
                    cumMat[i][j] = mat[i][j] + cumMat[i - 1][j]
        for row in cumMat:
            print(row)

        