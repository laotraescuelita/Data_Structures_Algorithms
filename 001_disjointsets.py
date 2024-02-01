"""
The Disjoint-set data structure (also known as the Union-Find data structure) is commonly used to manage disjoint sets.
It offers two main operations:
Union: Combines two sets into a single set.
Find: Determines the set to which a particular element belongs and usually returns a representative element of that set.
"""

class DisjointSet:
    def __init__(self, size):
        # Initialize the Disjoint Set with given size        
        self.parent = [i for i in range(size)]  # vector to store parent of each element.
        self.rank = [0] * size  # Vector to store the rank of each element.
        
    def find(self, x):
        # Find operation with path compression
        if self.parent[x] != x:
            # If the current element's parent is not itself, set the parent to the representative of its set
            self.parent[x] = self.find(self.parent[x])  # Path compression            
        return self.parent[x]

    def union(self, x, y):
        # Union operation with union by rank
        root_x = self.find(x)  # Find the representative of x        
        root_y = self.find(y)  # Find the representative of y 

        if root_x != root_y:
            # If x and y are not already in the same set
            if self.rank[root_x] < self.rank[root_y]:
                # Attach the smaller rank tree under the root of the higher rank tree
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                # If ranks are the same, arbitrarily choose one as the parent and increase its rank
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


# Create a disjoint set with 5 elements
ds = DisjointSet(8)

# Initially, each element is in its own set
# Represented by [0, 1, 2, 3, 4, 5, 6, 7] (each index is its own set representative)

# Perform some unions:
ds.union(0, 1)
ds.union(2, 3)
#ds.union(4, 5)
#ds.union(6, 7)

ds.union(0, 3)
#ds.union(4, 7)

#ds.union(0, 7)


# Find representatives of elements after unions
for i in range(8):
    print(f"Element {i} belongs to set with representative: {ds.find(i)}")

print("rank", ds.rank)
print("parent", ds.parent)
