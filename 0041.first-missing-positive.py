class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, elem in enumerate(nums):
            while 0 <= elem - 1 < len(nums) and nums[elem - 1] != elem:
                tmp = elem - 1
                elem, nums[tmp] = nums[tmp], elem

        for i, elem in enumerate(nums):
            if elem != i + 1:
                return i + 1

        return len(nums) + 1
