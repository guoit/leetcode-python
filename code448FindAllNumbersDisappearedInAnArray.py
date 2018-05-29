"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution:
    # similar to problem 442, 1st pass mark corresponding index's value as negative, 2nd pass filter out the index with values > 0
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i,num in enumerate(nums):
            j = abs(num) - 1
            nums[j] = -abs(nums[j])
        
        return [(i+1) for i, num in enumerate(nums) if num > 0]

nums = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(nums))