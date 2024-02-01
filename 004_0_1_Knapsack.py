def knapsack(weights, values, capacity):
    n = len(weights)

    # Initialize a table to store the maximum value for each subproblem
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]    

    # Fill the table using a bottom-up approach
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item can be included in the knapsack
            if weights[i - 1] <= w:
                # Choose the maximum value between including and excluding the current item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the current item's weight is more than the capacity, skip it
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find the selected items
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items[::-1]

# Example usage:
weights = [2, 3, 5, 7, 1, 4, 1]
values = [10, 5, 15, 7, 6, 18, 3]
capacity = 15

max_value, selected_items = knapsack(weights, values, capacity)

print("Maximum Value:", max_value)
print("Selected Items:", selected_items)
