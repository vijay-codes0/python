# Python Dictionary Methods Example

# create dictionary
student = {
    "name": "Vijay",
    "age": 22,
    "course": "Python"
}

# get() – returns value of a key
print(student.get("name"))

# keys() – returns all keys
print(student.keys())

# values() – returns all values
print(student.values())

# items() – returns key-value pairs
print(student.items())

# update() – updates dictionary
student.update({"age": 23})
print(student)

# pop() – removes element using key
student.pop("course")
print(student)

# popitem() – removes last inserted item
student.popitem()
print(student)

# setdefault() – returns value if key exists, otherwise adds key
student.setdefault("city", "Bangalore")
print(student)

# copy() – creates copy of dictionary
copy_dict = student.copy()
print(copy_dict)

# clear() – removes all elements
temp = {"a": 1, "b": 2}
temp.clear()
print(temp)