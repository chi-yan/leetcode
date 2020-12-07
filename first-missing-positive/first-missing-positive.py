class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if nums == []:
            return 1
        li = [0 for _ in nums]
        for i in range(len(nums)):
            j = nums[i]
            if j-1 < len(li) and j-1 >= 0 :
                li[j-1] = j
        print(li)
        for i in range(len(li)):
            if li[i] != i+1 :
                return i+1
        return i+2
        
