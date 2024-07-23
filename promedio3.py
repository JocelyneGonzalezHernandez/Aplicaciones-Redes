#A) Programa que realiza el promedio de 3 calificaciones e indica si el alumno está reprobado

def prom(): #Define la función
    a=[] #Lista vacía
    for i in range(3): #Bucle for en un rango de 3 iteraciones
        c=eval(input("Ingrese calificación:")) #Captura de calificación
        a.append(c) #Añadir a la lista
    prom=sum(a)/len(a) #Calcular el promedio
    
    print("Promedio:",prom) #Imprimir el promedio
    if prom>=6.0: #Si el promedio es mayor o igual a 6.0 
        print("No estás reprobado") #Imprime "No estás reprobado"
    else: #De lo contrario
        print("Estás reprobado")  #Imprime "Estás reprobado"

prom()
