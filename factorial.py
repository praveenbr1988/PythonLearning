n=int(input("Enter no to find the factorial:"))
result=1
print(f'Factorial of {n} is: ',end="")
#Approach 1
while(n>=1):
    result=result * n
    n=n-1
print(result)


#Approach 2
def factfn(n):
    if n>0:
        return n*factfn(n-1)
    return 1

print(factfn(n))


5*factfn(4)
5*4*factfn(3)
5*4*3*factfn(2)
5*4*3*2*factfn(1)
5*4*3*2*1*factfn(0)

"""
1st Iteration:    
n=5    
result=1
While loop is true
    result=1*5=5
    n=4

2nd Iteration:
result=5
n=4
tru3
    Result=5*4=20
    n=3

3nd Iteration:
result=20
n=3
tru3
    Result=20*3=60
    n=2

"""
