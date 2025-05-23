import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresá una tarea.")

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)
    else:
        messagebox.showwarning("Advertencia", "Seleccioná una tarea para eliminar.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.config(width=400, height=400)
ventana.resizable(False, False)

# Entrada de texto
tk.Label(text="Nueva tarea:").place(x=30, y=30)
entrada_tarea = tk.Entry()
entrada_tarea.place(x=120, y=30, width=200)

# Botones
tk.Button(text="Agregar", command=agregar_tarea).place(x=120, y=70, width=90, height=30)
tk.Button(text="Eliminar", command=eliminar_tarea).place(x=230, y=70, width=90, height=30)

# Lista de tareas
tk.Label(text="Tareas pendientes:").place(x=30, y=130)
lista_tareas = tk.Listbox()
lista_tareas.place(x=30, y=160, width=330, height=180)

ventana.mainloop()
