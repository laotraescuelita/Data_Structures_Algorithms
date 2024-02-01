def fractional_knapsack(profits, weights, capacity):
    # Calculate profits-to-weights ratio for each item
    ratio = [v / w for v, w in zip(profits, weights)]

    # Create a list of tuples (profits, weights, ratio) for each item
    items = [(v, w, r) for v, w, r in zip(profits, weights, ratio)]

    # Sort items based on the profits-to-weights ratio in descending order
    items.sort(key=lambda x: x[2], reverse=True)

    total_profits = 0
    knapsack = []

    for v, w, r in items:
        if capacity >= w:  # If the whole item can be taken
            knapsack.append((v, w, 1))  # Add the whole item to the knapsack            
            total_profits += v
            capacity -= w
        else:  # Take a fraction of the item to fill the capacity
            fraction = capacity / w
            knapsack.append((v, w, fraction))  # Add the fraction of the item to the knapsack
            total_profits += v * fraction
            break  # Capacity full, stop

    return total_profits, knapsack


profits = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]
knapsack_capacity = 15

max_profits, items_taken = fractional_knapsack(profits, weights, knapsack_capacity)
print("Maximum profits in the knapsack:", max_profits)
print("Items taken:")
for v, w, fraction in items_taken:
    print(f"profits: {v}, weights: {w}, Taken fraction: {fraction}")
