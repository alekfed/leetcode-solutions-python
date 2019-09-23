class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        i, j = 0, len(height)-1

        while j-i > 0:
            if height[i] < height[j]:
                tmp_area = (j-i)*height[i]
                i += 1
            else:
                tmp_area = (j-i)*height[j]
                j -= 1

            if tmp_area > area:
                area = tmp_area

        return area
