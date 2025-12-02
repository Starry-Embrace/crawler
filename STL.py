stack_test=False
queue_test=False
class stack:
    def init(self):
        self.stack=[]
        if(stack_test) print("stack init finished")
    def append(self,value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def length(self):
        return len(self.stack)
    def top(self):
        if self.length!=0:
            return self.stack[-1]
        return None
class queue:
    def init(self):
        self.queue=[]
        if(queue_test) print("queue init finished")
    def append(self,value):
        self.queue。append(value)
    def pop(self):
        # need to append
    def length(self):
        return len(self.queue)
    def top(self):
        if self.length!=0:
            # need to append
        return None
if stack_test:
    s=Stack()
