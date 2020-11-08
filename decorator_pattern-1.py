def simpleDecorator(f):
    def function():
        print("Running f......")
        return f()

    return function


def helloWorld():
    return "Hello world"


newFunc1 = simpleDecorator(helloWorld)
print(newFunc1())

newFunc2 = simpleDecorator(lambda: "Hello Jupiter")
print(newFunc2())