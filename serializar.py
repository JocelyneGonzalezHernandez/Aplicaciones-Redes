import json

alumno={'id': 1,'nombre':'Pedro', 'edad':20, 'aprobado':False } #diccionario

cadenaJson=json.dumps(alumno)

print(cadenaJson) #Imprime en formato Json

#Imprime el "False" como "false"
print(type(cadenaJson)) #str  -> Serializar objetos para poderlo transmitir

cadena='{"id":2, "nombre":"Juana", "edad":25,"aprobado":true}'
otroA=json.loads(cadena)

#True con T es formato de python
#true con t es formato Json
for x,y in otroA.items():
    print(x,y)

#Mando objetos en un cadena Json y ouedo recibir igual en Json