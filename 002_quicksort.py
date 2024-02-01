def partition(vector, low, high):
    pivot = vector[high]  # Choose the last element as the pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if vector[j] < pivot:
            i += 1
            vector[i], vector[j] = vector[j], vector[i]  # Swap elements if smaller than the pivot

    vector[i + 1], vector[high] = vector[high], vector[i + 1]  # Place the pivot element in its correct position
    return i + 1  # Return the partitioning index

def quick_sort(vector, low, high):
    if low < high:
        # Partition the array and get the partitioning index
        pi = partition(vector, low, high)

        # Recursively sort elements before and after partition
        quick_sort(vector, low, pi - 1)
        quick_sort(vector, pi + 1, high)


vector = [70,50,30,10,20,40,60]
print("Unsorted vector:", vector)
quick_sort(vector, 0, len(vector)-1)
print("Sorted vector:", vector)
