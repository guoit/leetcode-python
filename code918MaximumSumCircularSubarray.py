"""
918 Maximum Sum Circular Subarray

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1

Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""
# similar problems: 53 Maximum Subarray
from collections import deque
class Solution:
    # the final result could be from (1) a subarray of A, or (2) a subarray with the end and first element
    # (1) can be solved with problem 53's method
    # (2) can be solved by finding the max of the sum of two lists: left_most and right_most
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # find the max sum of a subarray of A
        # same method as 53 Maximum Subarray
        pre, res, n = A[0], A[0], len(A)
        left_most, left = [0, A[0]], A[0]   # left_most[i] is the most sum for subarray starting with A[0] and length <= i
        right_most, right = [0, A[-1]], A[-1]   # right_most[i] is the most sum for subarray ending with A[-1] and length <= i
        for i in range(1, n):
            if pre < 0:
                pre = A[i]
            else:
                pre += A[i]
            res = max(res, pre)
            # update the left_most
            left += A[i]
            left_most.append(max(left_most[-1], left))
            # update the right_most
            right += A[n-i-1]
            right_most.append(max(right_most[-1], right))

        for i in range(1, n):
            res = max(res, right_most[i] + left_most[n-i])
        
        return res      

    # https://leetcode.com/problems/maximum-sum-circular-subarray/solution/
    # method 2, time O(N), space O(N)
    # mono-queue solution, by constructing a new list B = A + A
    # Assume P[i] is the sum of B[:i]
    # the result will be max of all P[j] - P[i] with j - i <= len(A)
    # we can maintain a mono-queue with ascending P value
    def maxSubarraySumCircular2(self, A):
        # trick to get the sum list
        P = [0]
        for _ in range(2):
            for a in A:
                P.append(P[-1] + a)
        
        q = deque([0])
        res = A[0]
        for j in range(1, len(P)):
            if j - q[0] > len(A):
                q.popleft()
            res = max(res, P[j] - P[q[0]])
            while q and P[q[-1]] >= P[j]:
                q.pop()
            
            q.append(j)
        
        return res

    # 1st trial, wrong solution
    # the final result could be from (1) a subarray of A, or (2) a subarray with the end and first element
    # this solution considers only one case of (2) by re-arranging two halves of A, but we need to consider other scenarios where the two parts have different length, a test case is [2,-2,2,7,8,0]
    def maxSubarraySumCircular3(self, A):
        def maxSum(A):
            pre, res = A[0], A[0]
            for i in range(1, len(A)):
                if pre < 0:
                    pre = A[i]
                else:
                    pre += A[i]
                res = max(res, pre)

            return res

        # main
        N = len(A)
        return max(maxSum(A), maxSum(A[N//2:]+A[:N//2]))

    # https://leetcode.com/problems/maximum-sum-circular-subarray/solution/
    # method 3, time O(N), space O(1)
    def maxSubarraySumCircular4(self, A):
        def kadane(gen):
            ans = cur = -2**31
            for x in gen:
                cur = x + max(cur, 0)
                ans = max(ans, cur)
            return ans
        
        S = sum(A)
        ans1 = kadane(iter(A))
        ans2 = S + kadane(-A[i] for i in range(1, len(A)))  # without the 1st element
        ans3 = S + kadane(-A[i] for i in range(len(A)-1))   # without the last element

        return max(ans1, ans2, ans3)

#A = [3,-1,2,-1]
#A = [1, 2, 3, 4]
#A = [-3000]
#A = [1,-2,3,-2]
#A = [2,-2,2,7,8,0]  #expected 19
A = [-2, -3, -1]
print(Solution().maxSubarraySumCircular4(A))