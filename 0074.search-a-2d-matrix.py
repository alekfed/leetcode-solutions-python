import bisect
import functools


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        unfolded = functools.reduce(list.__add__, matrix, [])
        pos = bisect.bisect_left(unfolded, target)
        return pos < len(unfolded) and unfolded[pos] == target
