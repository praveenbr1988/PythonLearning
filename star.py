for i in range(1,5):
    for j in range(1,i+1):
        print ("*", end="")
    print()

print("##########################################################")

for i in range(1,5):
    for j in range(1,i+1):
        print (j, end="")
    print()

print("##########################################################")

# i loop runs from 1 to 4
# i=1
#     j loop runs from 1 to i+1 which is (1,  2) so it runs once
# i=2
#     j loop runs from 1 to i+1 which is (1,  3) so it runs twice


for i in range(4,0,-1):
    for j in range(1,i+1):
        print ("*", end="")
    print()

print("##########################################################")

n = 5  # Number of rows for the upper half (total height will be 2*n - 1)

# Upper triangle
for i in range(1, n + 1):
    print(" " * (n - i), end="")  # Print spaces
    print("*" * (2 * i - 1))  # Print stars

# Lower triangle
for i in range(n-1, 0, -1):
    print(" " * (n - i), end="")  # Print spaces
    print("*" * (2 * i - 1))  # Print stars

print("##########################################################")