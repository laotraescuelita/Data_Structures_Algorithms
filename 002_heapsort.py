
def heapify(vector, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child
    right = 2 * i + 2  # Right child

    # Check if left child exists and is greater than root
    if left < n and vector[left] > vector[largest]:
        largest = left

    # Check if right child exists and is greater than root or left child
    if right < n and vector[right] > vector[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        vector[i], vector[largest] = vector[largest], vector[i]  # Swap
        # Heapify the root's affected subtree
        heapify(vector, n, largest)

def heap_sort( vector ):
    n = len(vector)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(vector, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        vector[i], vector[0] = vector[0], vector[i]  # Swap the root (max element) with the last element
        heapify(vector, i, 0)  # Heapify the reduced heap


vector = [70,50,30,10,20,40,60]
print("Unsorted vector:", vector)  # Print vector unsorted
heap_sort(vector)
print("Sorted vector:", vector)
