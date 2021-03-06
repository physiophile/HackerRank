class MyQueue(object):
    def __init__(self):
        # stack1 to keep all records, stack2 to assist query
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        top_value = self.stack2[-1]
        return top_value
        
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        self.stack2.pop()
        
    def put(self, value):
        self.stack1.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        
