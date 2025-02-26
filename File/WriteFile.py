# file= open("C:/Users/techi/PycharmProjects/PythonProject/File/appointments1.csv",'w')
# file.write("writing to a file")
# file.close()

# Writing/Overriding a file
path="C:/Users/techi/PycharmProjects/PythonProject/File/new_file.txt"
with open(path,'w') as file:
    print(file.write("Hi Hello"))

# Appending to a file
path="C:/Users/techi/PycharmProjects/PythonProject/File/new_file.txt"
with open(path,'a') as file:
    print(file.write("\nPraveen"))


