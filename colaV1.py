class MyQueue():
    def __init__(self):
        self.a = []  # Lista para almacenar los elementos
        self.n = 0   # Número de elementos en la lista

    def is_empty(self):
        if self.n==0: #Si la lista está vacía
            return True #Ejecuta y sale
        return False #Solo si No se ejecutó la anterior, por eso no ocupa else

    def enqueue(self, x):
        self.a.insert(0, x)  # Insertar elemento al principio de la lista
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty :p")
            return None
        else:
            x = self.a.pop()  # Retirar elemento del final de la lista
            self.n -= 1
            return x

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

    def front(self):
        if self.is_empty():
            return None
        else:
             return self.a[0]

# TESTING
q = MyQueue()

print(q.is_empty())
print(q.dequeue())

q.enqueue("Ferrari")
q.enqueue("Vocho")
q.enqueue("Tsuru")
q.enqueue("Sentra")
q.enqueue("Camaro")

print(q.is_empty())
print('Total de elementos: ', q.count())
print('Max:', q.max())
print('Front:', q.front())



q.enqueue("BMW")

print("\n\nElemento a eliminar:",q.dequeue())
print(q.is_empty())
print('Total de elementos: ', q.count())
print('Max:', q.max())
print('Front:', q.front())

