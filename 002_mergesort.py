def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector) // 2  # Find the middle index
        left_half = vector[:mid]  # Divide the array into two halves
        right_half = vector[mid:]

        # Recursive calls to merge_sort for each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves back together
        i = j = k = 0  # Initialize pointers for left_half, right_half, and merged array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                vector[k] = left_half[i]
                i += 1
            else:
                vector[k] = right_half[j]
                j += 1
            k += 1

        # Add remaining elements from left_half (if any)
        while i < len(left_half):
            vector[k] = left_half[i]
            i += 1
            k += 1

        # Add remaining elements from right_half (if any)
        while j < len(right_half):
            vector[k] = right_half[j]
            j += 1
            k += 1


vector = [70,50,30,10,20,40,60]
print("Unsorted vector:", vector)
merge_sort(vector)
print("Sorted vector:", vector)
