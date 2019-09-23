from collections import Counter


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def pre_check():
            """Checks whether board has all the required characters."""
            chars_required = Counter(word)

            for row in board:
                for char in row:
                    if char in chars_required and chars_required[char] > 0:
                        chars_required[char] -= 1

            for count in chars_required.values():
                if count > 0:
                    return False
            return True

        def path_exists(char_ind, x, y):
            """DFS checking for path existence."""
            if board[x][y] != word[char_ind]:
                return False
            if char_ind == l - 1:
                return True

            char_ind += 1

            board[x][y] = None

            # Check each possible direction
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_x, next_y = x + d[0], y + d[1]
                # Only explore the move if it's valid
                # and hasn't already been explored
                if (-1 < next_x < m and
                        -1 < next_y < n and
                        board[next_x][next_y]):
                    if path_exists(char_ind, next_x, next_y):
                        return True

            # Change the board back to its original character
            board[x][y] = word[char_ind - 1]
            return False

        # Initial Checks
        if not board:
            return False
        if not word:
            return True
        if not pre_check():
            return False

        # Check paths starting from each character in the board
        m, n, l = len(board), len(board[0]), len(word)
        for i in range(m):
            for j in range(n):
                if path_exists(0, i, j):
                    return True

        # False if no such path exists.
        return False
