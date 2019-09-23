class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 1.0

        while True:
            j = (i + x / i) / 2.0
            if abs(i - j) < 0.1:
                break
            i = j

        return int(j)
