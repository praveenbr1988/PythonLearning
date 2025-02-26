# from functools import partial
#
# def email(id, domain, extension):
#     print(id+domain+extension)
#
# #email("Praveen", "@PNC", ".com")
#
# test = partial(email,"Praveenbr1988")
# test("@microsoft",".com")

############################################################################

# def add_1(x):
#     x=[1,2]
#     return x
#
# a=[1,2,3]
# print(add_1(a))
# print(a)

############################################################################
# we can set default values in the fn arguments. c is optional. Default values should present at last.
def add(a=3,b=2,c=4):
    return a+b+c

print(add(5,6))
print(add(5,6,2))
print(add(a=1))
print(add(b=1))
print(add(c=5,a=4,b=1))