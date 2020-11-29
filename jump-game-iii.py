class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        def helper(visited, position):
            print(position)
            if arr[position] == 0:
                return True
            if position in visited:
                return False
            else:
                visited.add(position)
                left = False
                right = False
                if position + arr[position] < len(arr):
                    left = helper(visited, position+arr[position])
                if position - arr[position] >= 0: 
                    right = helper(visited, position-arr[position])
