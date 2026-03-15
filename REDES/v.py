def encontrar_longitud_llave(texto_cifrado):
    frecuencias = []
    for desplazamiento in range(1, len(texto_cifrado) // 2 + 1):
        coincidencias = sum(1 for i, letra in enumerate(texto_cifrado) if letra == texto_cifrado[(i + desplazamiento) % len(texto_cifrado)])
        frecuencias.append(coincidencias)
    longitud_llave = frecuencias.index(max(frecuencias)) + 1
    return longitud_llave

def obtener_columnas(texto_cifrado, longitud_llave):
    columnas = [''] * longitud_llave
    for i, letra in enumerate(texto_cifrado):
        columna = i % longitud_llave
        columnas[columna] += letra
    return columnas

def analizar_frecuencia(columna):
    frecuencia = [0] * 26
    for letra in columna:
        posicion = ord(letra) - 97
        frecuencia[posicion] += 1
    total_letras = sum(frecuencia)
    frecuencia_normalizada = [count / total_letras for count in frecuencia]
    return frecuencia_normalizada

def encontrar_caracter_llave(frecuencia_columna):
    InglesFrecuencia = [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 0.0751, 0.0193, 0.001, 0.0599, 0.0633, 0.0906, 0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]
    resultados = []
    for desplazamiento in range(26):
        resultado = sum(fc * InglesFrecuencia[(i - desplazamiento) % 26] for i, fc in enumerate(frecuencia_columna))
        resultados.append(resultado)
    indice_max = resultados.index(max(resultados))
    return chr(indice_max + 97)

def descifrar_texto(texto_cifrado, llave):
    texto_descifrado = ""
    for i, letra in enumerate(texto_cifrado):
        if letra.isalpha():
            key_index = i % len(llave)
            shift = ord(llave[key_index]) - 97
            if letra.islower():
                decrypted = chr(((ord(letra) - 97 - shift) % 26) + 97)
            else:
                decrypted = chr(((ord(letra) - 65 - shift) % 26) + 65)
            texto_descifrado += decrypted
        else:
            texto_descifrado += letra
    return texto_descifrado

# Leer texto cifrado desde el archivo
with open('texto_cifrado.txt', 'r') as file:
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

# Descifrar el texto
texto_descifrado = descifrar_texto(texto_cifrado, llave)
print("\nTexto descifrado:\n", texto_descifrado)