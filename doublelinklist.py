class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return

        last_node = self.head
        while last_node.next_node:
            last_node = last_node.next_node

        last_node.next_node = new_node
        new_node.prev_node = last_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head

        if self.head:
            self.head.prev_node = new_node

        self.head = new_node

    def delete(self, data):
        current_node = self.head

        while current_node and current_node.data != data:
            current_node = current_node.next_node

        if not current_node:
            return

        if current_node.prev_node:
            current_node.prev_node.next_node = current_node.next_node
        else:
            self.head = current_node.next_node

        if current_node.next_node:
            current_node.next_node.prev_node = current_node.prev_node

    def display_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next_node
        print("None")

    def display_backward(self):
        current_node = self.head
        while current_node and current_node.next_node:
            current_node = current_node.next_node

        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.prev_node
        print("None")

# Example Usage:
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.prepend(0)

doubly_linked_list.display_forward()  # Output: 0 <-> 1 <-> 2 <-> 3 <-> None
doubly_linked_list.display_backward()  # Output: 3 <-> 2 <-> 1 <-> 0 <-> None

doubly_linked_list.delete(2)
doubly_linked_list.display_forward()  # Output: 0 <-> 1 <-> 3 <-> None
doubly_linked_list.display_backward()  # Output: 3 <-> 1 <-> 0 <-> None
