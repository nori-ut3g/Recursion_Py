# // 単項関数（unary function）fを受け取り、新しい機能が追加された関数fを返します。実行するたびにタイマーを使用し、fの実行時間がどれぐらいかを計算します。
import datetime
def timerDecorator(f, arg):
    def function():
        start = datetime.datetime.now().second * 1000 + datetime.datetime.now().microsecond / 1000
        result = f(arg)
        end = datetime.datetime.now().second * 1000 + datetime.datetime.now().microsecond / 1000
        print("This function took: " + str(int(end-start)) + "ms")
        return result
    return function()


print(timerDecorator((lambda x: x*2),100))

def bigOn2(x):
    def f():
        finalResult = 1
        for i in range(x):
            result = i
            for j in range(i):
                result += j
            finalResult += result
        return finalResult
    return f()
print(timerDecorator(bigOn2,10000))

def fibonacci(n):
    if n <= 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacciFast(fib1, fib2, n):
    if n <= 0: return fib1
    return fibonacciFast(fib1, fib1+fib2, n-1)

print(fibonacciFast(0, 1, 40))

timedFibonacciFast =(lambda n:fibonacciFast(0,1,n))
print(timerDecorator(timedFibonacciFast,40));