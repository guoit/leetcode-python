"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
# Ask what to return if the input array is empty
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 1:
            return None
        res = nums[0]
        m = max(nums[0], 0)

        for j in range(1, len(nums)):
            m += nums[j]
            res = max(res, m)
            if m < 0:
                m = 0

        return res

obj = Solution()
test_cases = [[], [-199], [-1,-2,-3,-4,-5], [-2,1,-3,4,-1,2,1,-5,4]]
for case in test_cases:
    print(case, end = ' => ')
    print(obj.maxSubArray(case))