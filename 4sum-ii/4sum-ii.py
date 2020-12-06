from collections import defaultdict 
​
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        sums = defaultdict(int)
        for i in A:
            for j in B:
                sums[i+j] += 1
        #print(sums)
        count = 0
        for i in C:
            for j in D:
                if -i-j in sums:
                    count += sums[-i-j]
        return count
