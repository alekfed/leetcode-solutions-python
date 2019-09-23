class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack, ans = [-1], 0

        for i, height in enumerate(heights):
            while height < heights[stack[-1]]:
                cur_h = heights[stack.pop()]
                cur_w = i - stack[-1] - 1
                ans = max(ans, cur_h * cur_w)
            stack.append(i)
        heights.pop()

        return ans
