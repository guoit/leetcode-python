"""
224 Basic Calculator

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.

"""
class Solution:
    # stack solution, when see a '(', push previous result and the sign before '('into stack, then evaluate the expression within '()'.
    # when seeing a ')', pop the previous result and sign out of stack, and continue evaluate the result
    # Be careful if a number is left in stack
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '+'
        stack = []
        res, num, sign = 0, 0, 1
        for c in s:
            if c.isdigit():
                num = num*10 + ord(c) - ord('0')
            elif c == '+':
                res += sign*num
                num, sign = 0, 1
            elif c == '-':
                res += sign*num
                num, sign = 0, -1
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res, sign = 0, 1
            elif c == ')':
                res += sign*num # value inside this '()'
                num = 0 # reset num                
                res *= stack.pop()
                res += stack.pop()

        return res
    # follow-up: stack only saves sign? https://www.1point3acres.com/bbs/thread-654010-1-1.html

    # generic solution, see OneNote
    def calculate_generic(self, s):
        l1, o1 = 0, 1
        stack, i = [], 0
        while i < len(s):
            if s[i].isdigit():
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                i = j - 1
            elif s[i] in ('+', '-'):
                l1 = l1 + o1 * num
                o1 = 1 if s[i] == '+' else -1
            elif s[i] == '(':
                stack.append((l1, o1))
                l1, o1 = 0, 1
            elif s[i] == ')':
                num = l1 + o1 * num
                l1, o1 = stack.pop()
                
            i += 1
        return l1 + o1 * num

    # recursive solution, add a number after parsing a number, or after evaluating a (...) part
    def calculate2(self, s):
        """
        :type s: str
        :rtype: int
        """        
        def eval(s, i):
            """
            evaluate expression starting from index i
            return result and next start position
            """
            res, num, sign = 0, 0, 1
            while i < len(s):
                # check if it is a '('
                if s[i] == '(':
                    num, i = eval(s, i+1)
                    res += sign*num
                    num, sign = 0, 1    # bug fixed: num is like a number, must reset num and sign
                    continue

                if s[i] == ')':
                    return (res, i+1)

                # check if it is a sign
                if s[i] == '-':
                    sign *= -1
                    i += 1
                    continue

                # check if it is a digit
                j = i
                while j < len(s) and s[j].isdigit():    # parse the number
                    num = num*10 + ord(s[j]) - ord('0')
                    j += 1

                if j > i:   # has a number, must add it to result and reset num and sign
                    res += sign*num
                    num, sign = 0, 1
                    i = j
                    continue
                
                # anything else like ' ', '+', just ignore it
                i += 1
            
            return (res, i)
        
        res, end = eval(s, 0)

        return res

    # 7/24/2020 recursive solution, TLE
    def calculate3(self, s):
        s += '+'
        sign, res, num = 1, 0, 0
        i = 0
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '+':
                res += sign*num
                num, sign = 0, 1
            elif c == '-':
                res += sign*num
                num, sign = 0, -1
            elif c == '(':
                # find the corresponding ')'
                cnt = 1
                for j in range(i+1, len(s)):
                    if s[j] == '(':
                        cnt += 1
                    elif s[j] == ')':
                        cnt -= 1
                        if cnt == 0:
                            break
                            
                num = self.calculate(s[i+1:j])
                i = j + 1
                continue
            i += 1
        
        return res        

test_case = '100-(-(2-34)+6 -(9))'
obj = Solution()
print(obj.calculate(test_case))
#print(obj.calculate2(test_case))
