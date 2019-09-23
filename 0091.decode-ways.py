class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        w = int(s > '')  # number of ways
        v = 0  # previous number of ways
        p = ''  # previous digit

        # d - digit
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d

        return w
