"""
286 Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m < 1: return        
        INF, n = 2**31 - 1, len(rooms[0])
        Q = deque((i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0)
        
        dist = 0
        while Q:
            dist += 1
            size = len(Q)
            for _ in range(size):
                i, j = Q.popleft()
                for i, j in (i, j-1), (i-1, j), (i, j+1), (i+1, j):
                    if m > i >= 0 <= j < n and rooms[i][j] == INF:
                        Q.append((i, j))
                        rooms[i][j] = dist
    
    # FB follow up: find the shortest distance from top left to bottom right
    