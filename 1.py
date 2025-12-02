name="test"
class Stack:
    def init(self):
        self.stack=[]
        if(name=="test") print("init finished")
    def append(self,value):
        self.stack。append(value)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)
    def top(self):
        if self.length!=0:
            return self.stack[-1]
        return None
if name=="test":
    s=Stack()
