conteo_equipos = {}
suma_edades = {}
conteo_articulos = {}
total_dias = 0

print("EQUIPOS DE FUTBOL COLOMBIANOS")

for i in range(10):
    print(f"Fanático {i+1}")
    
    edad = int(input("Ingresa su edad: "))
    equipo = input("Ingresa su equipo favorito: ")
    
    print("¿Qué artículo prefiere? (camiseta, chaqueta, gorra, morral): ")
    articulo = input()
    
    print("Cantidad de días al año que asiste al estadio: ")
    dias = int(input())
    
    if equipo in conteo_equipos:
        conteo_equipos[equipo] += 1
        suma_edades[equipo] += edad
    else:
        conteo_equipos[equipo] = 1
        suma_edades[equipo] = edad
    
    if articulo in conteo_articulos:
        conteo_articulos[articulo] += 1
    else:
        conteo_articulos[articulo] = 1
    
    total_dias += dias

print("\nCantidad de fanáticos por equipo:")
for equipo in conteo_equipos:
    print(equipo, ":", conteo_equipos[equipo])

print("\nPromedio de edades por equipo:")
for equipo in conteo_equipos:
    promedio = suma_edades[equipo] / conteo_equipos[equipo]
    print(equipo, ":", promedio)

articulo_preferido = max(conteo_articulos, key=conteo_articulos.get)
print("\nArtículo más preferido:", articulo_preferido)

promedio_dias = total_dias / 10
print("\nPromedio de días al estadio:", promedio_dias)