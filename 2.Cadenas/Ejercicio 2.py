#Ejercicios de cadenas

#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, 
# una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

from tabulate import tabulate

nombre = input("Ingresa nombre de usario: ")

minus = nombre.lower()
mayusc = nombre.upper()
title = nombre.title()

datos = [
    [1, minus],
    [2, mayusc],
    [3, title]
]
    
encabezados = ["Nro","Palabra"]

tabla = tabulate(datos, headers=encabezados, tablefmt="grid")

print (tabla)