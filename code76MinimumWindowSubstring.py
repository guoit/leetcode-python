"""
76 Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""
# similar problems: 632 Smallest Range
# 8/10/2020
# typical counter-based sliding window problem
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        m, n = len(t), len(s)
        diff = Counter(t)
        start, end = 0, 0 # default values if no window exists
        i, req = 0, m
        for j in range(n):
            # add s[j] to window
            if s[j] in diff:
                diff[s[j]] -= 1
                if diff[s[j]] >= 0:
                    req -= 1
            # only update result when req is 0
            if req == 0:
                # shrink window until req == 1
                while i <= j and req == 0:
                    if s[i] in diff:
                        diff[s[i]] += 1
                        if diff[s[i]] > 0:
                            req += 1
                    i += 1
                # update result accordingly
                if end == start:
                    start, end = i-1, j+1
                elif end - start > j-i + 2:
                    start, end = i-1, j+1
        
        return s[start:end]

# previous more verbose solution
class Solution2(object):
    required = {} # count of each unique required character
    requires = 0 # count of all required characters
    def add(self, s, i):
        """
        Add a character into the window
        """
        if s[i] in self.required:
            self.required[s[i]] -= 1
            if self.required[s[i]] >= 0:    # There may be more than required number of this characters
                self.requires -= 1
    
    def remove(self, s, i):
        """
        Remove a character from the window
        """
        if s[i] in self.required:
            self.required[s[i]] += 1
            if self.required[s[i]] > 0:
                self.requires += 1

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return 0

        self.required.clear()
        self.requires = 0
        res = ''

        # Build the required count map
        self.requires = len(t)
        for c in t:
            if c in self.required:
                self.required[c] += 1
            else:
                self.required[c] = 1
        
        i = 0
        for (j, c) in enumerate(s):
            self.add(s, j)  # append the character to the window from right side
            if self.requires == 0: # the window contains all required characters, but we need to shrink the window by removing non-required characters from left
                while i <= j and self.requires == 0:
                    self.remove(s, i)
                    i += 1
                # After exiting while loop, i-1 is the correct index of the min window
                if self.requires == 1:
                    if not res or (j - i + 2) < len(res):   # bug fixed here: the length is j - i + 2, not j - i
                        res = s[i-1: j+1]
        
        return res

test_cases = [("cabwefgewcwaefgcf","cae")]
obj = Solution()
for case in test_cases:
    print(obj.minWindow(case[0],case[1]))

                
                    
