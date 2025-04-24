import tkinter as tk
from tkinter import ttk, messagebox

# Función para calcular el tamaño de muestra
def calcular():
    try:
        tipo = tipo_var.get()
        Z = float(z_var.get())
        p = float(p_var.get())
        e = float(e_var.get())
        q = 1 - p

        if tipo == "F":
            N = float(n_var.get())
            n = (N * Z**2 * p * q) / ((e**2 * (N - 1)) + (Z**2 * p * q))
            resultado = f"Tamaño de muestra (finita): {round(n, 0):,.0f}"
        else:
            n = (Z**2 * p * q) / (e**2)
            resultado = f"Tamaño de muestra (infinita): {round(n, 0):,.0f}"

        resultado_var.set(resultado)
    except Exception as ex:
        messagebox.showerror("Error", f"Ocurrió un error: {ex}")

# Crear ventana principal con Canvas y Scrollbar
ventana = tk.Tk()
ventana.title("Calculadora de Tamaño de Muestra")
ventana.geometry("550x770")
ventana.resizable(False, False)

canvas = tk.Canvas(ventana, borderwidth=0)
frame_contenido = tk.Frame(canvas)
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((0, 0), window=frame_contenido, anchor="nw")

# Actualizar scroll region
def ajustar_scroll(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame_contenido.bind("<Configure>", ajustar_scroll)

# Variables de control
tipo_var = tk.StringVar(value="F")
z_var = tk.StringVar(value="1.96")
p_var = tk.StringVar(value="0.5")
e_var = tk.StringVar(value="0.05")
n_var = tk.StringVar(value="10000")
resultado_var = tk.StringVar()

# Encabezado con fórmulas
tk.Label(frame_contenido, text="Fórmulas utilizadas", font=("Arial", 11, "bold"), fg="black").pack(pady=(10, 0))
tk.Label(frame_contenido, text="Población finita:", font=("Arial", 10, "bold")).pack()
tk.Label(frame_contenido, text="n = (N * Z² * p * q) / [(e² * (N - 1)) + (Z² * p * q)]").pack()
tk.Label(frame_contenido, text="Población infinita:", font=("Arial", 10, "bold")).pack()
tk.Label(frame_contenido, text="n = (Z² * p * q) / e²").pack()
tk.Label(frame_contenido, text="Estas fórmulas permiten calcular el tamaño de muestra necesario para estimar una\nproporción poblacional con un nivel de confianza y margen de error definidos.", wraplength=500, justify="center", fg="gray").pack(pady=(0, 15))

# Interfaz gráfica
tk.Label(frame_contenido, text="Tipo de población (F = Finita, I = Infinita)").pack()
ttk.Combobox(frame_contenido, textvariable=tipo_var, values=["F", "I"]).pack()

tk.Label(frame_contenido, text="Nivel de confianza (Z): valor estadístico que indica cuánta certeza deseas tener en el resultado").pack()
tk.Entry(frame_contenido, textvariable=z_var).pack()

tk.Label(frame_contenido, text="Proporción esperada (p): proporción esperada de éxito en la población, usar 0.5 si se desconoce").pack()
tk.Entry(frame_contenido, textvariable=p_var).pack()

tk.Label(frame_contenido, text="Margen de error (e): tolerancia de error que aceptas en los resultados, en decimales").pack()
tk.Entry(frame_contenido, textvariable=e_var).pack()

frame_n = tk.Frame(frame_contenido)
tk.Label(frame_n, text="Tamaño de población (N): número total de elementos en la población (solo para población finita)").pack()
tk.Entry(frame_n, textvariable=n_var).pack()
frame_n.pack()

tk.Button(frame_contenido, text="Calcular", command=calcular).pack(pady=(10, 5))
tk.Label(frame_contenido, textvariable=resultado_var, font=("Arial", 12, "bold"), fg="blue").pack(pady=(0, 5))

# Tablas informativas
frame_tablas = tk.Frame(frame_contenido)
tk.Label(frame_tablas, text="Tabla de Nivel de Confianza (Z-score)", font=("Arial", 10, "bold")).pack(pady=5)
tk.Label(frame_tablas, text="Indica el grado de certeza del resultado: a mayor Z, mayor confianza.\n80%  →  1.28\n85%  →  1.44\n90%  →  1.64\n95%  →  1.96\n98%  →  2.33\n99%  →  2.58", justify="left").pack()

tk.Label(frame_tablas, text="\nTabla de Margen de Error (e)", font=("Arial", 10, "bold")).pack(pady=5)
tk.Label(frame_tablas, text="Define el rango de error aceptable en los resultados:\n0.10 → Más permisivo = menos muestras\n0.05 → Estándar para la mayoría de estudios\n0.03 → Más riguroso = más muestras\n0.01 → Muy riguroso = muchas más muestras", justify="left").pack()
frame_tablas.pack(pady=(0, 10))

# Créditos
tk.Label(frame_contenido, text="Aplicación desarrollada por Santiago Cruz", font=("Arial", 8), fg="gray").pack(side="bottom", pady=10)

ventana.mainloop()
