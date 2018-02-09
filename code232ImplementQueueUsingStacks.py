"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""
class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            
        return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            
        return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return (len(self.stack1)==0) and (len(self.stack2)==0)


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
print(obj.pop())
print(obj.empty())
obj.push(2)
obj.push(3)
print(obj.peek())