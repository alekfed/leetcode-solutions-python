class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ")" + s
        stack, ans = [], 0

        for index, element in enumerate(s):
            if element == ")" and stack and stack[-1][1] == "(":
                stack.pop()
                ans = max(ans, index - stack[-1][0])
            else:
                stack.append((index, element))

        return ans
