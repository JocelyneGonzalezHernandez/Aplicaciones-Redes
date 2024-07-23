import tkinter as tk
import math

# Configuración predeterminada para los botones
configuracion_boton = {
    "font": ("", 12),
    "height": "2",
    "width": "7",
    "relief": "flat",
    "activebackground": "blue"
}

# Lista de dígitos que necesitan una función especial
especiales = ["√", "x²", "C", "=", "log"]

# Lista de dígitos que recibirán un fondo personalizado
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.displayFrame = tk.Frame(self.master)
        self.displayFrame.pack()
        self.buttonsFrame = tk.Frame(self.master)
        self.buttonsFrame.pack()
        self.output = tk.Entry(self.displayFrame, width=30, relief="sunken", bd=3, font=("", 17))
        self.output.grid(row=0, column=0)
        self.crearBotones()

    def crearBotones(self):
        botones = [
            ["√", "(", ")", "/", "x²"],
            ["7", "8", "9", "+", "**"],
            ["4", "5", "6", "-", "log"],
            ["1", "2", "3", "*"],
            [".", "0", "=", "C"]
        ]

        for i in range(len(botones)):
            for j in range(len(botones[i])):
                texto = botones[i][j]
                comando = lambda t=texto: self.accionBoton(t)
                config = configuracion_boton if texto in numeros else configuracion_boton
                boton = tk.Button(self.buttonsFrame, config, text=texto, command=comando)
                boton.grid(row=i, column=j)

    def accionBoton(self, texto):
        if texto != "=":
            if texto not in especiales:
                self.output.insert('end', texto)
            else:
                if texto == "√":
                    self.agregarValor(math.sqrt(float(self.output.get())))
                elif texto == "x²":
                    self.agregarValor(float(self.output.get()) ** 2)
                elif texto == "C":
                    self.agregarValor("")
                elif texto == "log":
                    self.agregarValor(math.log10(float(self.output.get())))
        else:
            self.agregarValor(eval(self.output.get()))

    def agregarValor(self, valor):
        self.output.delete(0, 'end')
        self.output.insert('end', valor)

root = tk.Tk()
Calculadora(root)
root.mainloop()
