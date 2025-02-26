word_dict={
    "intelligent":"One who is brainy",
    "Idiot": "One who does not think",
    "Clever": "One who is smart",
    3: "three",
    (1,2,3): "tuple",
    "car": "a 4 wheel drive"
}

print(word_dict[(1,2,3)]) # This might throw error if the key is not present so use the below one to get any key. This gracefully handles the exception
print(word_dict.get("intelligent"))

#We can add new Items
word_dict["bike"]= "2 wheel"

#Replace Existing
word_dict["car"]="4 wheeler"
word_dict.update({"car":"44 wheeller"})

print(word_dict)

#Delete a key
word_dict.pop("bike")
print(word_dict)

#Print keys
keys=word_dict.keys()
print(keys)
print(type(keys))


#Print value
values=word_dict.values()
print(values)
print(type(values))

#Print Items
items=word_dict.items()
print(items)
print(type(items))

#To convert to list
items_list=list(items)
print("Items list:", items_list)


#Check whether a kay is present
print(word_dict.__contains__("car"))

#Size of the Dictionary
print(word_dict.__len__())

#To convert tuple to DIct
order_data=[(101,1000),(102,1002),(103,1254),(104,1524),(105,8945)]
orders_dict=dict(order_data)
print(orders_dict)
print(type(orders_dict))

#To delete items in the dictionary
orders_dict.clear()
print(orders_dict)

# to delete the whole dictionary
a={"age":2}
print (a)
del a
#print (a)

# Iterating a Dict
fruits={'apple':"high in vitamin c",
        'banana': "high in potassiium"}

for key in fruits.keys():
    value=fruits[key]
    print(key, value)
