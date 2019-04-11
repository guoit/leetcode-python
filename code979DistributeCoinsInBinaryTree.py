"""
979 Distribute Coins in Binary Tree

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

Example 1:
Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.

Example 3:
Input: [1,0,2]
Output: 2

Example 4:
Input: [1,0,0,null,3]
Output: 4

Note:

1<= N <= 100
0 <= node.val <= N
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.moves = 0
        def dfs(node):
            """
            return the number of coins need to move to parent
            if the result is positive, this means there are extra coins in this subtree, which need to move to parent
            if the result is negative, this means this subtree needs that amount of coins from parent
            """ 
            if not node:
                return 0
            
            move = dfs(node.left) + dfs(node.right) + node.val - 1
            self.moves += abs(move)
            return move
        
        # main
        dfs(root)
        return self.moves

#tree = [3, 0, 0]    # expect 2
#tree = [1]  # expect 0
#tree= [0, 3, 0] # expect 3
tree = [1, 0, 2] # expect 2
root = ListToTree(tree)
print(Solution().distributeCoins(root))