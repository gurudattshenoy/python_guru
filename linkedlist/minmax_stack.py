
# Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that sorts the given array. The functions should put all 0s first, then all 1s and all 2s in last.
# Constraint : We have to traverse the array only once and no additional space(Sort inline)
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# min() -- Retrieve the minimum element in the stack.
# max() -- Retrieve the maximum element in the stack.

class Stack:
    def __init__(self):
        self._items = []
        self._min_stack = []
        self._max_stack = []

    def isEmpty(self):
        return self._items == []

    def top(self):
        if not self.isEmpty():
            return self._items[-1]

    def push(self,data):
       if self.isEmpty():
           self._items.append(data)
           self._min_stack.append(data)
           self._max_stack.append(data)
       else:
           if self._min_stack[-1] > data:
                self._min_stack.append(data)
           else:
               self._min_stack.append(self._min_stack[-1])
           if self._max_stack[-1] < data:
               self._min_stack.append(data)
           else:
               self._max_stack.append(self._max_stack[-1])
           self._items.append(data)

    def min(self):
        return self._min_stack[-1]

    def max(self):
        return self._max_stack[-1]

    def pop(self):
        if self.isEmpty():
            raise ValueError("stack is empty")
        self._min_stack.pop()
        self._max_stack.pop()
        return self._items.pop()

    def display(self):
        return self._items

s = Stack()
s.push(12)
s.push(3)
s.push(4)
s.push(2)

s.push(2)
s.pop()


print(s.display())
print(s.min())
s.pop()
print(s.min())
print(s.max())
