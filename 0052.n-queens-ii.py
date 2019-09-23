class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def place_queens(col, board, ups, downs):
            if col == n:
                return 1
            num_solutions = 0
            for row in range(n):
                if row not in board and \
                        (row+col) not in ups and \
                        (row-col) not in downs:
                    board[col] = row
                    up = row + col
                    down = row - col
                    num_solutions += place_queens(col+1,
                                                  board[:],
                                                  ups | {up},
                                                  downs | {down})
            return num_solutions

        board = [-1] * n
        return place_queens(0, board, set(), set())
