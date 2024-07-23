from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generar_par_claves():
    # Generar un par de claves RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key, private_key.public_key()

def guardar_clave_privada(private_key, filename):
    # Convertir la clave privada a formato PEM y guardarla en un archivo
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(filename, 'wb') as f:
        f.write(pem)

def cargar_clave_privada(filename):
    # Cargar la clave privada desde un archivo
    with open(filename, 'rb') as f:
        pem = f.read()
    return serialization.load_pem_private_key(pem, password=None, backend=default_backend())

def guardar_clave_publica(public_key, filename):
    # Convertir la clave pública a formato PEM y guardarla en un archivo
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(filename, 'wb') as f:
        f.write(pem)

def cargar_clave_publica(filename):
    # Cargar la clave pública desde un archivo
    with open(filename, 'rb') as f:
        pem = f.read()
    return serialization.load_pem_public_key(pem, backend=default_backend())

def cifrar_mensaje(public_key, mensaje):
    # Cifrar un mensaje utilizando la clave pública
    cifrado = public_key.encrypt(
        mensaje,
        padding=padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return cifrado

def descifrar_mensaje(private_key, cifrado):
    # Descifrar un mensaje utilizando la clave privada
    mensaje = private_key.decrypt(
        cifrado,
        padding=padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensaje

def firmar_datos(private_key, datos):
    # Firmar datos utilizando la clave privada
    firma = private_key.sign(
        datos,
        padding=padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        algorithm=hashes.SHA256()
    )
    return firma

def verificar_firma(public_key, datos, firma):
    # Verificar la firma de datos utilizando la clave pública
    try:
        public_key.verify(
            firma,
            datos,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print("Error al verificar la firma:", e)
        return False

# Ejemplo de uso
if __name__ == "__main__":
    # Generar un par de claves
    private_key, public_key = generar_par_claves()

    # Guardar las claves en archivos
    guardar_clave_privada(private_key, 'private_key.pem')
    guardar_clave_publica(public_key, 'public_key.pem')

    # Cargar las claves desde archivos
    private_key_loaded = cargar_clave_privada('private_key.pem')
    public_key_loaded = cargar_clave_publica('public_key.pem')

    # Mensaje de ejemplo
    mensaje = b"Ejemplo de mensaje secreto"

    # Cifrar y descifrar el mensaje
    cifrado = cifrar_mensaje(public_key_loaded, mensaje)
    mensaje_descifrado = descifrar_mensaje(private_key_loaded, cifrado)

    print("Mensaje original:", mensaje)
    print("Mensaje descifrado:", mensaje_descifrado)

    # Firmar y verificar datos
    firma = firmar_datos(private_key_loaded, mensaje)
    verificacion = verificar_firma(public_key_loaded, mensaje, firma)
    print("Verificación de firma:", verificacion)
