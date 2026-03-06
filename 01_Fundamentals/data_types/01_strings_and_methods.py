# Python String Built-in Methods

## 1. lower()
#Converts the string into lowercase.

#Example:
s = 'HeLlO'
print(s.lower())

#Output:
#hello


## 2. upper()
#Converts the string into uppercase.

#Example:
s = 'hello'
print(s.upper())

#Output:
#HELLO


## 3. title()
#Converts the first letter of every word to uppercase.

#Example:
s = 'hElLo pythoN'
print(s.title())

#Output:
#Hello Python


## 4. capitalize()
#Converts only the first character of the string to uppercase.

#Example:
s = 'hello python'
print(s.capitalize())

#Output:
#Hello python


## 5. swapcase()
#Converts uppercase letters to lowercase and lowercase to uppercase.

#Example:
s = 'HeLLo'
print(s.swapcase())

#Output:
#hEllO


#-------------------------

# Boolean String Methods
#(Note: Methods starting with **is** return True or False)

## 6. islower()
#Returns True if the string is in lowercase.

#Example:
s = 'hello'
print(s.islower())

#Output:
#True


## 7. isupper()
#Returns True if the string is in uppercase.

#Example:
s = 'HELLO'
print(s.isupper())

#Output:
#True


## 8. istitle()
#Returns True if the string is in title case.

#Example:
s = 'Hello'
print(s.istitle())

#Output:
#True


## 9. isalpha()
#Returns True if the string contains only alphabets.

#Example:
s = 'hello'
print(s.isalpha())

#Output:
#True


## 10. isdigit()
#Returns True if the string contains only digits.

#Example:
s = '1234'
print(s.isdigit())

#Output:
#True


## 11. isalnum()
#Returns True if the string contains alphabets or digits.

#Example:
s = 'hello123'
print(s.isalnum())

#Output:
#True


## 12. isspace()
#Returns True if the string contains only spaces.

#Example:
s = '   '
print(s.isspace())

#Output:
#True


#-------------

# Checking Methods

## 13. startswith()
#Checks if the string starts with the given substring.

#Example:
s = 'hello'
print(s.startswith('h'))

#Output:
#True


## 14. endswith()
#Checks if the string ends with the given substring.

#Example:
s = 'hello'
print(s.endswith('o'))

#Output:
#True


#--------------

# Removing Spaces

## 15. strip()
#Removes spaces from both sides.

#Example:
s = '   hello   '
print(s.strip())

#Output:
#hello


## 16. rstrip()
#Removes spaces from the right side.

#Example:
s = 'hello   '
print(s.rstrip())

#Output:
#hello


## 17. lstrip()
#Removes spaces from the left side.

#Example:
s = '   hello'
print(s.lstrip())

#Output:
#hello


#------------------

# Splitting Strings

## 18. split()
#Splits the string into a list.

#Example:
s = 'hello python'
print(s.split())

#Output:
'''['hello', 'python']'''


## 19. rsplit()
#Splits from the right side.

#Example:
s = 'hello python'
print(s.rsplit())

#Output:
'''['hello', 'python']'''


#-------------------

# Replacing Text

## 20. replace()
#Replaces old substring with new substring.

#Example:
s = 'hello python'
print(s.replace('l','@'))

#Output:
#he@@o python


#-------------

# Counting and Searching

## 21. count()
#Counts occurrences of a substring.

#Example:
s = 'hello python hai'
print(s.count('h'))

#Output:
#3


## 22. index()
#Returns the index of the first occurrence.

#Example:
s = 'hello'
print(s.index('l'))

#Output:
#2


## 23. find()
#Returns index if found, otherwise -1.

#Example:
s = 'hello'
print(s.find('z'))

#Output:
#-1


#---------------

# Formatting

## 24. format / f-string
#Used to insert dynamic values.

#Example:
name = "Vijay"
print(f"Hello {name}")

#Output:
#Hello Vijay


#---------------------

# Joining

## 25. join()
#Joins elements with a specified character.

#Example:
s = 'hello'
print('.'.join(s))

#Output:
#h.e.l.l.o


#-----------------

# Partition

## 26. partition()
#Splits the string into three parts.

#Example:
s = 'hello python'
print(s.partition('o'))

#Output:
'''('hell', 'o', ' python')'''


## 27. rpartition()
#Splits from the right side.

#Example:
s = 'hello python'
print(s.rpartition('o'))

#Output:
'''('hello pyth', 'o', 'n')'''
