import tkinter as tk
import sqlite3

class Formulario:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Formulario de Datos Personales")

        # Etiquetas y campos de entrada
        tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky="e")
        self.entry_nombre = tk.Entry(ventana)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(ventana, text="Apellido Paterno:").grid(row=1, column=0, sticky="e")
        self.entry_apellido_paterno = tk.Entry(ventana)
        self.entry_apellido_paterno.grid(row=1, column=1)

        tk.Label(ventana, text="Apellido Materno:").grid(row=2, column=0, sticky="e")
        self.entry_apellido_materno = tk.Entry(ventana)
        self.entry_apellido_materno.grid(row=2, column=1)

        tk.Label(ventana, text="Fecha de Nacimiento:").grid(row=3, column=0, sticky="e")
        self.entry_fecha_nacimiento = tk.Entry(ventana)
        self.entry_fecha_nacimiento.grid(row=3, column=1)

        tk.Label(ventana, text="Sexo:").grid(row=4, column=0, sticky="e")
        self.entry_sexo = tk.Entry(ventana)
        self.entry_sexo.grid(row=4, column=1)

        # Botones
        self.btn_guardar = tk.Button(ventana, text="Guardar", command=self.guardar_datos)
        self.btn_guardar.grid(row=5, column=0, columnspan=2)

        self.btn_mostrar = tk.Button(ventana, text="Mostrar Datos", command=self.mostrar_datos)
        self.btn_mostrar.grid(row=6, column=0, columnspan=2)

        # Conexión a la base de datos SQLite
        self.conexion = sqlite3.connect('datos_personales.db')
        self.cursor = self.conexion.cursor()

        # Crear la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS personas
                            (id INTEGER PRIMARY KEY, nombre TEXT, apellido_paterno TEXT, apellido_materno TEXT, fecha_nacimiento TEXT, sexo TEXT)''')
        self.conexion.commit()

    def guardar_datos(self):
        nombre = self.entry_nombre.get()
        apellido_paterno = self.entry_apellido_paterno.get()
        apellido_materno = self.entry_apellido_materno.get()
        fecha_nacimiento = self.entry_fecha_nacimiento.get()
        sexo = self.entry_sexo.get()

        # Insertar datos en la tabla
        self.cursor.execute("INSERT INTO personas (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo) VALUES (?, ?, ?, ?, ?)",
                            (nombre, apellido_paterno, apellido_materno, fecha_nacimiento, sexo))
        self.conexion.commit()

        # Limpiar campos después de guardar
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellido_paterno.delete(0, tk.END)
        self.entry_apellido_materno.delete(0, tk.END)
        self.entry_fecha_nacimiento.delete(0, tk.END)
        self.entry_sexo.delete(0, tk.END)

    def mostrar_datos(self):
        # Obtener todos los registros de la tabla
        self.cursor.execute("SELECT * FROM personas")
        personas = self.cursor.fetchall()

        # Mostrar los datos en una nueva ventana
        ventana_mostrar = tk.Toplevel(self.ventana)
        ventana_mostrar.title("Datos Almacenados")

        # Crear una tabla para mostrar los datos
        for i, columna in enumerate(["ID", "Nombre", "Apellido Paterno", "Apellido Materno", "Fecha de Nacimiento", "Sexo"]):
            tk.Label(ventana_mostrar, text=columna).grid(row=0, column=i)

        for i, persona in enumerate(personas, start=1):
            for j, valor in enumerate(persona):
                tk.Label(ventana_mostrar, text=valor).grid(row=i, column=j)

# Crear la ventana principal
ventana_principal = tk.Tk()
formulario = Formulario(ventana_principal)
ventana_principal.mainloop()
