"""
1026 Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.
(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 
Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from TreeNode import *
class Solution:
    # my own DFS solution, tracking the pair of (min, max) for subtree
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def getBounds(node):
            lower, upper = node.val, node.val
            if node.left:
                lower1, upper1 = getBounds(node.left)
                self.res = max(self.res, abs(node.val - lower1), abs(node.val - upper1))
                lower, upper = min(lower, lower1), max(upper, upper1)
            if node.right:
                lower2, upper2 = getBounds(node.right)
                self.res = max(self.res, abs(node.val - lower2), abs(node.val - upper2))
                lower, upper = min(lower, lower2), max(upper, upper2)

            return (lower, upper)
        
        # main
        getBounds(root)
        return self.res

null = None
root = ListToTree([8,3,10,1,6,null,14,null,null,4,7,13])
print(Solution().maxAncestorDiff(root))
