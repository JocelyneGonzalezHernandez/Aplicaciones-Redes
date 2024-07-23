def cifrado_cesar(texto, llave):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            caracter = caracter.lower()
            codigo = ord(caracter)
            codigo += llave

            if codigo > ord('z'):
                codigo -= 26
            elif codigo < ord('a'):
                codigo += 26

            resultado += chr(codigo).upper() if mayuscula else chr(codigo)
        else:
            resultado += caracter

    return resultado

# Entrada de usuario
texto_original = input("Ingresa el texto a cifrar: ")
llave = int(input("Ingresa la llave (número entero): "))

# Cifrado César
texto_cifrado = cifrado_cesar(texto_original, llave)

# Salida
print("Texto cifrado:", texto_cifrado)
