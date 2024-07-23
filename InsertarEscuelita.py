import mysql.connector

def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="225369",  
            database="escuelita",
            auth_plugin='mysql_native_password'
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None
    
def crear_registro():
    nombre = input("Ingrese el nombre del alumno: ")
    return {"nombre": nombre}

def guardar_registro(registro):
    conexion = conectar_db()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            consulta = "INSERT INTO alumno (nombre) VALUES (%s)"
            datos = (registro["nombre"],)
            cursor.execute(consulta, datos)
            conexion.commit()
            print("Registro guardado correctamente")
        except mysql.connector.Error as err:
            print(f"Error al guardar el registro: {err}")
        finally:
            conexion.close()

def mostrar_registros():
    conexion = conectar_db()
    if conexion is not None:
        try:
            cursor = conexion.cursor()
            consulta = "SELECT * FROM alumno"
            cursor.execute(consulta)
            registros = cursor.fetchall()
            print("Registros en la base de datos:")
            for registro in registros:
                print(registro)
        except mysql.connector.Error as err:
            print(f"Error al mostrar los registros: {err}")
        finally:
            conexion.close()

registro = crear_registro()
guardar_registro(registro)
mostrar_registros()
