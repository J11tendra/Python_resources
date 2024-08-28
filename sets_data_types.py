# Sets are mutable collection of unique elements.
# Remember - 1 is True and 0 is False

nums = {1, 2, 23, 23, 14, 15, 17}

print(nums)
print(type(nums))

num_1 = { 1, 2, 76, 34, 232, 234, 12}
num_2 = { 12, 3, 46, 6}

num_1.intersection_update(num_2)
num_1.symmetric_difference_update(num_2)
num_1.symmetric_difference(num_2)
num_1.difference_update(num_2)
print(num_1)

odd_num = {1, 3, 5, 7, 9}
even_num = {2, 4, 6, 8, 10}
natural_num = odd_num.union(even_num)

print(natural_num)
print(even_num)
print(odd_num)
