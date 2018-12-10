"""
908 Smallest Range I

Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 0
Explanation: B = [3,3,3] or B = [4,4,4]

Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""
class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        m1, m2 = -1, 10001
        for a in A:
            m1, m2 = max(m1, a), min(m2, a)
        
        if m1 - K <= m2 + K:
            return 0
        else:
            return m1 - m2 - 2*K

A = [0,10]
K = 2
print(Solution().smallestRangeI(A, K))