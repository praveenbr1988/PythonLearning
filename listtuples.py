# order_amts_list = [100,200,300,400]
# order_newList= []
# for x in order_amts_list:
#        order_newList.append(x*0.18+x)
# print("Including GST: ",order_newList)
import math

#better way of doing the above commented lines- Using List comprehension
# order_amts_list = [100,200,300,400]
# order_newList= [x*0.18+x for x in order_amts_list]
# print("Including GST: ",order_newList)

##################################################################################################

# order_amts_list = [(100,5),(200,18),(300,6),(400,8)]
# order_newList= []
# for x in order_amts_list:
#        order_newList.append(x[0]+ x[0]*x[1]/100)
# print("Including GsST: ",order_newList)

#better way of doing the above commented lines- Using List comprehension
# order_amts_list = [(100,5),(200,18),(300,6),(400,8)]
# order_newList= [x[0]+ x[0]*x[1]/100 for x in order_amts_list]
# print("Including GST: ",order_newList)

##################################################################################################

#output should be [(100,5,105), (200,18,236),(300,6,318),(400,8,432)]
# order_amts_list = [(100,5),(200,18),(300,6),(400,8)]
# order_newList= [(x[0], x[1], x[0]+ x[0]*x[1]/100) for x in order_amts_list]
# print("Including GST: ",order_newList)

##################################################################################################

#output should be [[1,1,1], [2,4,8],[3,9,27],[400,8,432]] nested list
#using for loop
# nested_list=[]
# for x in range(1,4):
#     nested_list.append([x,x**2, x**3])
# print("Nested List: ",nested_list)
#
# flattened_list = []
# for sublist in nested_list:
#     for item in sublist:
#         flattened_list.append(item)
# print("Flattened list using for loop: ", flattened_list)

#using List comprehension
# nested_list=[ [x,x**2, x**3] for x in range(1,4) ]
# print("Nested List using list comprehension: ",nested_list)
# print("DataType ",type(nested_list))
#
# flattened_list=[item for sublist in nested_list for item in sublist ]
# print("Flattened list using for loop: ", flattened_list)

##################################################################################################

# orders_list=[
#     [101, '2023-07-25 00:00:00.0', 11599, 'CLOSED'],
#     [102, '2023-07-25 00:00:00.0', 115, 'PENDING_PAYMENT'],
#     [103, '2023-07-25 00:00:00.0', 111, 'COMPLETE']
# ]
# print("Order_list: ", orders_list)
# Closed_orders_list=[order for order in orders_list if order[3]=='CLOSED' ]
# print("Closed Order_list: ", Closed_orders_list)

##################################################################################################

#unpacking
# order=[101, '2023-07-25 00:00:00.0', 11599, 'CLOSED']
#
# order_id,order_date,order_amt,order_status = order
# print(order_id)
# print(order_date)
# print(order_amt)
# print(order_status)

##################################################################################################

#Generate 1 to 100 nos in a list
# numbers = tuple(range(1 , 101))
# print(numbers)

##################################################################################################
#
# order=[101, '2023-07-25 00:00:00.0','XXXXXX', 11599, 'CLOSED']
# #I want to remove junk 'xxxx'
# new_list= order[0:2] + order[3:]
# print(new_list)

#To append list 2 to list1
# list_1= [1,2,3,4]
# list_2=[5,6,7,8]
# # list_1.append(list_2)
# # print(list_1)
# # print(list_1[4][0])
#
# list_1.extend(list_2)
# print(list_1)

#list3  = list1 + list2  #similar to extend
#print(list3)

#How to print index and ELement
# orders=[101, '2023-07-25 00:00:00.0', 11599, 'CLOSED']
# for index, element in enumerate(orders):
#     print(f'Index:{index}, Element is {element}')
##################################################################################################

#How to count the no of occurences of a word in a list
# input = input("Enter the text: \n")
# input_list=input.split()
# input_list_lower=[word.lower()  for word in input_list]
# input_set = set(input_list_lower)
#
# print(input_set)
# occurences_list = [(word, input_list_lower.count(word)) for word in input_set]
# print (occurences_list)

##################################################################################################

# orders_list="""Col1, Col2, Col3, Col4
# 101, '2023-07-25 00:00:00.0', 11599, 'CLOSED'
# 102, '2023-07-25 00:00:00.0', 115, 'PENDING_PAYMENT'
# 103, '2023-07-25 00:00:00.0', 111, 'CLOSED'
# 103, '2023-07-25 00:00:00.0', 111, 'PENDING_PAYMENT'"""
#
#
# lines = orders_list.split("\n")[1:]
# print(lines)
#
# lines_tuple= [tuple( line.split(",")) for line in lines]
# print(lines_tuple)
#
# closed_list= [line_tup for line_tup in lines_tuple if line_tup[3].__contains__("CLOSED")]
# print(closed_list)
#
# status_list=[line_tup[3] for line_tup in lines_tuple]
# print(status_list)
#
# Status_count = [(status,status_list.count(status))for status in status_list]
# print(Status_count)

##################################################################################################

# transactions=[
#     [1,100,'success'],
#     [2,200,'fail'],
#     [3,300,'pending'],
#     [4,400,'fail'],
#     [5,500,'success'],
#     [6,600,'success']
# ]
#
# status_list = [ tran[2] for tran in transactions]
# status_set=set(status_list)
# print(status_set)
#
# count_list= [[status,status_list.count(status)] for status in status_set]
# print(count_list)
#
# for x in count_list:
#     print(x[0],": ", x[1] )

#################################################################################################

employees=[[101,'John','IT', 60000],
    [101,'Alice','HR', 50000],
    [101,'Bob','Finance', 70000],
    [101,'Emma','IT', 55000],
    [101,'David','Finance', 75000],
    [101,'Sophia','HR', 48000]]

# dept_list= [emp[2] for emp in employees]
# dept_uniq_set=set(dept_list)
# print(dept_uniq_set)
#
# sal_list=[[]]
# for dept in dept_uniq_set:
#     sum = 0
#     count=0
#     for emp in employees:
#         if emp[2] == dept:
#             sum=sum+emp[3]
#             count+=1
#         else:
#             continue
#     avg=sum/count
#     sal_list.append([dept,avg])
#
# sal_list=sal_list[1:]
# print(sal_list)
#
# for x in sal_list:
#     print(f'For {x[0]} Department, average salary is {x[1]}')

#Approach2
dept_lst = [emp[2] for emp in employees]
dept_set = set(dept_lst)
avg_lists=[[dept,sum([emp[3] for emp in employees if emp[2]==dept])/len([emp[2] for emp in employees if emp[2]==dept])] for dept in dept_set]
print(avg_lists)

print(["HI"]*3)
a=[11,12,9,10,5,7]
a.insert(1,4)
a[2:2]=[34,54]
print(a)
del a
#print(a)

"""
List- 
Allows Duplicate,
Any data can be stored
Insertion order is maintained
Mmutable- insert, delete, update 
"""
#pop()- Removes last element
#pop(2)- Removes using index
#remove("dsfdsaf")- Removes using element value
#list[2:5]=[]- removes those index positions
#my_list.index("Praveen")-> Gives the index position ofr element "Praveen"
# my_list.reverse()- Reverses the elements present in list
# my_list.sort()- Sorts in Ascending order.
# To sort in descending- First sort and then reverse
# append-> inserts element at the last position
# insert(0,"dsgsdf")-> Inserts elements at the 0th index
# my_list.extend([1,2,3])-> inserts 1,2,3 into the list as separate elements


##################################################################################

""""
tuple- 
Allows Duplicate,
Any data can be stored
Insertion order is maintained
Immutable - No insertion, deletion, updation
"""
tuple_a=(11,12,9,10,5,7)
print("Tuple length is : ",tuple_a.__len__())
print("To find the index of an element is ",tuple_a.index(11,0,5))

print("Count of items:", tuple_a.count(11))
print("Present or not:",tuple_a.__contains__(11))
