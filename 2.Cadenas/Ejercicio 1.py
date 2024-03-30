#Ejercicios de cadenas

#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

from tabulate import tabulate

nombre = input("Ingrese nombre de usuario: ")
número = int(input("Ingrese número de repeticiones: "))

datos = []
for n in range (1, número + 1):
    datos.append([n,nombre])

encabezados = ["Nro","Nombre"]

tabla = tabulate(datos, headers=encabezados, tablefmt="grid")

print(tabla)