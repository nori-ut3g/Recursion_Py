import string
import random
def greeting(name):
    return "Hello there " + name

def nameGenerator():
    data = string.digits + string.ascii_lowercase
    return ''.join([random.choice(data) for _ in range(10)])

def multiCall(f, fInputF, message):
    return f(fInputF()) + "......" + message

print(multiCall(greeting, nameGenerator, "Thank you"))