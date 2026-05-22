#Nombre:Jeison arley casadiegos
#Grupo:213022_334
#Programa: Ing telecomunicaciones+
#Código:autoría_propia

print("Bienvenido A Juguetería Mundo Mágico")
print("Ingresa la cantidad del pedido de payasos de tela:")
cantidad_payasos= int(input())
print("Ingresa la cantidad del pedido de muñecas clásica:")
cantidad_muñeca= int(input())
peso_payasos_gramos = 112
peso_muñecas_gramos = 75
valor_total_pedido_gramos= (cantidad_payasos*peso_payasos_gramos)+(cantidad_muñeca * peso_muñecas_gramos)
print ("su valor total del pedido en gramos es:",
       valor_total_pedido_gramos)