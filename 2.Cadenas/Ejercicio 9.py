#Ejercicio de cadena

#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato 
# dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa 
# anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

from tabulate import tabulate

fecha = input("Ingrese fecha de nacimiento: ")

data = []
dia = fecha[:2]
mes = fecha[3:5]
año = fecha[6:]

data.append([fecha, dia, mes, año])

headers = ('Fecha de nacimiento', 'Día', 'Mes', 'Año')

tabla = tabulate(data, headers=headers, tablefmt="grid")

print(tabla)