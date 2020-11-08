def myFilter(predicateF, arr):
    results = []
    for i in arr:
        if predicateF(i) == True: results.append(i)
    return results
list1 = [1,2,3,4,5,6,7,8,9,10]
print(myFilter((lambda x: x%2 != 0), list1))