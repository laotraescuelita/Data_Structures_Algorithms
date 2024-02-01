class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from an empty queue")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("front from an empty queue")

    def size(self):
        return len(self.items)

# Example Usage:
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.items)  # Output: Queue: [1, 2, 3]
print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
print("Queue after dequeue:", queue.items)  # Output: Queue after dequeue: [2, 3]

queue.enqueue(4)
print("Front:", queue.front())  # Output: Front: 2
print("Queue size:", queue.size())  # Output: Queue size: 3
