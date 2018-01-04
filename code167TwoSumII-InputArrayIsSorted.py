"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

"""
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i, j = 0, n-1
        while i < j:
            sum = numbers[i] + numbers[j]
            if target == sum:
                break
            elif target > sum:
                i += 1
            else:
                j -= 1
        
        return [i+1, j+1]

test_case = [2, 7, 11, 15]
obj = Solution()
print(obj.twoSum(test_case, 9))