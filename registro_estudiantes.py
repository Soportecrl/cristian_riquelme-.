import tkinter as tk
from tkinter import messagebox

def registrar_estudiante():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    clase = entry_clase.get()
    seccion = entry_seccion.get()
    estado = estado_inscripcion.get()
    materias = [materia.get() for materia in materias_optativas if materia.get()]
    comentarios = text_comentarios.get("1.0", tk.END).strip()
    nivel = nivel_escolar.get()

    detalles = f"""
    Nombre: {nombre}
    Apellido: {apellido}
    Edad: {edad}
    Clase: {clase}
    Sección: {seccion}
    Estado: {estado}
    Materias optativas: {', '.join(materias)}
    Nivel escolar: {nivel}
    Comentarios: {comentarios}
    """

    print(detalles)
    messagebox.showinfo("Registro", "Estudiante registrado exitosamente")

def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_clase.delete(0, tk.END)
    entry_seccion.delete(0, tk.END)
    estado_inscripcion.set(None)
    for materia in materias_optativas:
        materia.set(0)
    text_comentarios.delete("1.0", tk.END)
    nivel_escolar.set("Primaria")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Registro de Estudiantes - InnovadoresX")

# Frame para datos personales
frame_personales = tk.Frame(ventana)
frame_personales.pack(padx=10, pady=10)

tk.Label(frame_personales, text="Nombre:").grid(row=0, column=0, sticky="e")
entry_nombre = tk.Entry(frame_personales)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_personales, text="Apellido:").grid(row=1, column=0, sticky="e")
entry_apellido = tk.Entry(frame_personales)
entry_apellido.grid(row=1, column=1)

tk.Label(frame_personales, text="Edad:").grid(row=2, column=0, sticky="e")
entry_edad = tk.Entry(frame_personales)
entry_edad.grid(row=2, column=1)

# Frame para detalles académicos
frame_academicos = tk.Frame(ventana)
frame_academicos.pack(padx=10, pady=10)

tk.Label(frame_academicos, text="Clase:").grid(row=0, column=0, sticky="e")
entry_clase = tk.Entry(frame_academicos)
entry_clase.grid(row=0, column=1)

tk.Label(frame_academicos, text="Sección:").grid(row=1, column=0, sticky="e")
entry_seccion = tk.Entry(frame_academicos)
entry_seccion.grid(row=1, column=1)

# Frame para estado de inscripción
frame_estado = tk.Frame(ventana)
frame_estado.pack(padx=10, pady=10)

estado_inscripcion = tk.StringVar(value=None)
tk.Radiobutton(frame_estado, text="Inscrito", variable=estado_inscripcion, value="Inscrito").pack(side=tk.LEFT)
tk.Radiobutton(frame_estado, text="No Inscrito", variable=estado_inscripcion, value="No Inscrito").pack(side=tk.LEFT)

# Frame para materias optativas
frame_materias = tk.Frame(ventana)
frame_materias.pack(padx=10, pady=10)

materias_optativas = [tk.StringVar() for _ in range(4)]
tk.Checkbutton(frame_materias, text="Matemáticas", variable=materias_optativas[0], onvalue="Matemáticas", offvalue="").pack(side=tk.LEFT)
tk.Checkbutton(frame_materias, text="Ciencias", variable=materias_optativas[1], onvalue="Ciencias", offvalue="").pack(side=tk.LEFT)
tk.Checkbutton(frame_materias, text="Historia", variable=materias_optativas[2], onvalue="Historia", offvalue="").pack(side=tk.LEFT)
tk.Checkbutton(frame_materias, text="Deportes", variable=materias_optativas[3], onvalue="Deportes", offvalue="").pack(side=tk.LEFT)

# Frame para comentarios adicionales
frame_comentarios = tk.Frame(ventana)
frame_comentarios.pack(padx=10, pady=10)

tk.Label(frame_comentarios, text="Comentarios:").pack(anchor="w")
text_comentarios = tk.Text(frame_comentarios, height=4, width=50)
text_comentarios.pack()

# Menú desplegable para nivel escolar
frame_nivel = tk.Frame(ventana)
frame_nivel.pack(padx=10, pady=10)

tk.Label(frame_nivel, text="Nivel Escolar:").pack(anchor="w")
nivel_escolar = tk.StringVar(value="Primaria")
opciones_nivel = tk.OptionMenu(frame_nivel, nivel_escolar, "Primaria", "Secundaria")
opciones_nivel.pack()

# Frame para botones de acción
frame_botones = tk.Frame(ventana)
frame_botones.pack(padx=10, pady=10)

boton_registrar = tk.Button(frame_botones, text="Registrar Estudiante", command=registrar_estudiante)
boton_registrar.pack(side=tk.LEFT, padx=5)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_formulario)
boton_limpiar.pack(side=tk.LEFT, padx=5)

# Ejecutar la ventana principal
ventana.mainloop()
