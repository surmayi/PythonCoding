# Implement Stack using Array.
class myStack:
    # Please read sample.java file before starting.
    # Kindly include Time and Space complexity at top of each file
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return len(self.stack)==0
    #O(1)
    def push(self, item):
        self.stack.append(item)
    #O(1)
    def pop(self):
        return self.stack.pop()
    #O(1)
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def show(self):
        return self.stack

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())


# Time Complexity :
# Space Complexity :
# Did this code successfully run on Leetcode :
# Any problem you faced while coding this :


# Your code here along with comments explaining your approach