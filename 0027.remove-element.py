class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums.append(val)
        nums.sort(key=lambda x: x == val)
        return nums.index(val)
