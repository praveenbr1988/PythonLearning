def outerfn(message):
    print("outer function: ", message)
    def innerfn():
        print("inner function: ", message)
    innerfn()

outerfn("Hello")