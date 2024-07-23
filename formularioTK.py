import tkinter as tk
import sqlite3

class Formulario:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Formulario de Datos Personales")
        self.ventana.geometry("400x300")  # Ajustar el tamaño del formulario

        # Contenedor principal
        self.frame = tk.Frame(ventana)
        self.frame.pack(pady=20)  # Agregar un poco de espacio alrededor del contenedor

        # Etiquetas y campos de entrada
        tk.Label(self.frame, text="Nombre:", font=("Arial", 12)).grid(row=0, column=0, sticky="e", pady=5)
        self.entry_nombre = tk.Entry(self.frame, font=("Arial", 12))
        self.entry_nombre.grid(row=0, column=1, pady=5)

        tk.Label(self.frame, text="Apellido Paterno:", font=("Arial", 12)).grid(row=1, column=0, sticky="e", pady=5)
        self.entry_apellido_paterno = tk.Entry(self.frame, font=("Arial", 12))
        self.entry_apellido_paterno.grid(row=1, column=1, pady=5)

        tk.Label(self.frame, text="Apellido Materno:", font=("Arial", 12)).grid(row=2, column=0, sticky="e", pady=5)
        self.entry_apellido_materno = tk.Entry(self.frame, font=("Arial", 12))
        self.entry_apellido_materno.grid(row=2, column=1, pady=5)

        tk.Label(self.frame, text="Fecha de Nacimiento:", font=("Arial", 12)).grid(row=3, column=0, sticky="e", pady=5)
        self.entry_fecha_nacimiento = tk.Entry(self.frame, font=("Arial", 12))
        self.entry_fecha_nacimiento.grid(row=3, column=1, pady=5)

        tk.Label(self.frame, text="Sexo:", font=("Arial", 12)).grid(row=4, column=0, sticky="e", pady=5)
        self.entry_sexo = tk.Entry(self.frame, font=("Arial", 12))
        self.entry_sexo.grid(row=4, column=1, pady=5)

        # Botones
        self.btn_guardar = tk.Button(self.frame, text="Guardar", font=("Arial", 12), command=self.guardar_datos)
        self.btn_guardar.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn_mostrar = tk.Button(self.frame, text="Mostrar Datos", font=("Arial", 12), command=self.mostrar_datos)
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
            tk.Label(ventana_mostrar, text=columna, font=("Arial", 12)).grid(row=0, column=i)

        for i, persona in enumerate(personas, start=1):
            for j, valor in enumerate(persona):
                tk.Label(ventana_mostrar, text=valor, font=("Arial", 12)).grid(row=i, column=j)

# Crear la ventana principal
ventana_principal = tk.Tk()
formulario = Formulario(ventana_principal)
ventana_principal.mainloop()
