def descifrado_cesar(texto, llave):
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():
            mayuscula = caracter.isupper()
            caracter = caracter.lower()
            codigo = ord(caracter)
            codigo -= llave

            if codigo > ord('z'):
                codigo -= 26
            elif codigo < ord('a'):
                codigo += 26

            resultado += chr(codigo).upper() if mayuscula else chr(codigo)
        else:
            resultado += caracter

    return resultado

# Entrada de usuario
texto_cifrado = input("Ingresa el texto cifrado: ")
llave = int(input("Ingresa la llave utilizado para cifrar: "))

# Descifrado César
texto_descifrado = descifrado_cesar(texto_cifrado, llave)

# Salida
print("Texto descifrado:", texto_descifrado)

