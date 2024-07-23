import os

# Imprime el directorio de trabajo actual
print(os.getcwd())

# Cambia el directorio de trabajo al directorio padre y luego regresa al directorio actual
os.chdir('../.')
print(os.getcwd())

# Define la ruta como la raíz del sistema
path = "/"
# Lista los archivos y directorios en la ruta especificada
dir_list = os.listdir(path)

# Imprime los archivos y directorios en la ruta especificada
print("Archivos y directorios '", path, "':")
print(dir_list)

# Unir partes de rutas para formar una ruta completa
location = "./"
file = "texto.txt"

full_path = os.path.join(location, file)

# Renombrar un archivo (especificando el nombre antiguo y el nuevo)
os.rename('texto.txt', 'New.txt')

# Verificar si un archivo o directorio existe en la ruta especificada
result = os.path.exists("New.txt")

# Obtener el tamaño de un archivo en bytes
file_size = os.path.getsize('New.txt')

# Eliminar un archivo (se necesita especificar el nombre del archivo a eliminar)
#os.remove('New.txt')

# Eliminar un directorio (se necesita especificar el nombre del directorio a eliminar)
#os.rmdir('directoryname')
