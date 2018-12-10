"""
898 Bitwise ORs of Subarrays

We have an array A of non-negative integers.

For every (contiguous) subarray B = [A[i], A[i+1], ..., A[j]] (with i <= j), we take the bitwise OR of all the elements in B, 
obtaining a result A[i] | A[i+1] | ... | A[j].

Return the number of possible results.  (Results that occur more than once are only counted once in the final answer.)

Example 1:

Input: [0]
Output: 1
Explanation: 
There is only one possible result: 0.
Example 2:

Input: [1,1,2]
Output: 3
Explanation: 
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:

Input: [1,2,4]
Output: 6
Explanation: 
The possible results are 1, 2, 3, 4, 6, and 7.
 

Note:

1 <= A.length <= 50000
0 <= A[i] <= 10^9
"""
class Solution:
    # my own solution, TLE
    def subarrayBitwiseORs_TLE(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        dp = [0]*N
        unique = set()

        for i in range(N):
            for j in range(i+1):
                dp[j] |= A[i]
                unique.add(dp[j])
        
        return len(unique)
    # https://leetcode.com/problems/bitwise-ors-of-subarrays/solution/
    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
#A = [0] # expect 1
A = [1,1,2] # expect 3
print(Solution().subarrayBitwiseORs(A))
"""
Intuition

Let's try to speed up a brute force answer. Evidently, the brute force approach is to calculate every result result(i, j) = A[i] | A[i+1] | ... | A[j]. We can speed this up by taking note of the fact that result(i, j+1) = result(i, j) | A[j+1]. Naively, this approach has time complexity O(N^2), where N is the length of the array.

Actually, this approach can be better than that. At the kth step, say we have all the result(i, k) in some set cur. Then we can find the next cur set (for k -> k+1) by using result(i, k+1) = result(i, k) | A[k+1].

However, the number of unique values in this set cur is at most 32, since the list result(k, k), result(k-1, k), result(k-2, k), ... is monotone increasing, and any subsequent values that are different must have more 1s in it's binary representation (to a maximum of 32 ones).

Algorithm

In the kth step, we'll maintain cur: the set of results A[i] | ... | A[k] for all i. These results will be included in our final answer set.
"""
