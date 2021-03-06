"""
384 Shuffle an Array

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""
# Fisher–Yates shuffle Algorithm
# https://www.geeksforgeeks.org/shuffle-a-given-array/
from random import randrange
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.output = nums[:]

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.output = self.nums[:]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        o = self.output
        n = len(o)
        for i in range(n-1):
            j = randrange(i, n)
            o[i], o[j] = o[j], o[i]

        return o

nums = list(range(8))
obj = Solution(nums)
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()