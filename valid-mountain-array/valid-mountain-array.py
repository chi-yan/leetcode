class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) <= 2:
            return False
        
        i = 0
        j = len(arr) - 1
        
        while i + 2 <= len(arr) and arr[i+1] > arr[i]:
            
            i += 1
        print(i)
        while j >= 0 and arr[j] < arr[j-1]:
            j -= 1
        print(j)
        
        return i == j and i != 0 and  j != len(arr) - 1
