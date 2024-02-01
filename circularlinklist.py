class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next_node = self.head
        else:
            current_node = self.head
            while current_node.next_node != self.head:
                current_node = current_node.next_node
            current_node.next_node = new_node
            new_node.next_node = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head

        current_node = self.head
        while current_node.next_node != self.head:
            current_node = current_node.next_node

        current_node.next_node = new_node
        self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        current_node = self.head
        prev_node = None

        while current_node.data != data:
            if current_node.next_node == self.head:
                return  # Data not found

            prev_node = current_node
            current_node = current_node.next_node

        if current_node == self.head:
            if current_node.next_node == self.head:
                self.head = None
            else:
                prev_node = self.head
                while prev_node.next_node != self.head:
                    prev_node = prev_node.next_node

                self.head = self.head.next_node
                prev_node.next_node = self.head
        else:
            prev_node.next_node = current_node.next_node

    def display(self):
        if not self.head:
            return

        current_node = self.head
        while True:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
            if current_node == self.head:
                break
        print(" (head)")

# Example Usage:
circular_linked_list = CircularLinkedList()
circular_linked_list.append(1)
circular_linked_list.append(2)
circular_linked_list.append(3)
circular_linked_list.prepend(0)

circular_linked_list.display()  # Output: 0 -> 1 -> 2 -> 3 ->  (head)

circular_linked_list.delete(2)
circular_linked_list.display()  # Output: 0 -> 1 -> 3 ->  (head)
