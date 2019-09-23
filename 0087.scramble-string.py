class Solution(object):
    def isScramble(self, s1, s2, memo={}):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False

        length = len(s1)
        dp = [
            [[False] * (length+1) for i in range(length)]
            for j in range(length)
        ]

        for k in range(1, length+1):
            for i in range(0, length+1-k):
                for j in range(0, length+1-k):
                    if k == 1:
                        dp[i][j][k] = s1[i] == s2[j]
                    else:
                        for q in range(1, k):
                            if dp[i][j][k]:
                                break
                            else:
                                dp[i][j][k] = dp[i][j][q] and \
                                    dp[i+q][j+q][k-q] or \
                                    dp[i][j+k-q][q] and \
                                    dp[i+q][j][k-q]

        return dp[0][0][length]
