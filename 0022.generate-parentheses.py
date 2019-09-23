class Solution(object):
    def generateParenthesis(self, n, opened=0):
        """
        :type n: int
        :rtype: List[str]
        """
        if n > 0 <= opened:
            return (['(' + p for p in self.generateParenthesis(n-1, opened+1)]
                   +[')' + p for p in self.generateParenthesis(n, opened-1)])

        return [')' * opened] * (not n)
