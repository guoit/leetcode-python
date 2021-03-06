"""
403 Frog Jump

A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
"""

class Solution:
    # DP solution
    def canCross(self, stones: List[int]) -> bool:
        dp = {} # dp[pos] contains a set of last jump size
        for pos in stones:
            dp[pos] = set()
        dp[0].add(0)
        
        for pos in stones:
            for k in dp[pos]:
                for nxt in range(pos+k-1, pos+k+2):
                    if nxt > pos and nxt in dp:
                        dp[nxt].add(nxt - pos)
        
        return len(dp[stones[-1]]) > 0

    # 9/5/2020
    # DFS + HashMap
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        pos = {num: i for i, num in enumerate(stones)}
        def helper(stones, start, k, memo):
            if start == len(stones) - 1:
                return True
            if (start, k) in memo:
                return memo[(start, k)]
            cur = stones[start]
            res = False
            for nxt in range(cur + k - 1, cur + k + 2):
                if nxt > cur and nxt in pos:
                    res |= helper(stones, pos[nxt], nxt - cur, memo)
            memo[(start, k)] = res
            return res
        
        memo = {}
        return helper(stones, 0, 0, memo)

    # DFS + HashMap
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        if not stones:  # ask this corner case
            return False
        
        def dfs(cur, k, ss, mem):
            if cur == stones[-1]:
                return True
            elif cur < stones[-1]:
                if (cur, k) in mem:
                    return mem[(cur, k)]
                else:
                    res = False
                    for offset in range(-1,2):
                        next = cur + k + offset
                        if next > cur and next in ss:
                            res = res or dfs(next, k+offset, ss, mem)
                    
                    mem[(cur, k)] = res
                    return res
            else:
                return False

        ss, mem = set(stones), {}
        return dfs(0, 0, ss, mem)

stones = [0,1,3,5,6,8,12,17]
obj = Solution()
print(obj.canCross(stones))