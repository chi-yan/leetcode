# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
         
        if root.left == None and root.right == None:
            return 0
        self.ans = 1
        def helper(root):
            if root == None:
                return 0
         
            left = helper(root.left) 
            right = helper(root.right)
            self.ans = max(self.ans, left+right+1)
            return max(left, right) + 1
        helper(root)
        return self.ans - 1
