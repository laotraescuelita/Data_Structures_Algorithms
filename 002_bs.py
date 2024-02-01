def binary_search(vector, target):
    # Initialize pointers for the start and end of the vector.
    left, right = 0, len(vector) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        # Check if the middle element is the target
        if vector[mid] == target:
            return mid
        # If the target is greater, ignore left half
        elif vector[mid] < target:
            left = mid + 1
        # If the target is smaller, ignore right half
        else: #vector[mid] > target:
            right = mid - 1

    # If the target is not found, return -1
    return -1


vector = [2, 4, 6, 8, 10, 12, 14, 16]
target = 14
result = binary_search(vector, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")
