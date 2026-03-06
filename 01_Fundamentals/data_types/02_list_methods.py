# Python List Methods Example

# create list
numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)


# 1 append() – add element at end
numbers.append(60)
print("After append:", numbers)


# 2 extend() – add multiple elements
numbers.extend([70, 80])
print("After extend:", numbers)


# 3 insert() – insert element at specific index
numbers.insert(2, 25)
print("After insert:", numbers)


# 4 remove() – remove specific value
numbers.remove(30)
print("After remove:", numbers)


# 5 pop() – remove element using index
numbers.pop(3)
print("After pop:", numbers)


# 6 clear() – remove all elements
temp_list = [1, 2, 3]
temp_list.clear()
print("After clear:", temp_list)


# 7 index() – find index of element
print("Index of 40:", numbers.index(40))


# 8 count() – count occurrences
numbers.append(40)
print("Count of 40:", numbers.count(40))


# 9 sort() – sort list
numbers.sort()
print("After sort:", numbers)


# 10 reverse() – reverse list
numbers.reverse()
print("After reverse:", numbers)


# 11 copy() – copy list
copy_list = numbers.copy()
print("Copied list:", copy_list)
