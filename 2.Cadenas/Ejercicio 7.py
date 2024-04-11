#Ejercicio de cadena

# Escribir un programa que pregunte el correo electrónico del usuario 
# en la consola y muestre por pantalla otro correo electrónico con el 
# mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

from tabulate import tabulate
import random

cant = int(input("Ingrese cant de correos: "))
final = "@gmail.com"

def users():
    nombres = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Diego", "Sofía"]
    apellidos = ["Gómez", "Pérez", "López", "Rodríguez", "Fernández", "Martínez", "González", "Ramírez"]

    nombresal = random.choice(nombres)
    apellidosal = random.choice(apellidos)
    email = f"{nombresal}.{apellidosal}{final}"
    
    return email

data = []
for n in range(1, cant+1):
    email = users()
    new_email = f"{email[:email.find('@')] + '@ceu.es'}"
    
    data.append([n, email, new_email])

headers = ('Nro', 'Email ingresado', 'Nuevo email')

tabla = tabulate(data, headers=headers, tablefmt="grid")

print(tabla)
