"""
947 Most Stones Removed with Same Row or Column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Example 3:

Input: stones = [[0,0]]
Output: 0
 

Note:

1 <= stones.length <= 1000
0 <= stones[i][j] < 10000
"""
class Solution:
    # Union find solution, better to understand
    def removeStones(self, stones):
        def find(root, i):
            while i != root[i]:
                i = root[i]
            return i
        
        n = len(stones)
        root = list(range(n))

        res = 0
        # union current stone with previous stones if they share row or column
        # note that we must check if i and j belongs to the same group before counting the removal
        # similar counting strategy is also used in 305 Number of Islands II
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    p, q = find(root, i), find(root, j)
                    if p != q:
                        root[p] = q
                        res += 1

        return res

    # https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O(N)
    # tricks: inverse bits of y, then put x and y into root map
    # problem becomes union find coordinates
    """
    When we search on points,
    we alternately change our view on a row and on a col.

    We think:
    a row index, connect two stones on this row
    a col index, connect two stones on this col.

    In another view：
    A stone, connect a row index and col.

    Have this idea in mind, the solution can be much simpler.
    The number of islands of points,
    is the same as the number of islands of indexes.
    """
    def removeStones2(self, points):
        UF = {}
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)
        return len(points) - len({find(x) for x in UF})
    # key: for all connected stones, eventually only 1 left after maximally removing other stones
    # so this is similar to 547 friend circles, we find out the number of groups of stones. Stones in a group are connected.
    def removeStones_WRONG(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        # union find and union are wrong
        def unionfind(X, Y, stones, i):
            """
            union find the root stone which connected to (x, y)
            return the index of the root stone in list "stones"
            """
            x, y = stones[i]
            if x in X:
                i = X[x]
                Y[y] = i
            elif y in Y:
                i = Y[y]
                X[x] = i
            else:
                X[x] = i
                Y[y] = i
            
            return i
        
        X, Y = {}, {}   # X and Y have keys of x and y coordinates, values of root stones' indices
        N, remain = len(stones), 0
        for i in range(N):
            j = unionfind(X, Y, stones, i)
            if j == i:
                remain += 1
        
        return N - remain

stones = [[1,0], [0, 1], [1,1]] #expect 2
print(Solution().removeStones(stones))