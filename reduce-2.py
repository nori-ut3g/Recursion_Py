from functools import reduce

list1 = ["hello", "world", "and", "hello", "jupiter"]
# reduce(累積値, 現在の値)
print(reduce((lambda totalStr, currStr: totalStr + ", " + currStr), list1))

# Pythonには、すべての配列を1つの文字列に結合するためのjoin関数も用意されています。
print(", ".join(list1))

# joinの逆であるsplitは区切りを取り、区切りに基づいて文字列を配列要素に分割します。
print(", ".join(list1).split())