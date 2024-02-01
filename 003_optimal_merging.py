import heapq

def optimal_merge_pattern(files):
    # Use a min heap to keep track of file sizes
    heapq.heapify(files)
    total_cost = 0

    while len(files) > 1:
        # Extract the two smallest files from the heap
        smallest1 = heapq.heappop(files)
        smallest2 = heapq.heappop(files)

        # Merge the two smallest files and calculate the cost
        merged_file = smallest1 + smallest2
        total_cost += merged_file

        # Insert the merged file back into the heap
        heapq.heappush(files, merged_file)

    return total_cost

# Example usage:
file_sizes = [20, 30, 10, 5, 30]
total_merge_cost = optimal_merge_pattern(file_sizes)

print("Total Optimal Merge Cost:", total_merge_cost)
