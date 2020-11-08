# ここから開発してください。
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def peekFront(self):
        if self.head == None: return None
        return self.head.data

    def enqueue(self, data):
        if self.head == None:
            self.head = Node(data)
        elif self.tail == None:
            self.tail = Node(data)
            self.head.next = self.tail
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None: return None
        temp = self.head

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return temp.data

class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, callback):
        self.queue.enqueue(callback)

    def taskExists(self):
        return self.queue.peekFront() != None

    def run(self):
        callback = self.queue.dequeue()
        if callback != None: callback()

scheduler = TaskQueue()
scheduler.push(lambda: print("Running the first function!!!"))
scheduler.push(lambda: print("Running the second function~~~"))
scheduler.push(lambda: print("Running the third function>>>"))
scheduler.push(lambda: print("Running the fourth function<<<"))

while scheduler.taskExists():
    scheduler.run()