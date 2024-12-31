class version1():
    def button(self):
        print ("Color Red from Version 1")

class version2(version1):   # version2 Class is inheriting version1 class
    def button(self):
        print("Color Purple from version 2")

if __name__=='__main__':
    ver1=version1()
    ver1.button()

    ver2=version2()
    ver2.button()


    # Polymorphism- Method Over riding- Same method but multiple different behaviours. Implemented using Inheritance




