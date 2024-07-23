import os
#print('Path: ',os.system('pwd'))

print(os.getcwd())  #Imprime el path
os.chdir('\\Users\\Jocel')#cambia el directorio

print(os.getcwd())  #Imprime el path

print(os.system('date'))
print(os.system('pwd'))

path='/'
dir_list = os.listdir(path)
print("Archivos y directorios '", path, "' -:")
print(os.system('pwd'))
print(dir_list)