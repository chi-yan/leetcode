class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "": return []
        result = []
        
        dict = {'1':'0','2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz", '0':'0'}
        
        def helper(prefix, suffix):
            if len(prefix) == len(digits):
                result.append(prefix.replace('0',''))
            else:
                for letter in list(dict[suffix[0]]):
                    helper(prefix + letter, suffix[1:])
            
        helper("", digits)
        return result
