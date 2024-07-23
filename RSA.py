import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

if len(sys.argv) < 4:
    print("Usage: python script.py bit_size key_format text_to_cipher")
    sys.exit(1)

# Parte para generar claves RSA
bit_size = int(sys.argv[1])
key_format = sys.argv[2]

keys = RSA.generate(bit_size)

print("Clave Pública:")
print(keys.publickey().export_key(key_format).decode(), end='\n\n')

print("Clave Privada:")
print(keys.export_key(key_format).decode())

# Parte para cifrar y descifrar texto
text_to_cipher = sys.argv[3]

# Importamos la clave pública para cifrar los datos
cipher_rsa = PKCS1_OAEP.new(keys.publickey())
# Importamos la clave privada para descifrar los datos
decipher_rsa = PKCS1_OAEP.new(keys)

# Ciframos los datos.
enc_data = cipher_rsa.encrypt(text_to_cipher.encode())

# Desciframos los datos
dec_data = decipher_rsa.decrypt(enc_data)

print("\nEncriptado:")
print(enc_data, end='\n\n')

print("Desencriptado:")
print(dec_data)
