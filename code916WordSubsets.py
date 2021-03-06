"""
916 Word Subsets

We are given two arrays A and B of words.  Each word is a string of lowercase letters.
Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  
For example, "wrr" is a subset of "warrior", but is not a subset of "world".
Now say a word a from A is universal if for every b in B, b is a subset of a. 
Return a list of all universal words in A.  You can return the words in any order.

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
Output: ["apple","google","leetcode"]
Example 3:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
Output: ["facebook","google"]
Example 4:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
Output: ["google","leetcode"]
Example 5:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
Output: ["facebook","leetcode"]

Note:

1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j].
"""
from collections import Counter
class Solution:
    # my own solution, the idea is to pre-process B to get a counter map
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        # cnt is the overall count limit of all letters in b in B
        # for example, B = ["ec", "oc", "ceo"], cnt will be {c:1, e:1, o:1}
        cnt = Counter()
        for b in B:
            cntb = Counter(b)
            for char in cntb:
                cnt[char] = max(cnt[char], cntb[char])
        
        def check(word, cnt):
            # check if all letters' count in word is not smaller than cnt
            cnta = Counter(word)
            return all(cnta[char] >= cnt[char] for char in cnt) # bug fixed: changed from "for char in cnta"
        
        return [a for a in A if check(a, cnt)]

A, B = ["amazon","apple","facebook","google","leetcode"], ["lo","eo"]
print(Solution().wordSubsets(A, B))