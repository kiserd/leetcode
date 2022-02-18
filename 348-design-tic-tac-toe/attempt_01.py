class TicTacToe:

    def __init__(self, n: int):
        self.rows = [{1: 0, 2: 0} for _ in range(n)]
        self.cols = [{1: 0, 2: 0} for _ in range(n)]
        self.diag_1 = {1: 0, 2: 0}
        self.diag_2 = {1: 0, 2: 0}
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        # handle processing for row and column
        self.rows[row][player] += 1
        if self.rows[row][player] == self.n:
            return player
        self.cols[col][player] += 1
        if self.cols[col][player] == self.n:
            return player
        # handle diagonals
        if row == col:
            self.diag_1[player] += 1
            if self.diag_1[player] == self.n:
                return player
        if row == self.n - col - 1:
            self.diag_2[player] += 1
            if self.diag_2[player] == self.n:
                return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)