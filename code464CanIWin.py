"""
464 Can I Win

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""
class Solution:
    # http://www.cnblogs.com/grandyang/p/6103525.html
    # tricks better than my solution: 1. use remaining, 2. "used" can represent all scenarios, so "used" can be the key in cache, no need to use tuple(sum_, next choose number)
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # precheck
        if (maxChoosableInteger >= desiredTotal): return True
        if desiredTotal > sum(range(1, maxChoosableInteger + 1)): return False

        def dfs(remain, used, mem):
            """
            remain: remaining to achieve desiredTotal
            used: each bit '1' represented that the position has been used
            mem: cache with key = used, value = win or not win            
            """
            if used in mem:
                return mem[used]

            for i in range(0, maxChoosableInteger):
                cur = 1 << i
                if (cur & used) == 0:
                    # i has not been used
                    if remain <= i+1 or not dfs(remain-i-1, used | cur, mem):
                        mem[used] = True
                        return True
                    
            mem[used] = False
            return False

        return dfs(desiredTotal, 0, {})

    # wrong solution
    def canIWin2(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        # pre-check
        if (maxChoosableInteger >= desiredTotal): return True
        if desiredTotal > sum(range(1, maxChoosableInteger + 1)): return False

        def dfs(sum_, used, mem):
            """
            sum_: previous sum
            used: 32-bit integer with positions 1 to maxChoosableInteger's bits initially set to 1. For each bit, 0 represents it has been used, 1 represents it has not been used
            mem: dict to cache the result, with key = (previous sum, currently selected number), value = win or not win for current player
            """
            # bug fixed: we should not use the below code to check win or not because this will forward win state to the other player
            # if sum_ >= maxChoosableInteger:
            #     return True
            # elif used == 0:
            #     return False

            for i in range(1, maxChoosableInteger + 1):
                if (1 << i) & used:
                    # number i has not been used by any player
                    # we should check if current player wins, with any possibility
                    if sum_ + i >= desiredTotal:    
                        return True

                    if (sum_, i) in mem:
                        win = mem[(sum_, i)]
                    else:
                        win = not dfs(sum_ + i, used^(1<<i), mem)   # current player's win state is the reverse of other play's win state
                        mem[(sum_, i)] = win    # cache result
                    
                    if win:
                        return True
            
            return False    # the current player will take any chance to win

        default_used = ((1 << (maxChoosableInteger + 1)) - 1)^1

        return dfs(0, default_used, {})

obj = Solution()
print(obj.canIWin2(10, 40))