"""
966 Vowel Spellchecker

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.
For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

Note:
1 <= wordlist.length <= 5000
1 <= queries.length <= 5000
1 <= wordlist[i].length <= 7
1 <= queries[i].length <= 7
All strings in wordlist and queries consist only of english letters.
"""
class Solution:
    # use set "origin" to store origin words
    # use dict "capital" to store lower-case word and its most left index
    # use dict "vowel" to store lower-case word with all vowels replaced by 'a' and its most left index
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: list[str]
        """
        def replaceA(s):
            return ''.join('a' if c in 'aeiou' else c for c in lower)   # don't use c in ('a', 'e', 'i', 'o', 'u')

        origin, capital, vowel = set(), {}, {}
        for i in range(len(wordlist)-1, -1, -1):    # the other option is to iterate from left to right and use dict's setdefault method, which will only set the value once
            origin.add(wordlist[i])
            lower = wordlist[i].lower()
            capital[lower] = i
            vowel[replaceA(lower)] = i

        res = []
        # bug fixed: forgot to process q to lower and vowel-replaced
        for q in queries:
            if q in origin:
                res.append(q)
                continue

            lower = q.lower()
            if lower in capital:
                res.append(wordlist[capital[lower]])
                continue

            replace = replaceA(lower)
            if replace in vowel:
                res.append(wordlist[vowel[replace]])
            else:
                res.append("")
        
        return res

wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
print(Solution().spellchecker(wordlist, queries))