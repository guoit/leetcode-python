"""
934 Shortest Bridge

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""
from collections import deque
class Solution:
    # improved solution
    # (1) color the first island to 2
    # (2) for the other island (color == 1), extract the boundaries to BFS queue
    # (3) BFS the other island's boundary until it touches island 2
    def shortestBridge(self, A):
        m, n, q = len(A), len(A[0]), deque()
        
        # dfs to color one of the island
        def markIsland(x, y, color):
            A[x][y] = color
            for x, y in (x, y-1), (x-1, y), (x, y+1), (x+1, y):
                if m > x >= 0 <= y < n and A[x][y] == 1:
                    markIsland(x, y, color)
        
        # iterate the matrix and color the first island, and push 2nd island's boarder coordinates to queue
        found = False # colored first island?
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    if not found:
                        markIsland(i, j, 2)
                        found = True
                    else:
                        touchWater = False # does this cell touch water?
                        for x, y in (i, j-1), (i-1, j), (i, j+1), (i+1, j):
                            if m > x >= 0 <= y < n and A[x][y] == 0:
                                touchWater = True
                                break
                        if touchWater:
                            q.append((i, j))
                    
        # BFS to touch the other island
        dist = 0
        while q:
            size = len(q)
            for _ in range(size):
                i, j = q.popleft()
                for x, y in (i, j-1), (i-1, j), (i, j+1), (i+1, j):
                    if m > x >= 0 <= y < n:
                        if A[x][y] == 2:
                            return dist
                        elif A[x][y] == 0:
                            q.append((x, y))
                            A[x][y] = 1
            dist += 1
                    
    # my own solution
    # use BFS to mark the first encountered island to 2, then put all the board cells (contact 0) of the island to a queue
    # next we will use another BFS to expand the island (marked as 2) outside, until it hits another island (marked as 1)
    def shortestBridge2(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]   # left, above, right, below
        Q, front = deque(), deque()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    # see a cell for a island, use BFS to mark all connected cells to 2
                    # in the BFS process, check if the cell connects to water (0), if so, it is a board cell, then we need to add it to front queue for further BFS
                    Q.append((i, j))
                    A[i][j] = 2
                    while Q:
                        x, y = Q.popleft()
                        isFront = False
                        for dx, dy in dirs:
                            p, q = x + dx, y + dy
                            if -1 < p < m and -1 < q < n:
                                if A[p][q] == 0:
                                    isFront = True
                                if A[p][q] == 1:
                                    Q.append((p, q))
                                    A[p][q] = 2
                        if isFront:
                            front.append((x, y))
                        #A[x][y] = 2 # mark this cell to 2
                    break   # inner break
            else:   # if no inner break, we continue to iterate to next i
                continue
            break   # outer break

        # use another BFS to expand the front until touches another island
        ans = 0
        while front:
            length = len(front)
            for i in range(length):
                i, j = front.popleft()                
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if -1 < x < m and -1 < y < n:
                        if A[x][y] == 1:    # front touches the other island
                            return ans
                        if A[x][y] == 0:
                            front.append((x, y))
                            A[x][y] = 2
                
            ans += 1

        # dummy return
        return ans

#A = [[0,1],[1,0]]
A = [[0,1,0],[0,0,0],[0,0,1]]
#A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
#A = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
print(Solution().shortestBridge(A))