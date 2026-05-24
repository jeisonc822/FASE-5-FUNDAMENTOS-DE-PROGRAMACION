#Nombre:Jeison arley casadiegos
#Grupo:213022_334
#Programa: Ing telecomunicaciones

#se realiza la creacion de una matriz con los recursos de nombre de empleados y las horas trabajas de lunes a viernes

empleados= [
    ["Maria Vargas", 8,8,9,8,7],
    ["Pedro Flores", 9,8,10,8,9],
    ["Dayana Casadiegos", 10,9,8,10,9],
    ["Jeison Casadiegos", 8,6,9,8,9]
]
# se crea una variable con un umbral de horas para determinar si un empleado ha trabajado horas extras o no, el cual se establece en 40 horas semanales
UMBRAL_HORAS = 40
def calcular_jornada_laboral(datos_empleado):
    total_horas =sum(datos_empleado[1:]) # se realiza la suma de las horas trabajadas por cada empleado utilizando la función suma y se omite el nombre del empleado que se encuentra en la primera posición de cada sublista
    if total_horas > UMBRAL_HORAS:
        clasificacion ="sobretiempo"
    else:
        clasificacion ="horario estandar"
    return total_horas, clasificacion

for datos_empleado in empleados:
    nombre = datos_empleado[0]
    total_horas, clasificacion = calcular_jornada_laboral(datos_empleado)
    print(f"Empleado: {nombre}")
    print(f"Total Horas Trabajadas: {total_horas}")
    print(f"Clasificacion:  {clasificacion}")

    print("=" * 35) 
    #separador para que el codigo sea mas organizado en la impresion