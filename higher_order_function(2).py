def summation(g, a, b):
   if b < a: return 0
   return g(b) + summation(g, a, b-1)

# 10までの総和
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
identity = lambda i : i
print(summation(identity, 1, 10))

# 10 * 100 の計算
print(summation((lambda i: 10),1,100))

def pPi(g,a,b):
   if b<a: return 1
   return g(b) * pPi(g,a,b-1)

# 10の階乗(10!)
print(pPi(identity,1,10))

# 5^10 の計算
print(pPi(lambda i: 5,1,10))