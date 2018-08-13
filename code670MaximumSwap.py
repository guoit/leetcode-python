"""

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 10^8]
"""
class Solution:
    # my own solution
    # convert num to string, then for every digit s[i], try to find a bigger digit on its right side
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        n = len(s)
        for i in range(n-1):
            for j in range(i+1, n):
                if s[i] < s[j]:
                    a = list(s)
                    a[i], a[j] = a[j], a[i]
                    return int(''.join(a))
        
        return num

test_cases = [0, 12, 2736, 9973, 1111, 9867]
obj = Solution()
for num in test_cases:
    print(num, end = ' -> ')
    print(obj.maximumSwap(num))