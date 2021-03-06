"""
417 Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
from collections import deque
from heapq import heappush, heappop
class Solution:
    # Solution 1
    # BFS on pacific and atlantic
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        if m < 1: return []
        n = len(matrix[0])
        if n < 1: return []
        
        dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        mark = [[0]*n for _ in range(m)] # explanation of value: 0 means never visited, 1 means flows to pacitic, 2 means flow to atlantic, 3 means flows to both
        
        def bfs(q, mark, mask):
            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if -1 < i < m and -1 < j < n and matrix[i][j] >= matrix[x][y] and mark[i][j] & mask == 0:
                        mark[i][j] |= mask
                        q.append((i, j))
        
        q1, q2 = deque(), deque()
        for i in range(m):
            # left board elements to q1
            q1.append((i, 0))
            mark[i][0] |= 1
        for j in range(1, n):
            # top board elements [0][1:] to q1
            q1.append((0, j))
            mark[0][j] |= 1

        for i in range(m):
            q2.append((i, n-1))
            mark[i][n-1] |= 2
        for j in range(n-1):
            # bottom board elements [m-1][0:n-1] to q2
            q2.append((m-1, j))
            mark[m-1][j] |= 2        

        bfs(q1, mark, 1)
        bfs(q2, mark, 2)
        
        return [[x, y] for x in range(m) for y in range(n) if mark[x][y] == 3]

    # Solution 2
    # DFS
    def pacificAtlantic2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        m, n = len(matrix), len(matrix[0])
        mark = [[0]*n for _ in range(m)]    # explanation of value: 0 means never visited, 1 means flows to pacitic, 2 means flow to atlantic, 3 means flows to both

        # DFS pacific cells
        for i in range(m):
            mark[i][0] |= 0x01; # 1 means touching pacific
            self.dfs(matrix, m, n, neighbors, i, 0, mark, 0x01)

        for j in range(1, n):
            mark[0][j] |= 0x01; # 1 means touching pacific
            self.dfs(matrix, m, n, neighbors, 0, j, mark, 0x01)

        # DFS  atlantic cells
        for i in range(m):
            mark[i][n-1] |= 0x02; # 2 means touching atlantic
            self.dfs(matrix, m, n, neighbors, i, n-1, mark, 0x02)

        for j in range(n-1):
            mark[m-1][j] |= 0x02; # 1 means touching atlantic
            self.dfs(matrix, m, n, neighbors, m-1, j, mark, 0x02)

        return [[i, j] for i in range(m) for j in range(n) if mark[i][j]==3]        

    def dfs(self, matrix, m, n, neighbors, x, y, mark, mask):
        for dx, dy in neighbors:
            i, j = x + dx, y + dy
            if -1 < i < m and -1 < j < n and (mark[i][j] & mask == 0) and matrix[i][j] >= matrix[x][y]:
                mark[i][j] |= mask
                self.dfs(matrix, m, n, neighbors, i, j, mark, mask)
              

    # Solution 3
    # similar to trapping water II, using a priority queue (heapq in python) and do BFS
    # First add all pacific board cells into priority queue, then use priority queue + BFS to visit top cell's neighbors, mark them as "visited" but only push those celss with >= top cell's height into priority queue, also into the pacific set
    # do this again for atlantic 
    # finally get the intersection of the two sets and wrap the answer into list(list())
    # we need to think do we really need a priority queue here? we used a priority queue because without the priority queue, we marked a cell as "visited" and then we may not visit it next time we see it
    # For example in the example test case, where the cell [1][4] will be marked as "visited" when we visited the cell [0][4]'s neighbors, but because it has lower height
    # so cell [1][4] will not be added to the pacific set. This is wrong because it can flow to cell [1][3], then flow to [0][3], then pacific. We used the priority queue to address this issue
    # Now the question again: do we really need the priority queue?
    # The answer is no. We do not need to mark a cell as "visited" everytime we see it. We only mark it as visited when it has bigger height than the current one popping out from normal queue
    # Note this will not cause the BFS into a dead loop because there will be no heights can form a loop in the matrix. See the above solution using a normal queue
    def pacificAtlantic3(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        # pacific
        pacific = set()
        queue = []
        visited = set()
        for i in range(m):
            heappush(queue, (matrix[i][0], i, 0))
            pacific.add((i, 0))
            visited.add((i, 0))
        
        for j in range(1, n):
            heappush(queue, (matrix[0][j], 0, j))
            pacific.add((0, j))
            visited.add((0, j))

        self.bfs3(matrix, m, n, queue, neighbors, pacific, visited)
        #print(pacific)

        # atlantic
        queue.clear()
        visited.clear()
        atlantic = set()
        for i in range(m):
            heappush(queue, (matrix[i][n-1], i, n-1))
            atlantic.add((i, n-1))
            visited.add((i, n-1))
        
        for j in range(n-1):
            heappush(queue, (matrix[m-1][j], m-1, j))
            atlantic.add((m-1, j))
            visited.add((m-1, j))

        self.bfs3(matrix, m, n, queue, neighbors, atlantic, visited)
        #print(atlantic)

        return list(map(list, pacific & atlantic))

    def bfs3(self, matrix, m, n, queue, neighbors, ocean, visited):
        while queue:
            h, x, y = heappop(queue)
            for dx, dy in neighbors:
                i, j = x + dx, y + dy
                if -1 < i < m and -1 < j < n and (i, j) not in visited:
                    visited.add((i, j))
                    if h <= matrix[i][j]:
                        heappush(queue, (matrix[i][j], i, j))
                        ocean.add((i, j))

    # 8/13/2020
    # priority queue solution, TLE
    def pacificAtlantic4(self, matrix):
        m = len(matrix)
        if m < 1: return []
        n = len(matrix[0])
        if n < 1: return []
        dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        pacific, atlantic = set(), set()
        q1, q2 = [], [] # priority queue containing height and coordinates
        for i in range(m):
            # left board elements to q1
            q1.append((matrix[i][0], i, 0))
            # right board elements to q2
            q2.append((matrix[i][n-1], i, n-1))
        for j in range(1, n):
            # top board elements [0][1:] to q1
            q1.append((matrix[0][j], 0, j))
            # bottom board elements [m-1][0:n-1] to q2
            q2.append((matrix[m-1][n-1-j], m-1, n-1-j))
        
        heapify(q1)
        heapify(q2)
        
        def bfs(q, visited):
            while q:
                h, x, y = heappop(q)
                visited.add((x, y))
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if -1 < i < m and -1 < j < n and matrix[i][j] >= h and (i, j) not in visited:
                        heappush(q, (matrix[i][j], i, j))
        
        # BFS for pacific
        bfs(q1, pacific)
        # BFS for atlantic
        bfs(q2, atlantic)
        
        return list(pacific & atlantic)

#matrix = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1,1, 2, 4]]
matrix = [[3,3,3],[3,1,3],[0,2,4]]
obj = Solution()
print(obj.pacificAtlantic(matrix))