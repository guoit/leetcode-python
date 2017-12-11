from TreeNode import *
"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        if root.left is None and root.right is None and root.val == sum:
            return True

        leftHasSum, rightHasSum = False, False
        
        if root.left is not None:
            leftHasSum = self.hasPathSum(root.left, sum - root.val)
        
        if root.right is not None:
            rightHasSum = self.hasPathSum(root.right, sum - root.val)
        
        return leftHasSum or rightHasSum


obj = Solution()
null = None
test_case = [5, 4, 8, 11, null, 13, 4, 7, 2, null, null, null, 1]
test_tree = ListToTree(test_case)
print(obj.hasPathSum(test_tree, 23))        
        