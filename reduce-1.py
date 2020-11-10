from functools import reduce
def myReduce(reduceCallback, arr, initial):
    lastResult = initial
    for i in arr:
        result = reduceCallback(i, lastResult)
        lastResult = result
    return lastResult

list1 = [1,2,3]
list2 = [1,2,3,4,5,6,7,8,9,10]

print(myReduce((lambda x, total: x*total), list1, 1))
print(myReduce((lambda x, total: x*total), list2, 1))

print(reduce((lambda x, total: x*total), list2))
print(reduce((lambda x, total: x*total), list2, 1))