#Ejercicio de cadena

#Escribir un programa que pregunte por consola el precio de un producto en euros 
# con dos decimales y muestre por pantalla el número de euros y el número de céntimos 
# del precio introducido.

from tabulate import tabulate

price = input("Ingrese precio con dos decimales: ")
euros = (price[:price.find(',')])
cent = (price[price.find(',')+1:])

data = []

data.append([price, euros, cent])

headers = ('Precio', 'Euros', 'Centimos')

tabla = tabulate(data, headers=headers, tablefmt="grid")

print(tabla)
