"""
67 Add Binary

Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

"""
import unittest
class Solution(object):
    decode = {'1':1, '0':0}
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or len(a) == 0:
            return b

        if not b or len(b) == 0:
            return a

        build = []
        carry = 0
        for k in range(max(len(a), len(b))):
            i = len(a) - 1 - k
            j = len(b) - 1 - k
            s = carry
            if i > -1:
                s += self.decode[a[i]]
            
            if j > -1:
                s += self.decode[b[j]]

            build.append(s%2)
            carry = s//2
        
        if carry > 0:
            build.append(carry)
        
        res = ''
        for k in range(len(build)):
            res += str(build.pop())

        return res

    # FB question: add two binary strings without using +, -, *, /
    # use bit operation, see https://leetcode.com/problems/add-binary/solution/
    def addBinary2(self, a, b):
        if not a or not b: return a or b
        x, y = int(a, 2), int(b, 2)
        while y:
            xor = x ^ y
            carry = (x&y) << 1
            x, y = xor, carry
        
        return bin(x)[2:]

class Test(unittest.TestCase):
    def test_1(self):
        test_cases = [('',''), ('','1'), ('0','0'), ('1','1'), ('1','0'), ('111111','1')]
        expected = ['', '1', '0', '10', '1', '1000000']
        obj = Solution()
        for i, case in enumerate(test_cases):
            self.assertEqual(obj.addBinary(*case), expected[i])

if __name__ == "__main__":
    unittest.main(exit=False)