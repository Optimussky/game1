# sets_compare.py

# Check if the list below has duplicate values
test_list = [1,2,3,4,5,2,3,4,5,6,7,8,9,10,11,12,13,14,15,12,13,14,15]

set1 = {1,2,3,4,4}
set2 = {4,5,6,7}


size = len(test_list)
print(f"Size: {size}")
no_duplicates = len(set(test_list))
print(f"No duplicates: {no_duplicates}")
compare = len(test_list) == len(set(test_list))
print(f"Compare, are equals?: {compare}")

print("set1.union(set2)")
print(set1.union(set2))

print("(set1 | set2)")
print(set1 | set2)

print("set1.intersection(set2)")
print(set1.intersection(set2))

print("(set1 & set2)")
print(set1 & set2)

print("(set1.difference(set2)")
print(set1.difference(set2))

print("(set1-set2)")
print(set1-set2)



