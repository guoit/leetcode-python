"""
60 Permutation Sequence

The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""
class Solution(object):
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880] # factor of 0 to 9
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if k < 1 or k > self.fact[n]:
            return ''

        unused = list(range(1, n+1))
        res = ''
        while n > 0:
            digit = (k-1)//self.fact[n-1]
            res += str(unused[digit])
            
            k = (k - 1)%self.fact[n-1] + 1
            unused.pop(digit)
            n -= 1
        
        return res

# 2nd round solution on 9/19/2018
class Solution2:
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880] # factor of 0 to 9
    def getPermutation(self, n, k):
        k -= 1
        candidates = list(range(1, n+1))
        res = ''
        for i in range(1, n+1):
            index = k // self.fact[n-i]
            k %= self.fact[n-i]
            res += str(candidates[index])
            candidates.pop(index)
        
        return res

    # 9/3/2020
    def getPermutation2(self, n: int, k: int) -> str:
        nums = list(range(1, n+1)) # numbers to be fetched
        f = [1]*(n+1) # factorial list
        for i in range(2, n+1):
            f[i] = f[i-1]*i
        res = []
        k -= 1
        for i in range(1, n+1):
            idx = k // f[n-i]
            res.append(nums[idx])
            nums.pop(idx)
            k = k % f[n-i]

        return ''.join(map(str, res))

obj = Solution2()
n = 3
for i in range(obj.fact[n]):
    print(obj.getPermutation(n,i + 1))