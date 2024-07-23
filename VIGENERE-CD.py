"""
@file VIGENERE-CD.py
@brief Este programa permite hacer el cifrado y descifrado Vigenere, además del
criptoanálisis por fuerza bruta.

@authors Jocelyne González, Michelle Pérez
@date 21/04/2024
"""
from random import sample
from itertools import product as col

"""
Función para quitar acentos de una letra.
Si encuentra alguna coincidencia, la reemplaza por la vocal correspondiernte.
En caso de ser una ñ, se reemplaza por n.
Si no encuetra coincidencia, regresa la letra.
@param letra	Letra a analizar
@return char
"""
def quitar_acentos(letra):
    """
    Función para quitar acentos de una letra.
    """
    if letra in 'áäàâ':
        return 'a'
    elif letra in 'éëèê':
        return 'e'
    elif letra in 'íïìî':
        return 'i'
    elif letra in 'óöòô':
        return 'o'
    elif letra in 'úüùû':
        return 'u'
    elif letra == 'ñ':
        return 'n'
    else:
        return letra
"""
Función que devuelve texto sin acentos.
Cambia el texto a minúsculas y manda a llamar a la función quitar_acentos.
Devuelve el texto sin acentos y en mayúsculas
@param texto	Texto ingresado
@return string
"""
def limpiar_texto(texto):
    # Utiliza la función quitar_acentos para limpiar el texto
    
    texto_limpio = ''.join(quitar_acentos(letra) for letra in texto.lower())
    return texto_limpio.upper()

"""
Función para cifrar o descrifrar un texto.
Convierte el texto recibido en una lista y la recorre posición por posición.
Si la contenido de la posición es una letra del alfabeto y si el parámetro cifrar
es True, se obtiene la letra cifrada. Si el parámetro cifrar es False, se obtiene
la letra descifrada.
@param texto	Texto a cifrar o descifrar
@param clave	Llave intriducida o calculada
@param cifrar 	Bandera para cifrar o descifrar
@return list
"""
def vigenere(texto, clave, cifrar):
    lista_final = []
    codigo = list(texto)
    j = 0
    
    for i, caracter in enumerate(codigo):
        if caracter.isalpha():
            codigo[i] = clave[(i+j) % len(clave)]
            if cifrar:
                lista_final.append((ord(texto[i]) + ord(codigo[i]) - 65 * 2) % 26)
            else:
                lista_final.append((ord(texto[i]) - ord(codigo[i])) % 26)
        else:
            lista_final.append(ord(caracter))
            j -=1

    for i, caracter in enumerate(codigo):
        if caracter.isalpha():
            lista_final[i] = chr(lista_final[i] + 65)
        else:
            lista_final[i] = chr(lista_final[i])
            
    return ''.join(lista_final)

"""
Función para encontrar la longitud de la llave.
Compara cada una de las letras del texto cifrado, con las letras del mismo
texto cifrado pero con un desplazamiento que puede ser desde 1 hasta la
posible longitud de la llave.
Cuenta el número de coincidencias que se encontraron por cada desplazamiento. 
Deduce la longitud de la llave basándose en el desplazamiento que tuvo el
mayor número de coincidencias.
@param texto_cifrado	Texto cifrado
@return int
"""
def encontrar_longitud_llave(texto_cifrado):
    frecuencias = []
    for desplazamiento in range(1, len(texto_cifrado) // 2 + 1):
        coincidencias = sum(1 for i, letra in enumerate(texto_cifrado) if letra == texto_cifrado[(i + desplazamiento) % len(texto_cifrado)])
        frecuencias.append(coincidencias)
    longitud_llave = frecuencias.index(max(frecuencias)) + 1
    return longitud_llave

"""
Función que obtiene las letras cifradas con el mismo desplzamiento.
Recorre el texto cifrado letra por letra para identificar el valor de desplzamiento
con el que fue cifrada y colocarla en el número de columna que indica el valor,
considerando la longitud de la llave.
@param texto_cifrado	Texto cifrado
@param longitud_llave 	Longitud calculada de llave
@return list
"""
def obtener_columnas(texto_cifrado, longitud_llave):
    columnas = [''] * longitud_llave
    for i, letra in enumerate(texto_cifrado):
        columna = i % longitud_llave
        columnas[columna] += letra
    return columnas

"""
Función para analizar la frecuencia de la columna.
Realiza un conteo para saber cuantas veces se repite la misma letra y poder conocer
la de mayor frecuencia. 
@param columna
@return float
"""
def analizar_frecuencia(columna):
    frecuencia = [0] * 26
    for letra in columna:
        posicion = ord(letra) - 97
        if 0 <= posicion < 26:
            frecuencia[posicion] += 1
        else:
            # Manejar el caso de letra fuera del rango esperado
            print(f"Caracter '{letra}' fuera del rango esperado.")
    total_letras = sum(frecuencia)
    frecuencia_normalizada = [count / total_letras for count in frecuencia]
    return frecuencia_normalizada
"""
Función para encontrar la letra que corresponde a cada columna de la llave.
Decide cuál de todas las letras podría ser la letra “e”, ya
que esta letra es la que mayor frecuencia de aparición presenta.
Se toma la de mayor frecuencia y se comprueba si las otras letras que aparecen
con una frecuencia alta, concuerdan con la tabla de frecuencias del idioma.
Si las demás letras no tienen un alto grado de aparición en el texto, se toma
la siguiente letra con mayor frecuencia.
@param frecuencia_columna
@return string
"""
def encontrar_caracter_llave(frecuencia_columna):
    InglesFrecuencia = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.001, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
    resultados = []
    for desplazamiento in range(26):
        resultado = sum(fc * InglesFrecuencia[(i - desplazamiento) % 26] for i, fc in enumerate(frecuencia_columna))
        resultados.append(resultado)
    indice_max = resultados.index(max(resultados))
    return chr(indice_max + 97)

"""
Pantalla principal del programa
"""
print("Bienvenido al cifrado Vigenère")

while True:
    print("Menú:")
    print("1. Cifrar")
    print("2. Descifrar")
    print("3. Criptoanálisis")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == '1':
        texto = limpiar_texto(input('Ingresa el texto: '))  # Limpia el texto antes de cifrar
        clave = input('Ingresa la clave: ').upper()
        cifrar = True
        print("Texto cifrado:", vigenere(texto, clave, cifrar))
    elif opcion == '2':
        texto = limpiar_texto(input('Texto: '))  # Limpia el texto antes de descifrar
        clave = input('Ingresa la clave: ').upper()
        cifrar = False
        print("Texto descifrado:", vigenere(texto, clave, cifrar))
    elif opcion == '3':
        with open('cifrado.txt', 'r') as file:
            texto_cifrado = file.read().lower()

        # Encontrar la longitud de la llave
        longitud_llave = encontrar_longitud_llave(texto_cifrado)
        print("Longitud de la llave encontrada:", longitud_llave)

        # Obtener las columnas del texto cifrado
        columnas = obtener_columnas(texto_cifrado, longitud_llave)

        # Descubrir la llave
        llave = ""
        for columna in columnas:
            frecuencia_columna = analizar_frecuencia(columna)
            caracter_llave = encontrar_caracter_llave(frecuencia_columna)
            llave += caracter_llave

        print("Llave descubierta:", llave)
        print(f'Probando clave: {llave} ==> {vigenere(texto_cifrado, llave, False)}')
        if input('¿Continuar (s/n)? ... : ')== "n":
            break
        else:
            while True:
                abc = list("ABCDEFGHIJKHIJKLMNOPQRSTUVWXYZ")
                clave_generada = ''.join(sample(abc, longitud_llave))
                cifrar = True
                print(f"para {clave_generada} = {vigenere(texto_cifrado, clave_generada, cifrar)}")
                if input('¿Continuar (s/n)? ... : ')== "n":
                    break
    elif opcion == '4':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
