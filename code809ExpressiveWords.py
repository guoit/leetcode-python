"""
809 Expressive Words

Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  
Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group are different.  
A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be extended in the second example.  
As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.

For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.  
Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, 
and add some number of the same character c to it so that the length of the group is 3 or more.  
Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave the group extended - ie., at least 3 characters long.

Given a list of query words, return the number of words that are stretchy. 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.
Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters
"""
class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        if not S:
            return 0

        def group(s):
            """
            group the same characters togeter, and return a list of tuples (letter, count)
            """
            res, cnt = [], 1
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    cnt += 1
                else:
                    res.append((s[i-1], cnt))
                    cnt = 1
            res.append((s[-1], cnt))

            return res

        gs, res = group(S), 0
        for word in words:
            gw = group(word)
            if len(gs) != len(gw):
                continue
            for i in range(len(gs)):
                s_letter, s_count = gs[i]
                w_letter, w_count = gw[i]
                if s_letter != w_letter or s_count < w_count or (s_count < 3 and s_count != w_count):
                    break
            else:
                res += 1
        
        return res

S = "heeellooo"
words = ["hello", "hi", "helo"]
print(Solution().expressiveWords(S, words))