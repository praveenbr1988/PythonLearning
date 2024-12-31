import math
from operator import truediv, index

print("welcome to python")
course_fee=800 #immutable. It will still be present in memory
course_fee=850
print("Course fee is- ", course_fee)
"""
This is a multi 
line comment
"""

#5 Simple DataTypes
instructor_name="Sumit Mittal"
course_fee=850
course_Rating=4.5
is_starting_soon=True
total_income=None  #NULL


print(type(instructor_name))
print(type(course_fee))
print(type(course_Rating))
print(type(is_starting_soon))
print(type(total_income))

print(instructor_name+"1") #concatenation operator for string
print(course_fee+1)
print(course_fee+1.5)
print(instructor_name+"1")

#typecasting
course_fees="600"
print(int(course_fees))

print("----"*9)
first_name="Praveen"
last_name="BR"
print(f"My firstname is {first_name} and lastname is {last_name}" )
print("----"*9)

#To take input from user
salary=input("What is the salary: ")
print(type(salary))
print(salary)

order_list = [1,"dfsdf",4.5, 50]
# for loop
for x in order_list:
    print (x)

numbers=range(1,11)
sum=0
for x in numbers:
    sum= sum + x

print (sum)


total_sales=1000.60
print(math.ceil(total_sales))


marks=int(input("Enter the marks:"))

#indentation is mandatory here
if marks>=35:
    print("pass")
    print("Hey you passed")
else:
    print("fail")

#String related operations
print(len(first_name))

print(first_name[::-1])
print(first_name[-1:0])

order_amounts = [100,200,"None", "Invalid", 400.7,100]
sum1=0
for x in order_amounts:
    if type(x)==int or type(x)==float:
        sum1 =sum1+x
    else:
        continue

print (sum1)
print (order_amounts.count(100)) # it counts and prints the value- 2. If not present- 0
print(100 in order_list)
order_amounts1 = [100,200, 400.7,100]
order_amounts1.sort()
print(order_amounts1)
order_amounts1.reverse()
print(order_amounts1)
order_tuple = (100,200,"None", "Invalid", 400.7, 100)
#While loop works the same way as in java except syntax

#If I want to make a copy of one list, I cannot simply assign like below because it references to original list
order_list_new=order_list
#I want to use copy method\
order_list_new_1=order_list.copy()
print(order_list_new_1)
order_list_new_1.pop(2)

print(order_list_new_1)
