"""
547 Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""
from collections import deque
class Solution:
    # union find solution on 3/5/2019
    def findCircleNum_uf(self, M):
        N = len(M)
        root, res = [-1]*N, N

        # union find function
        def find(root, i):
            while -1 != root[i]:
                i = root[i]
            return i
        
        for i in range(N):
            for j in range(i+1, N):
                if M[i][j]:
                    p, q = find(root, i), find(root, j)
                    if p != q:
                        root[p] = q
                        res -= 1
        
        return res

    # DFS solution on 3/6/2019
    def findCircleNum_dfs(self, M):
        def dfs(M, i, visited):
            """
            DFS search for connected friends and mark them as visited
            """
            visited[i] = True
            for j in range(len(M)):
                if M[i][j] and not visited[j]:  # no need to check if j != i because if j == i, visited[j] will be True and it can't pass the "not visited[j]" check
                    dfs(M, j, visited)

        # main
        N, circles = len(M), 0
        visited = [False]*N
        for i in range(N):
            if not visited[i]:
                dfs(M, i, visited)
                circles += 1
        
        return circles

    # BFS solution on 3/6/2019
    def findCircleNum_bfs(self, M):
        N, circles = len(M), 0
        visited = [False]*N
        for i in range(N):
            if visited[i]:
                continue
            q = deque([i])
            visited[i] = True
            while q:
                i = q.popleft()
                for j in range(N):
                    if M[i][j] and not visited[j]:
                        q.append(j)
                        visited[j] = True
            
            circles += 1
        
        return circles

    # my 2nd trial
    # create a set to store students not processed
    # iterate all students, for each student in the set, use BFS to process all friends, and remove friends from the set
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N, circle = len(M), 0
        unvisited = set(range(N))
        q = deque()
        for i in range(N):
            # ignore those visited because they belong to existing circles
            if i in unvisited:
                unvisited.remove(i)
                circle += 1
                q.append(i)
                while q:
                    host = q.popleft()
                    for friend in range(N): # bug fixed: previously used range(host+1, N) but think about this: 0->9, 2->9, how can we make 0->2?
                        if M[host][friend] and friend in unvisited: # bug fixed: friend must be in unvisited, otherwise remove it from unvisited will raise key error exception
                            unvisited.remove(friend)
                            q.append(friend)
                
        return circle


    # 1st trial, iterate all cells of M, for each connection, use BFS to color indirect connections. The result is wrong because we missed those without friends
    def findCircleNum2(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        circle = 1  # id of the friend circle
        q = deque()
        for i in range(N):
            for j in range(i+1, N):
                if M[i][j] == 1:
                    circle += 1
                    q.append(i)
                    q.append(j)
                    M[i][j] = circle
                    while q:
                        host = q.popleft()
                        for k in range(host+1, N):
                            if M[host][k] == 1:
                                M[host][k] = circle
                                q.append(k)

        return circle - 1

M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
print(Solution().findCircleNum_bfs(M))