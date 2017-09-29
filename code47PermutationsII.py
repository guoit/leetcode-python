"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
def _permuteUnique(nums, res, build, used, remain):
    if (remain == 0):
        res.append(build[:])
    else:
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue

            build.append(nums[i])
            used[i] = True
            _permuteUnique(nums, res, build, used, remain - 1)
            build.pop()
            used[i] = False

def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums or len(nums) < 1:
        return []

    nums.sort()

    used = [False]*len(nums)
    res = []
    _permuteUnique(nums, res, [], used, len(nums))

    return res

test_case = [1, 1, 2]
print(permuteUnique(test_case))        