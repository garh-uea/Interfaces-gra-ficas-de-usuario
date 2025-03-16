import tkinter as tk
from tkinter import ttk, messagebox

# Carreras en línea de la Universidad Estatal Amazónica UEA
carreras_en_linea = [
    "Licenciatura en Educación Básica",
    "Licenciatura en Educación Inicial",
    "Ingeniería en Tecnologías de la Información",
    "Turismo",
    "Comunicación",
    "Economía"
]

# Función para agregar datos ingresados por el usuario a la tabla
def agregar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    residencia = entry_residencia.get()
    correo = entry_correo.get()
    carrera = combo_carreras.get()

    if nombre and edad and residencia and correo and carrera:
        datos.insert("", "end", values=(nombre, edad, residencia, correo, carrera))
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_residencia.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        combo_carreras.set("")
    else:
        messagebox.showwarning("Campos incompletos", "Por favor, complete todos los campos.")

# Función para limpiar la tabla de datos
def limpiar_datos():
    for item in datos.get_children():
        datos.delete(item)

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Carreras en Línea UEA")
ventana.geometry("800x500")  # Ajusta el tamaño de la ventana
ventana.configure(bg="Light Gray")  # Color de fondo

# Configuración del diseño con grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=2)

# Etiquetas y entrada para los nombres
tk.Label(ventana, text="Nombres:", bg="Light Gray").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nombre = tk.Entry(ventana, width=50)
entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Etiqueta y entrada para la edad
tk.Label(ventana, text="Edad:", bg="Light Gray").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_edad = tk.Entry(ventana, width=50)
entry_edad.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Etiqueta y entrada para el lugar residencia
tk.Label(ventana, text="Lugar de residencia:", bg="Light Gray").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_residencia = tk.Entry(ventana, width=50)
entry_residencia.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Etiqueta y entrada para el e-mail
tk.Label(ventana, text="Correo:", bg="Light Gray").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_correo = tk.Entry(ventana, width=50)
entry_correo.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Etiqueta y selección de carrera
tk.Label(ventana, text="Carrera de interés:", bg="Light Gray").grid(row=4, column=0, padx=10, pady=5, sticky="e")
combo_carreras = ttk.Combobox(ventana, values=carreras_en_linea, state="readonly", width=47)
combo_carreras.grid(row=4, column=1, padx=10, pady=5, sticky="w")
combo_carreras.set("Seleccione una carrera")  # Texto por defecto

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar tus datos de registro", bg="green", fg="white", command=agregar_datos)
boton_agregar.grid(row=5, column=0, columnspan=2, pady=10)

# Tabla para mostrar los datos ingresados
datos = ttk.Treeview(ventana, columns=("Nombre", "Edad", "Residencia", "Correo", "Carrera"), show="headings")
datos.heading("Nombre", text="Nombre")
datos.heading("Edad", text="Edad")
datos.heading("Residencia", text="Residencia")
datos.heading("Correo", text="Correo")
datos.heading("Carrera", text="Carrera")
datos.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Botón para limpiar datos
boton_limpiar = tk.Button(ventana, text="Limpiar", bg="red", fg="white", command=limpiar_datos)
boton_limpiar.grid(row=7, column=0, columnspan=2, pady=10)

# Ejecutar la ventana principal
ventana.mainloop()