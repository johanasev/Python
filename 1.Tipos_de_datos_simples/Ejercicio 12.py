# Ejercicios de Tipos de Datos Simples

# 12. Una panadería vende barras de pan a 3.49€ cada una.
# El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas
# que no son del día. Después el programa debe mostrar el precio habitual
# de una barra de pan,# el descuento que se le hace por no ser fresca y el
# coste final total.

from tabulate import tabulate

valor_pan = 3.49

barra = int(input("Ingresa el número de barras a comprar" "que no son del día: "))

pan_dia = barra * valor_pan
pan_nodia = round((barra * valor_pan) - (barra * valor_pan) * 0.60, 2)
datos = [[valor_pan, "1", "60%"], [pan_dia, barra, pan_nodia]]
encabezados = ["Precio habitual", "Cant barras", "Precio con descuento"]

tabla = tabulate(datos, headers=encabezados, tablefmt="grid", stralign="center")

print(tabla)
