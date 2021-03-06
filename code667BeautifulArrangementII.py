"""
667 Beautiful Arrangement II

Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 10^4.
"""
# similar problems: 526 Beautiful Arrangement
class Solution:
    # solution from http://www.cnblogs.com/grandyang/p/7577878.html
    # observe different results when n = 6
    # k = 1 ==> 1, 2, 3, 4, 5, 6
    # k = 2 ==> 6, 1, 2, 3, 4, 5
    # k = 3 ==> 1, 6, 2, 3, 4, 5
    # k = 4 ==> 6, 1, 5, 2, 3, 4
    # k = 5 ==> 1, 6, 2, 5, 3, 4
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        i, j = 1, n
        while i <= j:
            if k > 1:
                if k & 1:
                    res.append(i)
                    i += 1
                else:
                    res.append(j)
                    j -= 1
                k -= 1
            else:
                res.append(i)
                i += 1

        return res

    # help from http://www.cnblogs.com/grandyang/p/7577878.html and my own trial
    # think about how many possible absolute differences? always n - 1
    # try to form an array with max possible absolute differences: for example n =6: 1, 6, 2, 5, 3, 4, and we found the style is fetch numbers from two ends each time
    def constructArray_WRONG(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        i, j = 1, n
        res = []
        flag = 1 # determine to use i or j, actually we can also use (k--%2) as flag
        for _ in range(k):  # bug fixed: change from range(k-1) to range(k). Think about n = 3, k = 2
            if flag:
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
            flag ^= 1   # flip between 0 and 1

        res.extend(range(i, j+1))

        return res

# 2nd round on 9/13/2018 - need help

n , k= 6, 4
print(Solution().constructArray_WRONG(n, k))