
# Python Data Types Examples

#single value data type (we can store only one single data in variable) 

#Integer
#the number without decimal point
age = 25
print("Age:", age)
print("Type of age:", type(age))
print()


#the number with decimal point
#Float
price = 99.99
print (price)
print(type(price))
print()

#complex
#complex number are combination of real part and imaginary part
a = 9+8j
print(a)
print(type(a))

#boolean
#these are used for defining yes or no.
b = True
print(b)
print (type(b))

# Multi value data type 

# String
'''
#string is a collection of individual element which are enclosed in a pair of quation marks
#in srting we can perform indexing and slicing 
#string is a immutable data type
#string is fixed length data type '''

name = " i love Python"
print(name)
print(type(name))

# List
'''
#list is collection of Homogeneous(we can store same data type)  and Heterogeneous(we can store difrent type data) data 
# list is mutable
# list is order collection data type
# list enclosed in square brakets[]
# list is variable length data type
#  in list we can perform indexing and slicing '''
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

# Tuple
'''
#tuple is collection of Homogeneous(we can store same data type)  and Heterogeneous(we can store difrent type data) data 
# tuple is immutable
# tuple is order collection data type
# in tuple comm(,)is mandatory
# fixed length data type
# in tuple we can perform indexing and slicing '''
t = (10, 'hai',20)
print(t)
print(type(t))

# Set
'''
#set is collection of Homogeneous(we can store same data type)  and Heterogeneous(we can store difrent type data) data 
each element saparetd by comma (,)
# set does not allow duplicates 
# set is randdom order collection data type
# in set we can't perform indexing and slicing 
# set is mutable data type 
# in set we can store immutable data type
# set is variable length data type
'''
s = {1, 2, 3, 4}
print(s)
print(type(s))

# Dictionary
'''
#dectionary is order collection of key and values pairs 
# in dectionary key and values are enclosed in pairs of curly barces{}
# each and every key values pairs are saparated by using comma(,)
# each and every values are saparated by using collon(:)
# dict is mutable data type
# in dict we cannot perform indeing and slicing'''
student = {"name": "vijay", "age": 22}
print(student)
print(type(student))


