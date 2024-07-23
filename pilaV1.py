class MyStack(): 
    def __init__(self): 
        self.a = []  # Lista que almacena los elementos de la pila

    def push(self, x): 
        self.a.append(x) 
     
    def is_empty(self): 
        return not bool(self.a)  # Verifica si la lista está vacía
    
    def pop(self):
        if self.is_empty(): 
            print("The stack is empty :p")
            return None 
        else:
            return self.a.pop() 

    def max(self):
        if self.is_empty():
            return None
        else:
            m = self.a[0]
            for x in self.a:
                if x > m:
                    m = x
            return m  # Moví esta línea para que esté fuera del bucle
    
    def count(self):
        return len(self.a)  # En lugar de usar la propiedad 'n'

    def top(self):
        if self.is_empty(): 
            return None
        else:
            return self.a[-1]  # Utilizando índices negativos para obtener el último elemento

# PROBAR / TESTING
stack = MyStack()
print(stack.is_empty())
print(stack.pop())

stack.push('A')  # Usar letras mayúsculas
stack.push('B')
stack.push('D')
stack.push('C')

print(stack.is_empty())
print("My stack has", stack.count(), "elements")
print("Max:", stack.max())
print("Top:", stack.top())

print("Elemento a eliminar:",stack.pop())

print("My stack has ", stack.count(), "elements")
print("Max:", stack.max())
print("Top:", stack.top())
