#Symmetric Difference: Returns elements that are in either of the sets, but not in both.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

sym_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print(sym_diff_set)  # Output: {1, 2, 4, 5}
 