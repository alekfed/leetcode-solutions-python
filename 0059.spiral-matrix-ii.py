class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix, lo = [], n*n+1

        while lo > 1:
            lo, hi = lo - len(matrix), lo
            matrix = [range(lo, hi)] + zip(*matrix[::-1])

        return matrix
