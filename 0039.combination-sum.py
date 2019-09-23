class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(candidates, nums, rem):
            if rem == 0:
                result.append(nums)
            for i, cand in enumerate(candidates):
                if rem >= cand:
                    backtrack(candidates[i:], nums+[cand], rem-cand)

        candidates.sort()
        result = []
        backtrack(candidates, [], target)
        return result
