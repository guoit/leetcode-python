"""
935 Knight Dialer

A chess knight can move as indicated in the chess diagram below:


This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46
 

Note:

1 <= N <= 5000
"""
class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        M = 10**9 + 7
        moves = [(4,6), (6,8), (7,9), (4,8), (0,3,9), (), (0,1,7), (2,6), (1,3), (2,4)] # moves[i] contains the previous dialing numbers moved to i
        pre, cur = [1]*10, [0]*10
        for _ in range(N-1):
            for dst in range(10):
                cur[dst] = 0
                for src in moves[dst]:
                    cur[dst] = (cur[dst] + pre[src])%M
            #pre = cur  # bug fixed: should do a deep copy
            pre[:] = cur[:]
        
        return sum(pre)%M

print(Solution().knightDialer(3))