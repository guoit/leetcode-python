"""
765 Couples Holding Hands

N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
"""
class Solution:
    # Greedy solution, time O(N), space O(N)
    # for each row[i], try to find if its couple row[i+1] is next, otherwise swap row[i+1] with couple
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {num:i for i, num in enumerate(row)}
        res = 0
        for i in range(0, len(row), 2):
            if row[i] == row[i+1]^1:
                continue
            couple = row[i]^1
            nei = pos[couple]  
            # swap          
            row[i+1], row[nei] = row[nei], row[i+1]
            # update pos map
            pos[couple] = i+1
            pos[row[nei]] = nei
            res += 1
        
        return res

    # union find solution
    def minSwapsCouples(self, row: List[int]) -> int:
        def find(root, i):
            while i != root[i]:
                i = root[i]
            return i
        
        n = len(row)//2
        root = [i for i in range(n)]
        res = 0
        for i in range(0, len(row), 2):
            x, y = find(root, row[i]//2), find(root, row[i+1]//2)
            if x != y:
                res += 1
                root[x] = y
        
        return res    