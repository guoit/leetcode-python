"""
385 Mini Parser

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        # not starting with '[' means only one integer, no list
        if s[0] != '[':
            return NestedInteger(int(s))

        sign, value = 1, 0
        stack = []
        for (i, c) in enumerate(s):
            if c == '-':
                sign = -1
            elif c == '[':  # create a NestedInteger object with empty list
                ni = NestedInteger()
                if stack:
                    stack[-1].add(ni)
                stack.append(ni)
            elif c == ']':
                if s[i-1].isdigit():   # a corner case about the second ']' of '[[1]]', and empty list'[]'
                    stack[-1].add(NestedInteger(sign*value))
                    value, sign = 0, 1
                res = stack.pop()   # s must end with ']'
            elif c == ',':
                if s[i-1].isdigit():   # corner case '[],[]'
                    stack[-1].add(NestedInteger(sign*value))
                    value, sign = 0, 1
            else:
                value = value*10 + ord(c) - ord('0')
        
        return res


"""
Input:
"[]"
Output:
[0]
Expected:
[]
"""

"""
Input:
"[123,456,[788,799,833],[[]],10,[]]"
Output:
[123,456,[788,799,833],0,[[]],0,10,[]]
Expected:
[123,456,[788,799,833],[[]],10,[]]
"""