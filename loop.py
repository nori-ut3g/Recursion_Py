def forEach(f, arr):
    for i in arr: f(i)


forEach((lambda num: print(num)), [2, 3, 4, 5])


# 通常のfor loop
def simpleLoop():
    l = [3, 4, 5, 6, 6, 10]
    counter = 0
    for i in l: counter += i * i
    return counter


def loopDifferent():
    l = [3, 4, 5, 6, 6, 10]

    counter = 0

    def forEach(f, arr):
        for ele in arr:
            f(ele)

    def counterFunc(x):
        nonlocal counter
        counter += x * x

    forEach(counterFunc, l)

    return counter


print(loopDifferent())


def loopDifferentLibrary():
    l = [3, 4, 5, 6, 6, 10]
    counter = 0;

    for x in l:
        counter += x * x

    return counter;


print(loopDifferentLibrary());