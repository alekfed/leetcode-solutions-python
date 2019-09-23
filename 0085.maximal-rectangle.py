class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res, hist_row = 0, ([0 for _ in matrix[0]]) if matrix else None

        for row_nums in matrix:
            stk = []
            for i, num in enumerate(row_nums):
                hist_row[i] = (hist_row[i] + 1) if num == '1' else 0

            for i, n in enumerate(hist_row + [0]):
                while stk and hist_row[stk[-1]] > n:
                    h = hist_row[stk.pop()]
                    res = max(res, h * ((i - stk[-1] - 1) if stk else i))
                stk.append(i)

        return res
