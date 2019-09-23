class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_index = 0
        for cur_index, num in enumerate(nums):
            if cur_index > max_index:
                return False
            max_index = max(max_index, cur_index + num)
        return True
