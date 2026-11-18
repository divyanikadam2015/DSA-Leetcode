class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                live = 0

                for x in range(max(0, i-1), min(m, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        if board[x][y] == 1 or board[x][y] == 2:
                            live += 1

                if board[i][j] == 1:
                    live -= 1

                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = 2

                elif board[i][j] == 0 and live == 3:
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == 3:
                    board[i][j] = 1