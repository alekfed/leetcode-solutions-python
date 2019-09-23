class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]

        for n in nums:
            perms = [p[:i] + [n] + p[i:]
                     for p in perms
                     for i in range((p + [n]).index(n) + 1)]

        return sorted(perms)
