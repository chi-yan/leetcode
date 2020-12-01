class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
       
        output = set()
        s = sorted(nums)
  
        diff = float('inf')
        closestSum = 0
        for i in range(len(s)):
            j = i + 1
            k = len(s)-1
        
            while j < k:
            
                sum = s[i] + s[j] + s[k]
                if abs(target-sum) < diff:
                    diff = abs(target-sum)
                    closestSum = sum
                elif sum > target:
                    k -= 1
                else:
                    j += 1
        return(closestSum)        
