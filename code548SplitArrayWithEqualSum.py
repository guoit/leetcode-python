"""
548 Split Array with Equal Sum

Given an array with n integers, you need to find if there are triplets (i, j, k) which satisfies following conditions:

0 < i, i + 1 < j, j + 1 < k < n - 1
Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
where we define that subarray (L, R) represents a slice of the original array starting from the element indexed L to the element indexed R.
Example:
Input: [1,2,1,2,1,2,1]
Output: True
Explanation:
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
Note:
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].
"""
class Solution:
    # trick is to iterate j and then iterate i and k inside j loop
    # this way we can improve time to O(N^2)
    def splitArray(self, nums: List[int]) -> bool:
        n, sums = len(nums), [0]
        for num in nums: sums.append(sums[-1] + num)
        for j in range(3, n-3):
            left = set()
            for i in range(1, j-1):
                if sums[i] == sums[j] - sums[i+1]:
                    left.add(sums[i])
            for k in range(j+2, n-1):
                if sums[k] - sums[j+1] == sums[-1] - sums[k+1] and sums[k] - sums[j+1] in left:
                    return True
                
        return False