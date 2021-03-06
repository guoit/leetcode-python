from TreeNode import *
"""
111 Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Key is the definition of leaf node: it must be have both left and right child == None
class Solution:
    def __init__(self):
        self.MAX_INT = 2**31 - 1

    def _isLeaf(self, root):
        return root is not None and root.left is None and root.right is None

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        minDepth, level = 0, [root]
        while len(level) > 0:
            nextLevel = []
            for node in level:
                if self._isLeaf(node):
                    return minDepth + 1

                if node.left is not None:
                    nextLevel.append(node.left)
                
                if node.right is not None:
                    nextLevel.append(node.right)
                
            minDepth += 1
            level = nextLevel
        
        return minDepth

    # 2nd round solution on 11/26/2018
    def minDepth2(self, root):
        def depth(root):
            if not root:
                return self.MAX_INT
            
            lvalue, rvalue = depth(root.left), depth(root.right)

            if lvalue == self.MAX_INT and rvalue == self.MAX_INT:
                return 1
            else:
                return 1 + min(lvalue, rvalue)

        d = depth(root)
        return 0 if d == self.MAX_INT else d

obj = Solution()
null = None
test_case = [1,2]
test_tree = ListToTree(test_case)
print(obj.minDepth2(test_tree))        
        