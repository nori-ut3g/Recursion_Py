# ここから開発してください。
print(lambda x, y: x + y)
print((lambda x, y: x + y)(15, 35))

myCallable = lambda x, y: x + y
print(myCallable(3, 5))
print(myCallable(10, 10))
print(myCallable(150, 5))
print(myCallable)
