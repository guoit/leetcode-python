"""
591 Tag Validator

Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. 
A code snippet is valid if all the following rules hold:

The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. 
The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.
Valid Code Examples:
Input: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

Output: True

Explanation: 

The code is wrapped in a closed tag : <DIV> and </DIV>. 

The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 

Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.

So TAG_CONTENT is valid, and then the code is valid. Thus return true.


Input: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

Output: True

Explanation:

We first separate the code into : start_tag|tag_content|end_tag.

start_tag -> "<DIV>"

end_tag -> "</DIV>"

tag_content could also be separated into : text1|cdata|text2.

text1 -> ">>  ![cdata[]] "

cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"

text2 -> "]]>>]"


The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.
Invalid Code Examples:
Input: "<A>  <B> </A>   </B>"
Output: False
Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.

Input: "<DIV>  div tag is not closed  <DIV>"
Output: False

Input: "<DIV>  unmatched <  </DIV>"
Output: False

Input: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
Output: False

Input: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
Output: False

Input: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
Output: False
Note:
For simplicity, you could assume the input code (including the any characters mentioned above) only contain letters, digits, '<','>','/','!','[',']' and ' '.
"""
# similar problems: 224, 227 Basic Calculator; 32, 301 Parentheses
class Solution(object):
    # help from http://www.cnblogs.com/grandyang/p/7016476.html
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        stack, i = [], 0
        while i < len(code):
            if i > 0 and not stack: # last tag should match first tag, for example <A></A><B></B>
                return False

            # note the sequence of if statements, we should start from "<![CDATA[", then "</", then "<"
            if code[i:i+9] == "<![CDATA[":
                j = i + 9
                i = code.find("]]>", j)
                if i < 0:
                    return False
                i += 2
            elif code[i:i+2] == "</":
                j = i + 2
                i = code.find(">", j)
                if i < 0:
                    return False
                tag = code[j:i]
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
            elif code[i:i+1] == "<":
                j = i + 1
                i = code.find(">", j)
                if i < 0 or i == j or i - j > 9:
                    return False
                tag = code[j:i]
                for char in tag:
                    if ord(char) < ord('A') or ord(char) > ord('Z'):
                        return False
                #if tag.upper() != tag: # bug fixed: compare upper case only cannot guarantee that all characters are 'A-Z'
                    #return False                    
                stack.append(tag)
            
            i += 1

        return not stack

#code = "<A></A><B></B>" # expected: False because the last tag should match the first tag
code = "<A<></A<>" # expected: False
obj = Solution()
print(obj.isValid(code))            