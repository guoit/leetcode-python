"""
500 Keyboard Row

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set('QWERTYUIOPqwertyuiop')
        row2 = set('ASDFGHJKLasdfghjkl')
        row3 = set('ZXCVBNMzxcvbnm')

        return [w for w in words if (set(w) <= row1 or set(w) <= row2 or set(w) <= row3)]

words = ["Hello", "Alaska", "Dad", "Peace"]
print(Solution().findWords(words))