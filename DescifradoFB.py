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

def criptoanalisis_cesar(texto_cifrado):
    for llave in range(1, 26):
        texto_descifrado = descifrado_cesar(texto_cifrado, llave)
        print("Intento con desplazamiento", llave, ":", texto_descifrado)

texto_cifrado = input("Ingresa el texto cifrado: ")
print("Descifrando por fuerza bruta:")
criptoanalisis_cesar(texto_cifrado)

