#Crear una calculadora con interfaz python

#Importaciones
import tkinter as tk
from tkinter import messagebox
import math

# Ventana principal
root = tk.Tk()
root.title("Calculadora Avanzada")
root.geometry("350x500")
root.configure(bg="#2c2c2c")
root.resizable(False, False)

# Entrada de expresión
entrada = tk.Entry(root, font=("Consolas", 22), bd=5, relief="sunken", justify="right", bg="#1e1e1e", fg="white")
entrada.grid(row=0, column=0, columnspan=5, ipady=15, pady=10, padx=10, sticky="nsew")

# Historial
historial = []

# Función para evaluar expresiones
def calcular():
    try:
        expresion = entrada.get()
        expresion = expresion.replace('^', '**').replace('√', 'math.sqrt')
        resultado = eval(expresion, {"__builtins__": None, "math": math})
        historial.append(f"{expresion} = {resultado}")
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception as e:
        messagebox.showerror("Error", f"Expresión inválida\n{str(e)}")

# Borrar un caracter
def borrar():
    entrada.delete(len(entrada.get()) - 1)

# Limpiar campo
def limpiar():
    entrada.delete(0, tk.END)

# Mostrar historial
def mostrar_historial():
    if not historial:
        messagebox.showinfo("Historial", "No hay operaciones aún.")
        return
    ventana = tk.Toplevel(root)
    ventana.title("Historial")
    ventana.geometry("300x400")
    ventana.configure(bg="#1e1e1e")
    texto = tk.Text(ventana, font=("Consolas", 14), bg="#1e1e1e", fg="white")
    texto.pack(expand=True, fill='both', padx=10, pady=10)
    texto.insert(tk.END, "\n".join(historial[-20:]))
    texto.config(state='disabled')

# Insertar texto en entrada
def insertar(valor):
    entrada.insert(tk.END, valor)

# Configuración de botones
botones = [
    ("C", limpiar), ("←", borrar), ("(", lambda: insertar("(")), (")", lambda: insertar(")")), ("/", lambda: insertar("/")),
    ("7", lambda: insertar("7")), ("8", lambda: insertar("8")), ("9", lambda: insertar("9")), ("*", lambda: insertar("*")), ("√", lambda: insertar("√(")),
    ("4", lambda: insertar("4")), ("5", lambda: insertar("5")), ("6", lambda: insertar("6")), ("-", lambda: insertar("-")), ("^", lambda: insertar("^")),
    ("1", lambda: insertar("1")), ("2", lambda: insertar("2")), ("3", lambda: insertar("3")), ("+", lambda: insertar("+")), ("%", lambda: insertar("/100")),
    ("0", lambda: insertar("0")), (".", lambda: insertar(".")), ("=", calcular), ("Hist", mostrar_historial)
]

# Crear botones dinámicamente
row = 1
col = 0
for texto, accion in botones:
    btn = tk.Button(root, text=texto, command=accion,
                    width=5, height=2, font=("Arial", 14),
                    bg="#3d3d3d", fg="white", activebackground="#555", activeforeground="white")
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1
    if col > 4:
        col = 0
        row += 1

# Expansión de celdas
for i in range(6):
    root.rowconfigure(i, weight=1)
for j in range(5):
    root.columnconfigure(j, weight=1)

# Soporte para teclado (enter = calcular, escape = limpiar)
root.bind('<Return>', lambda event: calcular())
root.bind('<Escape>', lambda event: limpiar())

# Ejecutar aplicación
root.mainloop()
