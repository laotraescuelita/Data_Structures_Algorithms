class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)

# Example Usage:
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)  # Output: Stack: [1, 2, 3]
print("Pop:", stack.pop())    # Output: Pop: 3
print("Stack after pop:", stack.items)  # Output: Stack after pop: [1, 2]

stack.push(4)
print("Peek:", stack.peek())  # Output: Peek: 4
print("Stack size:", stack.size())  # Output: Stack size: 3
