lists = [x for x in range(5)]
print (lists)

lists = [x for x in range(5) if (x%2)==0 ]
print (lists)

lists = [x if (x%2)==0 else "odd" for x in range(5)  ]
print (lists)

list1 = [0] * 5
print(list1)

list2=[1,2] +[5,8,9]
print(list2)

for a,b in zip(range(0,3), range(4,7)):
    print(a,b)

tuples_from_list = [(a,b) for a,b in zip(range(0,3), range(4,7))]
print(tuples_from_list)

dict_from_list = {a:b for a,b in zip(range(0,3), range(4,7))}
print(dict_from_list)

dict_from_list = {k:chr(k+64) for k in range(1,27)}
print(dict_from_list)

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print("Zipped lists: ", list(zipped))

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")


# Unzipping
zipped = [('a', 1), ('b', 2), ('c', 3)]
unzipped = zip(*zipped)
print(unzipped)
list1, list2 = list(unzipped)
print(list1)  # ('a', 'b', 'c')
print(list2)  # (1, 2, 3)