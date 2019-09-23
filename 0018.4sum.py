class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def findNsum(nums, target, N, result, results):
            if (len(nums) < N or
                    N < 2 or
                    target < nums[0]*N or
                    target > nums[-1]*N):
                return None

            if N == 2:
                left, right = 0, len(nums) - 1
                while left < right:
                    tmp_sum = nums[left] + nums[right]
                    if tmp_sum == target:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif tmp_sum < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:],
                                 target-nums[i],
                                 N-1,
                                 result+[nums[i]],
                                 results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)

        return results
