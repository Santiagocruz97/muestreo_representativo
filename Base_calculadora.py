from tabulate import tabulate
print("Determinación del tamaño de una muestra (n) para una población (N) finita o infinita")
tipo_poblacion = input('¿Tu población es finita ("F") o infinita ("I")? ').upper()
print("Muy bien, ahora vamos a escoger los parametros a usar")
if tipo_poblacion=="F":
    poblacion_N=float(input("¿Cual es el valor de tu Poblacion?: "))
else: print("Listo, tu Poblacion es 'infinita' ")
nivel_de_confianza_tabla = [
    ["80%", 1.28],
    ["85%", 1.44],
    ["90%", 1.64],
    ["95%", 1.96],
    ["98%", 2.33],
    ["99%", 2.58]
]
encabezados = ["Nivel de confianza", "Valor Z (Z-score)"]
print(tabulate(nivel_de_confianza_tabla, headers=encabezados, tablefmt="grid"))
nivel_de_confianza= float(input("¿Según la tabla, cúal va a ser tu nivel de confianza (Valor Z)?: "))
proporcion_esperada=float(input("¿Cuál es el valor de tu proporcion esperada?, Si es un valor desconocido, digita 0.5: "))
margen_de_error_tolerado_tabla = [
    ["0.10(10%)", "Mas Permisivo = Menos Muestras"],
    ["0.05(5%)", "Estandar para la mayoria de estudios"],
    ["0.03(3%)", "Mas Riguroso = Mas Muestras"],
    ["0.01(1%)", "Muy Riguroso = Muchas Mas Muestras"]
]
encabezados = ["Margen de error (e)", "Interpretacion"]
print(tabulate(margen_de_error_tolerado_tabla, headers=encabezados, tablefmt="grid"))
margen_de_error_tolerado=float(input("¿Según la tabla, cúal va a ser tu nivel de Margen de error (e), en decimales?: "))
if tipo_poblacion=="F":
    muestra_representativa_finita=(poblacion_N*(nivel_de_confianza**2)*proporcion_esperada*(1-proporcion_esperada))/((margen_de_error_tolerado**2)*(poblacion_N-1)+(nivel_de_confianza**2)*proporcion_esperada*(1-proporcion_esperada))
    print(f"Tu Numero de muestras para obtener representatividad segun tu poblacion y parametros establecidos es de: {round(muestra_representativa_finita,0)}")
else: 
    muestra_representativa_infinita=((nivel_de_confianza**2)*proporcion_esperada*(1-proporcion_esperada))/((margen_de_error_tolerado**2))
    print(f"Tu numero de muestras debe ser de: {round(muestra_representativa_infinita,0)}")                                                                                                        



