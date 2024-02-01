class MaxHeap:
    def __init__(self):
        #Vector to store all the elements.
        self.heap = []

    def parent(self, index):
        #Find the parent of the element related with index.
        return (index - 1) // 2

    def left_child(self, index):
        #Find the left child inthe tree of the element related with index.
        return 2 * index + 1

    def right_child(self, index):
        #Find the right child inthe tree of the element related with index.
        return  2 * index + 2

    def insert(self, key):
        #Append the element at the end of the vector. 
        self.heap.append(key)
        #Index is the lenght of the vector minus one.
        index = len(self.heap) - 1

        # Swap the newly inserted element with its parent if it violates the max heap property
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:            
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def heapify(self, index):
        largest = index
        leftchild = self.left_child(index)
        rightchild = self.right_child(index)        
        size = len(self.heap)

        if leftchild < size and self.heap[leftchild] > self.heap[largest]:
            largest = leftchild

        if rightchild < size and self.heap[rightchild] > self.heap[largest]:
            largest = rightchild

        if largest != index:
            # Swap the root (index) with the largest child if it violates the max heap property
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify(largest)

    def extract_max(self):
        # If there´s no vector the process will be finished.
        if not self.heap:
            return None

        # The first element is the max element and it will be return as the result. 
        max_element = self.heap[0]
        # By using the pop method we get the last element.  
        last_element = self.heap.pop()
        
        #After getting the last element we have to make sure there´s a vector.
        if self.heap:
            #last element is located in the first position.
            self.heap[0] = last_element
            # But since we made a change we have to respect the min heap rules that´s why we implement the methos heapify. 
            self.heapify(0)
        return max_element

    def get_max(self):
        return self.heap[0] if self.heap else None


vector = [70,50,30,10,20,40,60]
max_heap = MaxHeap()
for i in vector:
    max_heap.insert( i )

print("Unsorted vector:", vector)  # Print vector unsorted
print("Max heap vector:", max_heap.heap)  # Print vector with min heap rules.
print("Max element:", max_heap.extract_max())  # Extract and print the minimum element
print("Max heap vector after extraction:", max_heap.heap)  # Print the vector after extraction
