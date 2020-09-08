"""
430 Flatten a Multilevel Doubly Linked List

You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 

Constraints:
Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
"""

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    # stack solution 1: push current node's next node to stack if not None, then push current's node's child node to stack if it is not None too.
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return None
        sentinel = Node(0)
        pre = sentinel
        pre.next = head
        head.prev = pre
        stack = [head]
        while stack:
            cur = stack.pop()
            pre.next = cur
            cur.prev = pre
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            pre = cur
        head.prev = None
        return sentinel.next
    # stack solution 2: push next node to stack if current node has child, then iterate to its child
    # when current node's next is None, and stack has nodes, pop node from stack and iterate to it.
    def flatten2(self, head: 'Node') -> 'Node':
        stack, node = [], head
        while node:
            if node.child:
                if node.next: stack.append(node.next)
                node.next = node.child                
                node.child.prev = node
                node.child = None
            elif node.next is None and stack:
                skipped = stack.pop()
                node.next = skipped
                skipped.prev = node
            node = node.next                
        return head