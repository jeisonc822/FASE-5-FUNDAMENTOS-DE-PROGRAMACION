#Nombre:Jeison arley casadiegos
#Grupo:213022_334
#Programa: Ing telecomunicaciones


# Datos iniciales de los empleados
DATOS_EMPLEADOS = [
 {"nombre": "Ana García", "horas": 160, "tarifa": 15.5},
 {"nombre": "Luis Pérez", "horas": 150, "tarifa": 18.0},
 # se realiza la correcion de horas la cual estaba como string y debia ser un numero entero
 {"nombre": "Marta López", "horas": 165, "tarifa": 12.0}
]
TASA_DESCUENTO = 0.15
def calcular_bruto(h, t):
 """Calcula el salario bruto."""
 return h * t
# se realiza la correcion  la cual queria concatenar un numero con un string lo cual no es posible y se corrige para que se pueda realizar la operacion de multiplicacion
def calcular_neto(salario_bruto):
 """Calcula el salario neto aplicando el descuento."""
 descuento = salario_bruto * TASA_DESCUENTO
 #se realiza corecion de la variable tasa_descuento la cual estaba mal escrita y se corrige para que se pueda realizar la operacion de multiplicacio
 return salario_bruto - descuento
def generar_informe(lista_empleados):
    print("=== INFORME DE SALARIOS ===")
    for empleado in lista_empleados:
        nombre = empleado['nombre']
        horas = empleado['horas']
        tarifa = empleado['tarifa']

        salario_bruto = calcular_bruto(horas, tarifa)
        salario_neto = calcular_neto(salario_bruto)

        print(f"Empleado: {nombre}")
        print(f"  Salario Bruto: ${salario_bruto:.2f}")
        print(f"  Salario Neto: ${salario_neto:.2f}")
        print("-" * 30)

generar_informe(DATOS_EMPLEADOS)

