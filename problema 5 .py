#Nombre:Jeison arley casadiegos
#Grupo:213022_334
#Programa: Ing telecomunicaciones+
#Código:autoría_propia

print("EQUIPOS DE FUTBOL COLOMBIANOS")
# Listas donde  guardare la informacion recolectada
equipos = []
edades = [] 
dias_estadio = []
articulos = [] 

# Informacion solicitada a los fanaticos de futbool
for i in range(10):
    print(f"fanatico de futbol {i+1}")
    while True:
        try:
             edad = int(input("ingresa su edad: "))
             break
        except ValueError:
             print("Error: escribe solo numeros para la edad")

    equipo_favorito = input("ingresa su equipo favorito: ")
    articulo_favorito = input("articulo preferido (camiseta, chaqueta, gorra, morral con logo): ")

    # con while creo un condicional para que el usuario solo digite cantidad numericas y s idigita letra le muestra el error
    while True:
        try:
            dias = int(input("cantidad de dias al año en los cuales asiste al estadio: "))
            break 
        except ValueError:
            print("Error: ingresa solo numeros para los dias")



    #guardo la informacion en las listas 
    edades.append(edad)
    equipos.append(equipo_favorito)
    articulos.append(articulo_favorito)
    dias_estadio.append(dias)


print("RESULTADOS OBTENIDOS EN LA ENCUESTA: ")

print("cantidad de fanaticos por equipo: ")

for equipo in set(equipos):   # set elimina duplicados
    cantidad = equipos.count(equipo) # count cuenta cuantos hinchas tiene cada equipo
    print(f"{equipo}: {cantidad} hinchas")

promedio_edades = sum(edades) / len(edades) # len cuenta cuantos elementos hay en una lista
print(f"promedio de edades de todos los hinchas: {promedio_edades} años")

mas_repetido = "no definido"
mayor_cantidad = 0

for articulo in set(articulos):
    cantidad = articulos.count(articulo)
    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        mas_repetido = articulo

print(f"el artículo más preferido es: ", mas_repetido)


promedio_dias = sum(dias_estadio) / len(dias_estadio)
print(f"promedio de dias que asisten en el año al estadio: {promedio_dias}")
