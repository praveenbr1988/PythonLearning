from functools import partial

def email(id, domain, extension):
    print(id+domain+extension)

#email("Praveen", "@PNC", ".com")

test = partial(email,"Praveenbr1988")
test("@microsoft",".com")


