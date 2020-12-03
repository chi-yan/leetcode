# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.tree = TreeNode(0)
        self.createdTree = self.tree
        self.values = []
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def helper(node):
            if node is None:
                return
            if node.left:
                helper(node.left)
            self.values.append(node.val)
            print(node.val)
            if node.right:
                helper(node.right)
            
        helper(root)
        for i in range(len(self.values) - 1):
            self.createdTree.val = self.values[i]
            self.createdTree.right = TreeNode(0)
            self.createdTree = self.createdTree.right
        self.createdTree.val = self.values[-1]
        return self.tree
