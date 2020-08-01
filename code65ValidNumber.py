"""
65 Valid Number

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
"""
import unittest
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = False  # digits appeared
        numAfterE = True # if no 'e', this is always True, if 'e' appears, this will be set to False when 'e' appears, but digits appearance will set it to True after e
        dot = False # dot appears
        exp = False # e appears

        s = s.strip()
        for i in range(len(s)):
            if s[i] == ' ': # any whitespace in s is valid
                return False
            elif s[i] in ('+', '-'): # sign can only appear in s[0], or after e
                if i > 0 and s[i-1] != 'e':
                    return False
            elif s[i].isdigit():
                num = True
                numAfterE = True
            elif s[i] == '.': # dot cannot appear more than once, cannot appear after 'e'
                if dot or exp:
                    return False
                dot = True
            elif s[i] == 'e':
                if exp or not num: # 'e' cannot appear more than once, cannot appear before digits
                    return False
                exp = True
                numAfterE = False
            else:
                return False

        # digit must appear, and cannot end with 'e'
        return num and numAfterE

class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        self.assertFalse(obj.isNumber('9e'))
        self.assertTrue(obj.isNumber('e9'))

if __name__ == "__main__":
    unittest.main(exit=False)