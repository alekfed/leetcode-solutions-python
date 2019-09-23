class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]

        for num in sorted(nums):
            result += [i+[num] for i in result if i+[num] not in result]

        return result
