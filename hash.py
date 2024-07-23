import hashlib

texto="HOLA ESTE ES UN ARCHIVO DE PRUEBA"

hash=hashlib.sha256()
hash.update(texto.encode())
hash_hex=hash.hexdigest()
print("Hash SHA 256: ", hash_hex)