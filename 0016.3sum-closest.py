class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1
            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                if tmp_sum == target:
                    return tmp_sum

                if abs(tmp_sum - target) < abs(result - target):
                    result = tmp_sum

                if tmp_sum < target:
                    j += 1
                elif tmp_sum > target:
                    k -= 1

        return result
