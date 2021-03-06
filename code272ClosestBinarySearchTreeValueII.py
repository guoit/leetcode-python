"""
272 Closest Binary Search Tree Value II -   not submitted
 
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
 

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Hint:

1. Consider implement these two helper functions:
　　i. getPredecessor(N), which returns the next smaller node to N.
　　ii. getSuccessor(N), which returns the next larger node to N.
2. Try to assume that each node has a parent pointer, it makes the problem much easier.
3. Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
4. You would need two stacks to track the path in finding predecessor and successor node separately.
"""
from TreeNode import *
from collections import deque
class Solution:
    # use inorder traversal list and fixed-size sliding window
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: list[int]
        """
        def G(root):
            if root:
                yield from G(root.left)
                yield root.val
                yield from G(root.right)
        
        q = deque()
        for num in G(root):
            if len(q) < k:
                q.append(num)
            else:
                if q and target - q[0] > num - target:
                    q.popleft()
                    q.append(num)
                else:
                    break
        
        return list(q)

lt, target, k = [5, 3, 7, 2, 4, 6, 8], 3, 2
root = ListToTree(lt)
PrintTree(root)
print(Solution().closestKValues(root, target, k))