class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        decimals = 1
        while x / decimals >= 10:
            decimals *= 10

        while x:
            left = x / decimals
            right = x % 10
            if left != right:
                return False

            x = (x % decimals) / 10
            decimals /= 100

        return True
