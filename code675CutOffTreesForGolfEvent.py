"""
675 Cut Off Trees for Golf Event

You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:

0 represents the obstacle can't be reached.
1 represents the ground can be walked through.
The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. 
And after cutting, the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. 
If you can't cut off all the trees, output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.

Example 1:
Input: 
[
 [1,2,3],
 [0,0,4],
 [7,6,5]
]
Output: 6
Example 2:
Input: 
[
 [1,2,3],
 [0,0,0],
 [7,6,5]
]
Output: -1
Example 3:
Input: 
[
 [2,3,4],
 [0,0,5],
 [8,7,6]
]
Output: 6
Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
Hint: size of the given matrix will not exceed 50x50.
"""
# similar problems: 490 The Maze; 505 The Maze II
from collections import deque

class Solution:
    def cutOffTree_OJAccepted(self, forest):

        # Add sentinels (a border of zeros) so we don't need index-checks later on.
        forest.append([0] * len(forest[0]))
        for row in forest:
            row.append(0)

        # Find the trees.
        trees = [(height, i, j)
                for i, row in enumerate(forest)
                for j, height in enumerate(row)
                if height > 1]

        # Can we reach every tree? If not, return -1 right away.
        queue = [(0, 0)]
        reached = set()
        for i, j in queue:
            if (i, j) not in reached and forest[i][j]:
                reached.add((i, j))
                queue += (i+1, j), (i-1, j), (i, j+1), (i, j-1)
        if not all((i, j) in reached for (_, i, j) in trees):
            return -1

        # Distance from (i, j) to (I, J).
        def distance(i, j, I, J):
            now, soon = [(i, j)], []
            expanded = set()
            manhattan = abs(i - I) + abs(j - J)
            detours = 0
            while True:
                if not now:
                    now, soon = soon, []
                    detours += 1
                i, j = now.pop()
                if (i, j) == (I, J):
                    return manhattan + 2 * detours
                if (i, j) not in expanded:
                    expanded.add((i, j))
                    for i, j, closer in (i+1, j, i < I), (i-1, j, i > I), (i, j+1, j < J), (i, j-1, j > J):
                        if forest[i][j]:
                            (now if closer else soon).append((i, j))

        # Sum the distances from one tree to the next (sorted by height).
        trees.sort()
        return sum(distance(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees))

    # maze (BFS) method to get min steps from A to B with obstacles
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        m, n = len(forest), len(forest[0])
        # push tuple (heigh, i, j) into a list
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        # sort the list based on the height (unique)
        trees.sort()

        row, col = 0, 0
        steps = 0
        for h, i, j in trees:
            cnt = self.bfs(forest, row, col, i, j)
            if cnt == -1:
                return -1
            else:
                steps += cnt
                row, col = i, j
        
        return steps

    def bfs(self, forest, row, col, tree_row, tree_col):
        """
        row, col: current position
        tree_row, tree_col: target tree position
        return min steps from current position to target tree position
        """
        if (row, col) == (tree_row, tree_col):
            return 0

        m, n = len(forest), len(forest[0])
        steps = 0
        visited = [[False]*n for _ in range(m)]
        dirs = ((0,-1), (-1, 0), (0, 1), (1, 0))
        q = deque()
        q.append((row, col))
        visited[row][col] = True
        while q:
            steps += 1
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    i, j = x + dx, y + dy
                    if -1 < i < m and -1 < j < n and not visited[i][j] and forest[i][j] != 0:
                        if (i, j) == (tree_row, tree_col):
                            return steps
                        q.append((i, j))
                        visited[i][j] = True
                
        return -1


forest = [ [1,2,3], [0,0,4], [7,6,5] ]
print(Solution().cutOffTree(forest))