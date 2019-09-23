import itertools


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*(N+1) for i in range(M)] + [[0]*(N-1) + [1, 0]]
        for i, j in itertools.product(range(M-1, -1, -1), range(N-1, -1, -1)):
            dp[i][j] = (dp[i+1][j] + dp[i][j+1])*(1 - obstacleGrid[i][j])

        return dp[0][0]
