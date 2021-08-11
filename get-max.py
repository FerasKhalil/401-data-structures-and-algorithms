class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return 'Empty array'
    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        else:
            return None

class getMax:
    def __init__(self):
        self.stack = Stack()
        self.max_value = Stack()
    def push(self, item):
        self.stack.push(item)
        value_peek = self.max_value.peek()
        if value_peek is None or item >= value_peek:
            self.max_value.push(item)
    def pop(self):
        item = self.stack.pop()
        if item == self.max_value.peek():
            self.max_value.pop()
        return item
    def getMax(self):
        return self.max_value.peek()



getMax = getMax()

getMax.push(1)
 
getMax.push(50)
getMax.push(89)
# getMax.push(100)
getMax.push(95)
print(getMax.pop())
print(getMax.getMax())   
