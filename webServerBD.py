import mysql.connector
from flask import Flask
import json

app = Flask(__name__)

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
  
@app.route("/alumno")
def alumno():
        conexion=conectar_db()
        try:
                cursor = conexion.cursor()
                consulta = "SELECT * FROM alumno"
                cursor.execute(consulta)
                alumnos=cursor.fetchall()
                
                lista_alumnos=[]
                for alumno in alumnos:
                    alumnos_dicc={
                        "id": alumno[0],
                        "nombre": alumno[1]
                        }
                    lista_alumnos.append(alumnos_dicc)
                json_alumnos=json.dumps(lista_alumnos)
                return json_alumnos
        except mysql.connector.Error as err:
            print(f"Error al mostrar los registros: {err}")
        finally:
            conexion.close()
