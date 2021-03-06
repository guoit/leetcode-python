"""
485 Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
# similar problems: 1004 Max Consecutive Ones III
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, count = 0, 0
        for num in nums:
            if num:
                count += 1
            else:
                res = max(res, count)
                count = 0
        
        return max(res, count)

nums = []
print(Solution().findMaxConsecutiveOnes(nums))