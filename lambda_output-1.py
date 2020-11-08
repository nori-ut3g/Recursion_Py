# この関数は通常の関数として定義すればよいので、これは無意味です。
# どのような入力であっても、常に同じ関数が返されます。
def lambdaHelloWorld(randomInput):
    print(randomInput + " was passed in but this function always returns the same lambda function")
    return lambda: "Hello World"


def helloWorld():
    return "Hello World"


print(helloWorld())
print((lambdaHelloWorld("lalilulelo")()))