"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
"""
# misunderstood the problem in 1st trial: requires two CONTINUOUS "L"
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ask about empty string
        return s.count('A') < 2 and s.find('LLL') == -1

test_cases = ['', 'PPALLP', 'PPALLL']
for s in test_cases:
    print(Solution().checkRecord(s))