# Python Type Casting

Type casting means converting one data type into another data type.

## 1. int()

Used to convert a value into integer.

Example:
x = "10"
y = int(x)

print(y)
print(type(y))

Output:
10
<class 'int'>


## 2. float()

Used to convert a value into float.

Example:
x = "10"
y = float(x)

print(y)

Output:
10.0


## 3. str()

Used to convert a value into string.

Example:
x = 10
y = str(x)

print(y)

Output:
'10'


## 4. bool()

Used to convert a value into boolean.

Example:
print(bool(1))   # True
print(bool(0))   # False
print(bool(""))  # False
print(bool("hi"))# True
