def myMap(f, arr):
    results = []
    for i in arr: results.append(f(i))
    return results

nums = [1,2,3,4,5,6,7]
print(nums)
print(myMap((lambda x: x*x),nums))

# mapで返すのはイテレーター
print(list(map(lambda x: x*x, nums)))