"""
581 Shortest Unsorted Continuous Subarray

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
class Solution:
    # my own solution: two passes. Scan left to right and find the left margin. Scan right to left and find the right margin. 
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        left = -1   # a virtual position with smallest integer
        for i in range(n):
            while left > -1 and nums[i] < nums[left]:
                left -= 1
            
            if left + 1 == i:   # handles duplicate
                left = i
            
        right = n
        for j in range(n-1, -1, -1):
            while right < n and nums[j] > nums[right]:
                right += 1
            
            if j + 1 == right: # handles duplicate
                right = j

        return max(0, right - left - 1) # think about [1, 1, 1], after two passes, left = 2, right = 0

nums = [2, 1,1, 1]
print(Solution().findUnsortedSubarray(nums))