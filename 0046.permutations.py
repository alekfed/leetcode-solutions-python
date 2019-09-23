import itertools


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        """
        return map(list, itertools.permutations(nums))
