class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x > 0) - (x < 0)
        str_wo_sign = str(sign*x)
        reversed_wo_sign = int(str_wo_sign[::-1])
        return sign*reversed_wo_sign * (reversed_wo_sign < 2 ** 31)
