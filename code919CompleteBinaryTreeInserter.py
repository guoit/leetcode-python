"""
919 Complete Binary Tree Inserter

A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;
CBTInserter.get_root() will return the head node of the tree.

Example 1:

Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output: [null,1,[1,2]]
Example 2:

Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output: [null,3,4,[1,2,3,4,5,6,7,8]]

Note:

The initial given tree is complete and contains between 1 and 1000 nodes.
CBTInserter.insert is called at most 10000 times per test case.
Every value of a given or inserted node is between 0 and 5000.
 """

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import *
from collections import deque
# my own solution using an auxilary array similar to binary heap implementation
# parent's index is p, then children's index is 2*p and 2*p+1
# root's index is always 1
class CBTInserter:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.array = [None]
        Q = deque([root])
        while Q:
            node = Q.popleft()
            self.array.append(node)
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        parent = self.array[len(self.array)//2]
        node = TreeNode(v)
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
        self.array.append(node)

        return parent.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.array[1]

import collections
# better solution from OJ with less space (O(logN))
# BFS based solution with a deque which has: from the first non-complete nodes to the end
class CBTInserter_OJ(object):
    def __init__(self, root):
        self.deque = collections.deque()
        self.root = root
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v):
        node = self.deque[0]
        self.deque.append(TreeNode(v))
        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.popleft()
        return node.val

    def get_root(self):
        return self.root

root = ListToTree([1,2,3,4,5,6])
#obj = CBTInserter(root)
obj = CBTInserter_OJ(root)
print(obj.insert(7))
print(obj.insert(8))
PrintTree(obj.get_root())

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()