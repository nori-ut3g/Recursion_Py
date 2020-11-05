def helloFunction():
    return lambda: "hello world"


# この関数は関数を返します。
print(helloFunction())

# 戻り値としてのこの関数を実行するか、保存することができます。
print(helloFunction()())
outputF = helloFunction()
print("Running a function that was generated...." + outputF())


# 数値xを取り込み、その後xと入力を乗算する関数を返します。
def constantMultiplication(x):
    return lambda y: y * x


multiplyBy4 = constantMultiplication(4);
print(multiplyBy4(3))  # 3*4 = 12
print(multiplyBy4(10))  # 10*4 = 100
print(multiplyBy4(5))  # 5*4 = 20