#Nombre:Jeison arley casadiegos
#Grupo:213022_334
#Programa: Ing telecomunicaciones+
#Código:autoría_propia

print("EQUIPOS DE FUTBOL COLOMBIANOS")

# lista con la informacion
equipos= []
edades = [] 
dias_estadio=[]
articulos = [] 

# Datos ingresados por el usuario
for i in range(3):
    print(f"\nFanático {i+1}")
    
    edad = int(input("Ingresa su edad: "))
    equipos_favoritos = input("Ingresa su equipo favorito: ")
    
    print("Que articulo prefiere (camiseta, chaqueta, gorra, morral): ")
    articulo_favorito = input()
    
    dias = int(input("Cantidad de días al año en los cuales asiste al estadio: "))

    # guardar datos
    edades.append(edad)
    equipos.append(equipos_favoritos)
    dias_estadio.append(dias)
    articulos.append(articulo_favorito)

# -------- CANTIDAD POR EQUIPO --------
print("\nCantidad de fanáticos por equipo:")

for i in range(3):
    contar = 0
    for j in range(3):
        if equipos[i] == equipos[j]:
            contar += 1
    print(equipos[i], ":", contar)

# -------- PROMEDIO EDADES --------
print("\nPromedio de edades por equipos de futbol:")

for i in range(3):
    suma = 0
    contar = 0
    for j in range(3):
        if equipos[i] == equipos[j]:
            suma += edades[j]
            contar += 1
    promedio = suma / contar
    print(equipos[i], ":", promedio)

# -------- ARTÍCULO MÁS PREFERIDO --------
print("\nArtículo más preferido por los fanáticos:")

mayor = 0
articulo_popular = ""

for i in range(3):
    contar = 0
    for j in range(3):
        if articulos[i] == articulos[j]:
            contar += 1
    if contar > mayor:
        mayor = contar
        articulo_popular = articulos[i]

print(articulo_popular)


suma_dias = 0

for i in range(3):
    suma_dias += dias_estadio[i]

promedio_dias = suma_dias / 3

print("\nPromedio de días que acuden los fanáticos al estadio:", promedio_dias)