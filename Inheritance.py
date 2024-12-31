class version1():
    def v1(self):
        print ("Button")
        print("TextBox")

class version2(version1):   # version2 Class is inheriting version1 class
    def v2(self):
        print("Drop down Box")

if __name__=='__main__':
    app=version2()
    app.v1()
    app.v2()


#Multi level Inheritance- Version3->Version2->Version1
#Multi inheritance- can also be done - class version3(version1, version2):