import bisect


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: len_numsist[int]
        :type target: int
        :rtype: bool
        """
        len_nums = len(nums)

        if len_nums <= 1:
            return target in nums

        if target in [nums[0], nums[-1]]:
            return True

        for i in range(len_nums-1):
            if nums[i] == target:
                return True
            if nums[i] > nums[i+1]:
                break

        if nums[i] <= nums[i+1]:
            return False

        i_targ = ((bisect.bisect_left(nums[i+1:len_nums] + nums[:i+1],
                                      target) + i + 1) % len_nums)

        return nums[i_targ] == target
