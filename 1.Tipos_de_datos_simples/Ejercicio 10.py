#Ejercicios de Tipos de Datos Simples

#10: Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa 
# de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada 
# paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas 
# vendidos en el último pedido y calcule el peso total del paquete que será enviado.

payasos = int(input("Ingrese al pedido el número de payasos: "))
muñecas = int(input("Ingrese al pedido el número de muñecas: "))
peso_total = (payasos * 112) + (muñecas * 75)
print("Será enviado un paquete con un peso de ", peso_total,"g")
 