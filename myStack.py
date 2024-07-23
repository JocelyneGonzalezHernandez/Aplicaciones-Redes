
#HACER DIAGRAMA DE FLUJO Y DIAGRAMA DE CLASES
#CÓDIGO DE STACK

class MyStack(): #Declarar clase
    
    def __init__(self): #Métodp constructor
        #atributos
        self.a=[] # a que es una lista
        self.n=0 #numero de elementos de la lista
        
    def push(self, x): #Método push
        self.a.append(x) #Agregar un elemento a la lista
        self.n+=1 #Incrementar n
        
    def is_empty(self): #función auxiliar para pop
        if self.n==0: #Si la lista está vacía
            return True #Ejecuta y sale
        return False #Solo si No se ejecutó la anterior, por eso no ocupa else
    
    def pop(self):
        if self.is_empty(): #Está vacio
            print("The stack is empty :p")
            return None #No hace nada
        else:
            self.n-=1 #Decrementa porque vas a eliminar un elemento
            return self.a.pop() #Método pop
    
    def max(self):
        if self.is_empty(): #El máximo de una lista vacía es nada
            return None
        else: #El máximo de una lista
            m=self.a[0] 
            for x in self.a:
                if x>m:
                    m=x
            return m
            
    def count(self):
        return self.n
    
    def top(self):#ultimo elemento sin eliminarlo
        if self.is_empty(): #El máximo de una lista vacía es nada
            return None
        else:
            return self.a[self.n-1]
        
        
#PROBAR / TESTING
stack=MyStack()
print(stack.is_empty())
print(stack.pop())

stack.push(4)
stack.push(5)
stack.push(7)
stack.push(1)

print(stack.is_empty())

print("My stack has ", stack.count(), "elements")
print("Max:", stack.max())
print("Top:", stack.top())

print("Elemento a eliminar:",stack.pop())

print("My stack has ", stack.count(), "elements")
print("Max:", stack.max())
print("Top:", stack.top())