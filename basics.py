#
# # Answer in Float
# print(7/3)
#
# #Answer - Quotiet only
# print(7//3)
#
# #Answer - Reminder only
# print(7%3)
#
# # 5 to the power 3
# print(5**3)
#
# #boolean
# type(True)

# None value
# print (type(None))

#
# # Strings
# print(type("Hello"))
# print(type("'Hello'"))
#
# #Float
# print(type(1.5))
#
# #int
# print(type(1))
#
# #List- Can store any datatypes in sequence- Mutable
grocery_list=["banana","orange","Pineapple"]
# print(type(grocery_list))
#
# #tuples - same like List but immutable.
grocery_tuples=("banana","orange","Pineapple")
# print(type(grocery_tuples))

#Relational Operators --   >,<, <=, >=, !=, ==(value only), ===(value and Datatype)
# Logical Operators -- and or not()
# incrementing operator --  +=, -=


# for item in grocery_list:
#     print (item)
#
# for item in grocery_tuples:
#     print (item)
#
# for i in range(0,3):
#     print(grocery_list[i])
#
# for i in range(len(grocery_list)):
#     print(grocery_list[i])
#
# for i,item in enumerate(grocery_list):
#     print(i, "-", item)

# while loop
# j= len(grocery_tuples)-1
# while j>=0:
#     print(grocery_tuples[j])
#     j-=1
#
# # To print in reverse order
# text = "Hello, World!"
# for i in range(len(text) - 1, -1, -1):  # Start from the last index to 0
#     print(text[i], end="")
#
# for char in reversed(text):
#     print(char, end="")

# if False:
#     print(1)
# elif False:
#     print(2)
# else:
#     print(3)

# x = 10
# y = 20
# z = 5
#
# if (x > 5 and y > 15) or not (z > 10):
#     print("Complex condition is True")  # This will be printed
# else:
#     print("Complex condition is False")


# "is" keyword is used for comparing the memory location
a=[1,2,3]
b=a
c=[1,2,3]
# print(a is b)  #True because a and b are referring to same location
# print(a is c) #True because a and c are referring to different location
a.append(4)
# appending 4 to a impacts b as well because they both are referring to same location
# print(a)
# print(b)

# If I want to have a copy of "a" but in a different location
# d=a.copy()
# print(a is d)
# print(a)
# print(d)

# If I want to have a copy of "a" but in a different location
from copy import deepcopy
f=deepcopy(a)
print(a is f)

print(chr(65))
print(chr(97))
print(ord('A'))
print(ord('a'))