#Ejercicio de cadena

#Escribir un programa que pregunte por consola por los productos de una 
# cesta de la compra, separados por comas, y muestre por pantalla cada 
# uno de los productos en una línea distinta.

from tabulate import tabulate

lista = input("Ingresa una lista de mercado separada por comas: ")

productos = lista.split(',')

data = []

for n, productos in enumerate(productos, 1):
    
    data.append([n,productos.strip()])

headers = ('Nro', 'Producto')

tabla = tabulate(data, headers=headers, tablefmt="grid")

print(tabla)