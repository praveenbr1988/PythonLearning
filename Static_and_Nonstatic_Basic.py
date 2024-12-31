class HelloWorld():

    def display1(self):
        print ("Non Static method--Hello world")

    @staticmethod
    def display2():
        print("Static Method- Hello world")

if __name__=='__main__':

    #To call Non static methods, Need to create object and use object for calling
    app=HelloWorld()  #Object creation
    app.display1()


    #To call static methods, we dont need to create object. Call like below
    HelloWorld.display2()
    app.display2() # can also use object to access static methods