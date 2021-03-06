"""
467 Unique Substrings in Wraparound String

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""
class Solution:
    # http://www.cnblogs.com/grandyang/p/6143071.html
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count, base, length = [0]*26, ord('a'), 0
        for i in range(len(p)):
            if i > 0 and ord(p[i]) - ord(p[i-1]) in (1, -25):
                length += 1
            else:
                length = 1
            
            index = ord(p[i]) - base
            count[index]  = max(count[index], length)

        print(count)
        return sum(count)

    # wrong solution, consider p = 'abaab', where 'ab' were calculated twice
    def findSubstringInWraproundString2(self, p):
        """
        :type p: str
        :rtype: int
        """
        i, j, res = 0, 1, 0
        while j < len(p):
            diff = ord(p[j]) - ord(p[j-1])
            if diff not in (1, -25):
                n = j - i
                res += n*(n-1)//2
                i = j
            j += 1
        
        n = j - i
        res += n*(n-1)//2 + len(set(p))

        return res

obj = Solution()
#p = 'abaab'
p = 'abzdebcdef'
print(obj.findSubstringInWraproundString(p))