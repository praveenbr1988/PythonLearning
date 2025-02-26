class a():
    def __init__(self):
        print("A")

    def display(self):
        print("you are in class a")

class b():
    def __init__(self):
        super().__init__()
        print("BB")

    def display(self):
        print("you are in class b")

class c(b, a):
    def __init__(self):
        super().__init__()
        print("C")

    def display(self):
        print("you are in class c")

obj1 = c()
