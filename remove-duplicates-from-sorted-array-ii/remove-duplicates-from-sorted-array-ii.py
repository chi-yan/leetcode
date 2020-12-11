class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        for i in range(2, len(nums)):
            print(i)
            while i < len(nums) and nums[i] == nums[i-2]: 
                del nums[i]
                print(nums)
                
        return len(nums)
