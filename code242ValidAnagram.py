"""
242 Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return ''.join(sorted(s)) == ''.join(sorted(t))

s, t = 'anagram', 'nagaram'
obj = Solution()
print(obj.isAnagram(s, t))