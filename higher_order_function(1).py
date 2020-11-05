# この関数は関数の参照を受け取り、ローカルスコープ内で呼び出します。
def functionInputTest(f):
   return f() + ".... called from another function!"

print(functionInputTest(lambda:"hello world"))

def fSquaredX(f, x):
   return f(x*x)

# f(a^2) = a^2 + 30;
print(fSquaredX((lambda a: a + 30),5))  # 25 + 30 = 55

# 呼び出し可能オブジェクトを変数内に格納します。
callable1 = (lambda p : "p is " + str(p))
print(fSquaredX(callable1, 10))
print(fSquaredX(callable1, 8))
