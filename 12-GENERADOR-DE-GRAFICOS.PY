import tkinter as tk 
from tkinter import ttk 
import matplotlib.pyplot as plt 
import numpy as np 

class GeneradorGraficosApp:
    def __init__(self, master):
        self.master = master
        self.master.title ("Generador de Gráficos")

        self.label_datos = ttk.Label(self.master, text="Ingrese los datos (separados por comas): ")
        self.label_datos.grid(row=0, column=0, padx=5, pady=5)

        self.datos_entry = ttk.Entry(self.master, width=50)
        self.datos_entry.grid(row=0, column=1, padx=5, pady=5)

        self.graficar_button = ttk.Button(self.master, text="Graficar", command=self.graficar)
        self.graficar_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def graficar(self):
        datos = self.datos_entry.get().split(",")
        datos = [float(d) for d in datos] #convierte los datos a flotantes

        #creando el gráfico de barras
        plt.bar(range(len(datos)), datos)
        plt.xlabel("Datos")
        plt.ylabel("Valor")
        plt.title("Gráfico")

        #mostrar el gráfico
        plt.show()

if __name__== "__main__":
    root = tk.Tk()
    app = GeneradorGraficosApp(root)
    root.mainloop()