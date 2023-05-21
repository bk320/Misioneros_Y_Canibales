import tkinter as tk
from tkinter import Scrollbar
import os

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Interfaz Gráfica")
        self.window.geometry("1500x700")
        self.window.resizable(False, False)  # Evitar cambio de tamaño
        
         # Body (Contenido)
        self.body_frame = tk.Frame(self.window)
        self.body_frame.pack(expand=True, fill="both")
        
        self.content_text = tk.Text(self.body_frame, height=20, width=80)
        self.content_text.insert(tk.END, "Tres misioneros se perdieron explorando una jungla. Separados de sus compañeros,\n"
                                 "sin alimento y sin radio, solo sabían que para llegar a su destino\n"
                                 "debían ir siempre hacia adelante. Los tres misioneros se detuvieron\n"
                                 "frente a un río que les bloqueaba el paso, preguntándose qué podían hacer.\n"
                                 "De repente, aparecieron tres caníbales llevando un bote, pues también ellos\n"
                                 "querían cruzar el río. Ya anteriormente se habían encontrado grupos de\n"
                                 "misioneros y caníbales, y cada uno respetaba a los otros, pero sin confiar en ellos.\n"
                                 "\n"
                                 "Regla importante no debe haber mas canibales que misioneros\n"
                                 "Valores iniciales\n"
                                 "Numero de misioners = 3\n"
                                 "Numero de canibales = 3\n"
                                 "Capacidad en el bote = 2\n"
                                 "Tiempo limite = 120 ms para un limite de tiempo\n"
                                 "Nodos maximos = 100000 para un limite de nodos")
        
        self.content_text.pack(side="left", fill="both", expand=True)
        
        # Barra de desplazamiento
        scrollbar = Scrollbar(self.body_frame, command=self.content_text.yview)
        scrollbar.pack(side="left", fill="y")
        
        self.content_text.config(yscrollcommand=scrollbar.set)
        
        # Footer
        self.footer_frame = tk.Frame(self.window)
        self.footer_frame.pack(pady=10)
        
        # Campos de entrada
        self.label1 = tk.Label(self.footer_frame, text="Nro misioneros:")
        self.label1.pack(side="left")
        self.entry1 = tk.Entry(self.footer_frame)
        self.entry1.pack(side="left")
        
        self.label2 = tk.Label(self.footer_frame, text="Nro canibales:")
        self.label2.pack(side="left")
        self.entry2 = tk.Entry(self.footer_frame)
        self.entry2.pack(side="left")
        
        self.label3 = tk.Label(self.footer_frame, text="Capacidad del Bote:")
        self.label3.pack(side="left")
        self.entry3 = tk.Entry(self.footer_frame)
        self.entry3.pack(side="left")
        
        self.label4 = tk.Label(self.footer_frame, text="Tiempo máximo:")
        self.label4.pack(side="left")
        self.entry4 = tk.Entry(self.footer_frame)
        self.entry4.pack(side="left")
        
        self.label5 = tk.Label(self.footer_frame, text="Nodos máximos:")
        self.label5.pack(side="left")
        self.entry5 = tk.Entry(self.footer_frame)
        self.entry5.pack(side="left")
        
        # Botones
        self.button1 = tk.Button(self.footer_frame, text="Guardar Datos", command=self.generar_archivo)
        self.button1.pack(side="left", padx=10)
        
        self.button2 = tk.Button(self.footer_frame, text="Mostrar outBFS.txt", command=self.mostrar_out)
        self.button2.pack(side="left", padx=10)
        
        self.button3 = tk.Button(self.footer_frame, text="Mostrar outDFS.txt", command=self.mostrar_out2)
        self.button3.pack(side="left", padx=10)
        
    def generar_archivo(self):
        with open("inicio.txt", "w") as file:
            data = f"{self.entry1.get()}\n{self.entry2.get()}\n{self.entry3.get()}\n{self.entry4.get()}\n{self.entry5.get()}"
            file.write(data)
        os.system("python main.py")
        
    def mostrar_out(self):
        with open("outBFS.txt", "r") as file:
            contents = file.read()
        self.content_text.delete("1.0", tk.END)
        self.content_text.insert(tk.END, contents)
        
    def mostrar_out2(self):
        with open("outDFS.txt", "r") as file:
            contents = file.read()
        self.content_text.delete("1.0", tk.END)
        self.content_text.insert(tk.END, contents)
        
    def run(self):
        self.window.mainloop()
        
gui = GUI()
gui.run()
