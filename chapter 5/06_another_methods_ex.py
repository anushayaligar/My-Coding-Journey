my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}
my_set.discard(10)  # No error even though 10 is not in the set
print(my_set)  # Output: {1, 3, 4}
removed_element = my_set.pop()
print(removed_element)  # Output: (Random element)
my_set.clear()
print(my_set)  # Output: set()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # Output: {3}
print(set1.difference(set2))  # Output: {1, 2}
print(set2.difference(set1))  # Output: {4, 5}
set3 = {1, 2}
print(set3.issubset(set1))  # Output: True
print(set1.issuperset(set3))  # Output: True
set4 = {6, 7, 8}
print(set1.isdisjoint(set4))  # Output: True
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}
set1 = {1, 2, 3}
set1.intersection_update(set2)
print(set1)  # Output: {3}
set1 = {1, 2, 3, 4}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}
set1 = {1, 2, 3}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}
