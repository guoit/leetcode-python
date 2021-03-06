"""
43 Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
# Should ask if num1 or num2 is empty
def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """ 
    m, n = len(num1), len(num2)
    res = [0]*(m+n)
    for i in range(m):
        for j in range(n):
            d1, d2 = ord(num1[m-1-i])-ord('0'), ord(num2[n-1-j]) - ord('0')
            res[i+j] += d1*d2
            
    carry = 0
    for k in range(m+n):
        res[k] += carry
        res[k], carry = res[k]%10, res[k]//10
        
    while res and res[-1] == 0:
        res.pop()
        
    return ''.join(map(str, reversed(res))) or '0'

test_cases = [('',''), ('1',''), ('0','0'), ('1','2'), ('12345','6789'), ('9999','999999')]
for case in test_cases:
    print(case[0], end = ' * ')
    print(case[1], end = ' = ')
    print(multiply(case[0], case[1]))