from functools import reduce
array2d = [[2,3,4,5],[5,22,34,4,5],[12,13,45,67,84]]

flatten = reduce((lambda flattenList, arr: flattenList+arr), array2d)

print(flatten)
print(flatten[1])
