class MinHeap:
    def __init__(self):
        #Vector to store all the elements.
        self.heap = []

    def parent(self, index):
        #Find the parent of the element related with index.
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return  2 * index + 2

    def insert(self, key):
        #Append the element at the end of the vector. 
        self.heap.append(key)
        #Index is the lenght of the vector minus one.
        index = len(self.heap) - 1

        # Swap the newly inserted element with its parent if it violates the min heap property
        while index > 0 and self.heap[self.parent(index)] > self.heap[index]:            
            self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
            index = self.parent(index)

    def heapify(self, index):
        smallest = index
        leftchild = self.left_child(index)
        rightchild = self.right_child(index)
        size = len(self.heap)

        if leftchild < size and self.heap[leftchild] < self.heap[smallest]:
            smallest = leftchild

        if rightchild < size and self.heap[rightchild] < self.heap[smallest]:
            smallest = rightchild

        if smallest != index:
            # Swap the root (index) with the smallest child if it violates the min heap property
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

    def extract_min(self):
        # If there´s no vector the process will be finished.
        if not self.heap:
            return None

        # The first element is the min element and it will be return as teh result. 
        min_element = self.heap[0]
        # By using the pop method we get the last element.  
        last_element = self.heap.pop()
        
        #After getting the last element we have to make sure there´s a vector.
        if self.heap:
            #last element is located in the first position.
            self.heap[0] = last_element
            # But since we made a change we have to respect the min heap rules that´s why we implement the methos heapify. 
            self.heapify(0)
        return min_element

    def get_min(self):
        return self.heap[0] if self.heap else None


vector = [70,50,30,10,20,40,60]
min_heap = MinHeap()
for i in vector:
    min_heap.insert( i )

print("Unsorted vector:", vector)  # Print vector unsorted
print("Min heap vector:", min_heap.heap)  # Print vector with min heap rules.
print("Min element:", min_heap.extract_min())  # Extract and print the minimum element
print("Min heap vector after extraction:", min_heap.heap)  # Print the vector after extraction
