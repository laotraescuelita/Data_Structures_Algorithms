import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if not self.is_empty():
            priority, item = heapq.heappop(self.heap)
            return item
        else:
            raise IndexError("pop from an empty priority queue")

    def peek(self):
        if not self.is_empty():
            priority, item = self.heap[0]
            return item
        else:
            raise IndexError("peek from an empty priority queue")

    def size(self):
        return len(self.heap)

# Example Usage:
priority_queue = PriorityQueue()

priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

print("Priority Queue Size:", priority_queue.size())  # Output: Priority Queue Size: 3
print("Peek:", priority_queue.peek())  # Output: Peek: Task 2

while not priority_queue.is_empty():
    print("Pop:", priority_queue.pop())
# Output:
# Pop: Task 2
# Pop: Task 3
# Pop: Task 1
