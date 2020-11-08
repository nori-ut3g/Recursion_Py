import math
import random


class LambdaMachine:
    def __init__(self):
        self.lambdaStorage = []
        # ハンドラはキーと値のペアを含み、キーは関数名、値は格納された関数のインデックスになります。ラムダ関数はこのlamdbaStorageに格納されます。
        self.handlers = {}
        self.counter = 0

    # キーに基づいて、ラムダ関数をデータ構造に挿入します。
    def insert(self, key, fLambda):
        if key in self.handlers:
            self.lambdaStorage[self.handlers[key]] = fLambda
            return
        else:
            self.lambdaStorage.append(fLambda)
            self.handlers[key] = len(self.lambdaStorage) - 1

    def retrieve(self, key):
        if len(self.lambdaStorage) > 0 and key in self.handlers:
            return self.lambdaStorage[self.handlers[key]]
        else:
            return None

    def roundRobinRetrieve(self):
        l = len(self.lambdaStorage)
        if l == 0: return None
        index = self.counter % l
        print("Round-Rpbin retrieval at index: " + str(index))

        self.counter += 1
        return self.lambdaStorage[index]

    def randomRetrieve(self):
        l = len(self.lambdaStorage)
        if l == 0: return None
        ran = math.floor(random.random() * l)
        print("Random retrieval at index: " + str(ran))
        return self.lambdaStorage[ran]


lambdaMachine = LambdaMachine()

# 2つの入力と共に、構造体ラムダに挿入します
lambdaMachine.insert("pythagora", lambda a, b: math.sqrt(a * a + b * b))
lambdaMachine.insert("addition", lambda x, y: x + y)
lambdaMachine.insert("subtraction", lambda x, y: x - y)
lambdaMachine.insert("multiplication", lambda x, y: x + y)
lambdaMachine.insert("division", lambda x, y: x / y)
lambdaMachine.insert("noises", lambda x, y: str(x) + "-DUM-DUM-DUM-DUM-" + str(y))

print(lambdaMachine.retrieve("pythagora"))
print(lambdaMachine.retrieve("pythagora")(3, 4))
print(lambdaMachine.retrieve("multiplication"))
print(lambdaMachine.retrieve("multiplication")(4, 10))
print(lambdaMachine.retrieve("noises"))
print(lambdaMachine.retrieve("noises")(10, 15))

x = 1
y = 10

print(lambdaMachine.randomRetrieve()(x, y))
print(lambdaMachine.randomRetrieve()(x, y))
print(lambdaMachine.randomRetrieve()(x, y))

# ラウンドロビンによる取得
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
print(lambdaMachine.roundRobinRetrieve()(x, y))
