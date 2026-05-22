# Programa: Matriz cuadrada con operaciones

# 1. Pedir la dimensión de la matriz
n = int(input("Ingrese la dimensión de la matriz cuadrada: "))

# 2. Crear la matriz con números ingresados por el usuario
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        num = int(input(f"Ingrese un número de 4 cifras para posición ({i},{j}): "))
        # Validar que sea de 4 cifras
        while num < 1000 or num > 9999:
            num = int(input("Número inválido. Ingrese un número de 4 cifras: "))
        fila.append(num)
    matriz.append(fila)

# 3. Mostrar la matriz
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# 4. Encontrar mayor y menor
mayor = matriz[0][0]
menor = matriz[0][0]

for i in range(n):
    for j in range(n):
        if matriz[i][j] > mayor:
            mayor = matriz[i][j]
        if matriz[i][j] < menor:
            menor = matriz[i][j]

print(f"\nNúmero mayor: {mayor}")
print(f"Número menor: {menor}")

# 5. Suma y verificar si es capicúa
suma = mayor + menor
print(f"Suma de mayor y menor: {suma}")

# Verificar capicúa
suma_str = str(suma)
if suma_str == suma_str[::-1]:
    print("La suma es un número capicúa.")
else:
    print("La suma NO es un número capicúa.")

# 6. Sumatoria de pares
suma_pares = 0
for i in range(n):
    for j in range(n):
        if matriz[i][j] % 2 == 0:
            suma_pares += matriz[i][j]

print(f"\nSumatoria de números pares: {suma_pares}")

# 7. Convertir a binario
binario = bin(suma_pares)[2:]
print(f"Representación binaria: {binario}")
