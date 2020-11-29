class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        def helper(valuesSoFar):
            if sum(valuesSoFar) == target:
                result.append(valuesSoFar)
            else:
                for number in candidates:
                    if valuesSoFar == [] or number >= valuesSoFar[-1]:
                        if sum(valuesSoFar) + number <= target:
                            helper(valuesSoFar + [number])
            
        helper([])
        return result
