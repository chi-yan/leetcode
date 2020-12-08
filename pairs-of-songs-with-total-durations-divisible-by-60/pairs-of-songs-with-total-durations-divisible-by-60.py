class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        dict = defaultdict(int)
        count = 0
        for t in time:
            remaining = 60 - t % 60 
            if remaining == 60: remaining = 0
            if remaining in dict:
                count += dict[remaining]
            dict[t % 60] += 1
        print(dict)
        return count
             
            
