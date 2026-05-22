#Nombre:Jeison arley casadiegos
#Grupo:213022_334
#Programa: Ing telecomunicaciones+
#Código:autoría_propia

numero_dimension = int(input("porfavor ingresa la dimeension de la matriz: "))
#creo la matriz donde van ingresados los numeros
matriz=[]
for i in range(numero_dimension):
    fila=[]
    for j in range(numero_dimension):
        # solicitar al usuario que ingrese un numero de 4 cifras 
        num=int(input(f"ingresa un numero de 4 cifras para la posicion({i},{j}):"))
        # valido si el numero si es de 4 cifras o no 
        while num < 1000 or num > 9999:
            num=int(input("numero invalido. ingresa un numero de 4 cifras: "))
        fila.append(num)
    matriz.append(fila)    
# proyecto la matriz con los numeros ingresados
    print("matriz ingresada")
    for fila in matriz:
        print(fila)

 # valido que numero es mayor y menor
numero_mayor= matriz[0][0]
numero_menor= matriz[0][0]

for i in range(numero_dimension):
    for j in range(numero_dimension):
        if  matriz[i][j]< numero_menor:
            numero_menor= matriz[i][j]
        if matriz[i][j]>numero_mayor:
            numero_mayor= matriz[i][j]    
#se imprime el numero mayor y menor  
print(f"el numero mayor:{numero_mayor}") 
print(f"el numero menor:{numero_menor}")       

# se suma el numero mayor y menor 

suma= numero_mayor+numero_menor
print(f"la suma de mayor y menor:{suma}")
 
# validacion si el numero es un capicua se lee igual al revez
suma_str= str(suma)
if suma_str==suma_str[::-1]:
    print("la suma es un numero capicua")
else:
    print("la suma no es un numero capicua ")



# realizo la suma de los numeros pares
suma_numeros_paares= 0
for i in range(numero_dimension):
    for j in range(numero_dimension):
        if matriz[i][j] % 2 == 0:
            suma_numeros_paares += matriz[i][j]

print (f"la suma de loa numeros pares:{suma_numeros_paares}")   

# por ultimo convierto los numeros pares a binarios  
binario= bin(suma_numeros_paares)[2:] 
print(f"representacion en binarios:{binario}")      



