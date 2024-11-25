list_example = ["Mike", "John","Anna"]
tuple_example = ("Mike", "John","Anna")
set_example = {"Mike", "John","Anna"} # no duplicate elements and unordered

sorted_list = sorted(set_example)

# print(sorted_list)


import sys

# Memory comparison
my_list = [i for i in range(1000)]      # Moderate memory
my_tuple = tuple(my_list)                # Most efficient
my_set = {i for i in range(1000)}        # Highest memory

# print(f"List memory: {sys.getsizeof(my_list)} bytes")
# print(f"Tuple memory: {sys.getsizeof(my_tuple)} bytes")
# print(f"Set memory: {sys.getsizeof(my_set)} bytes")


# Try some set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# new_set = set1.union(set2) # elements in set1 or set2
# new_set = set1.intersection(set2) # elements in both set1 and set2
# new_set = set1.difference(set2) # elements in set1 but not in set2
# new_set = set1.symmetric_difference(set2) # elements in set1 or set2 but not in both
# new_set = set1.issubset(set2) # True if set1 is a subset of set2

# print(new_set)
