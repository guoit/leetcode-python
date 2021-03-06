"""
323 Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

     0          3

     |          |

     1 --- 2    4

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

     0           4

     |           |

     1 --- 2 --- 3

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

 Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""
# union find, same as 547 friend circles
class Solution:
    def countComponents(n, edges):
          def find(root, i):
               while i != root[i]:
                    i = root[i]
               return i

          root = list(range(n))
          cnt = n
          for a, b in edges:
               p, q = find(root, a), find(root, b)
               if p != q:
                    root[p] = q
                    cnt -= 1
          
          return cnt