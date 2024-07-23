class MyStack():
    
    def __init__(self):
        self.a=[]
        
    def push(self,x):
        self.a.append(x)
        
    def is_empty(self):
        return not bool(self.a)
    
    def pop(self):
        if self.is_empty():
            print("The stack is empty")
            return None
        else:
            return self.a.pop()
        
    def max(self):
        if self.is_empty():
            return None
        else:
            m=self.a[0]
            for x in self.a:
                if x > m:
                    m = x
            return m
        
    def count(self):
        return len(self.a)
    
    def top(self):
        if self.is_empty():
            return None
        else:
            return self.a[-1]
        

stack=MyStack()
print(stack.is_empty())
print(stack.pop())

stack.push('A')
stack.push('B')
stack.push('C')
stack.push('D')

print(stack.is_empty())
print("My stack has", stack.count(),"elements")
print("Max",stack.max())
print("Top", stack.top())

print("Element to remove:", stack.pop())
print("My stack has ", stack.count(), "elements")
print("Max:",stack.max())
print("Top:", stack.top())