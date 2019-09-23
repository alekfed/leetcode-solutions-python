class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [set() for i in range(target+1)]
        dp[0].add(())

        for num in candidates:
            for t in range(target, num-1, -1):
                for prev in dp[t-num]:
                    dp[t].add(prev + (num,))

        return sorted(list(dp[-1]))
