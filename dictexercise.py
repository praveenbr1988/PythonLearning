customers_raw_data="""custId,fname,lname,Address
1,praveen,br,6332 andante ave
2,sowmiya,rajaram,300 durants neck lane
3,Vid,Praveen, kolappakam
4,Dhanya, Praveen,perrypoint"""

customer_header= customers_raw_data.split("\n")[0]
customer_content=customers_raw_data.split("\n")[1:]
print(customer_header)
print(customer_content)

#cust_list = [  [cust.split(",")[0], tuple(cust.split(",")[1:]) ]  for cust in customer_content ]

# cust_dict={}
# for x in customer_content:
#     cust_dict[x.split(",")[0]]= tuple(x.split(",")[1:])
# print(cust_dict)
# print(cust_dict.get("4"))

# Using Dict comprehension
cust_dict={ x.split(",")[0] : tuple(x.split(",")[1:]) for x in  customer_content  }
print(cust_dict)

#############################################################################################

#Nested Dictionary
#Output should be
# nested_dict = {
#     "123": {"fname":"Praveen", "lname":"BR", "Address":"6332 Andante"},
#     "456": {"fname":"Sowmiya", "lname":"R", "Address":"62 Andante"}
# }

nested_dict={}
for key, value in cust_dict.items():
    nested_dict[key] = {
        "fname" : value[0],
        "lname": value[1],
        "Address": value[2],
    }
print(nested_dict)
print(nested_dict.get("3").get("fname"))