# file= open("C:/Users/techi/PycharmProjects/PythonProject/File/appointments1.csv",'r')
# print (file.read())
# file.close()

# path="C:/Users/techi/PycharmProjects/PythonProject/File/appointments.csv"
# with open(path,'r') as file:
#     #print(file.readlines())
#     print(file.read())

# line by line- using for loop- better way
path="C:/Users/techi/PycharmProjects/PythonProject/File/appointments.csv"
with open(path, 'r') as file:
    for line in file:
        print(line.rstrip())


help(print)