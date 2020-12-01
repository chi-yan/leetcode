import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heapq.heapify(nums)
        #print(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums) 
            #print(nums)
        return nums[0]
