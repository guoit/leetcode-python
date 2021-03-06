"""
895 Maximum Frequency Stack 

Implement FreqStack, a class which simulates the operation of a stack-like data structure.

FreqStack has two functions:

push(int x), which pushes an integer x onto the stack.
pop(), which removes and returns the most frequent element in the stack.
If there is a tie for most frequent element, the element closest to the top of the stack is removed and returned.

Example 1:

Input: 
["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
Output: [null,null,null,null,null,null,null,5,7,5,4]
Explanation:
After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:

pop() -> returns 5, as 5 is the most frequent.
The stack becomes [5,7,5,7,4].

pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
The stack becomes [5,7,5,4].

pop() -> returns 5.
The stack becomes [5,7,4].

pop() -> returns 4.
The stack becomes [5,7].

Note:

Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
The total number of FreqStack.push calls will not exceed 10000 in a single test case.
The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
"""
# a stack pops the most frequent number or the number closest to top if tied
# https://leetcode.com/articles/maximum-frequency-stack/
from collections import defaultdict
class FreqStack(object):    
    def __init__(self):
        self.count = defaultdict(int)
        self.freq = defaultdict(list)
        self.maxFreq = 0

    def push(self, x):
        self.count[x] += 1
        self.maxFreq = max(self.maxFreq, self.count[x])
        self.freq[self.count[x]].append(x)        

    def pop(self):
        mx = self.maxFreq
        x = self.freq[mx].pop()
        self.count[x] -= 1
        if not self.freq[mx]:
            self.freq.pop(mx)
            self.maxFreq -= 1
            
        return x

obj = FreqStack()
for x in [5, 7, 5, 7, 4, 5]:
    obj.push(x)
for _ in range(6):
    print(obj.pop())