"""
55 Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
# Ask what's the result for empty list
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 2:
            return True
        i, max_s = 1, nums[0]

        while max_s < len(nums) - 1:
            temp = max_s
            while i <= max_s:
                temp = max(temp, i + nums[i])
                i += 1
            if temp == max_s: # no increase
                return False
            else:
                max_s = temp
        
        return True
    def canJump2(self, nums):
        # pre_end: the max achievable index in last leap
        # end: the max achievable index in current leap
        pre_end, end, N = 0, 0, len(nums)-1
        i = 0
        while end < N:
            # try all possible leaps to extend "end"
            while i <= pre_end:
                end = max(end, i+nums[i])
                i += 1
            # check if end > pre_end
            if end == pre_end:
                # we cannot go further
                return False
            else:
                pre_end = end
        
        return True

test_cases = [[],[0],[1],[2,3,1,1,4],[3, 2, 1, 0, 4],[1,1,1,1,0],[1,0,3,2],[5,0,0,0,0,0]]
obj = Solution()
for case in test_cases:
    print(case, end = ' -> ')
    print(obj.canJump2(case))