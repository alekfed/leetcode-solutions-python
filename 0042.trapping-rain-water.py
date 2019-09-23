class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        level = []
        left = 0

        for cur_height in height:
            left = max(left, cur_height)
            level += [left]

        right = 0

        for i, cur_height in reversed(list(enumerate(height))):
            right = max(right, cur_height)
            level[i] = min(level[i], right) - cur_height

        return sum(level)
