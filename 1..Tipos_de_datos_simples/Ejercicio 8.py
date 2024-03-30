#Ejercicios de Tipos de Datos Simples

#8: Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un c <c> y un resto <r> donde 
# <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el c y el resto de la división entera respectivamente.

n = int(input("Ingrese númerp para el n: "))
m = int(input("Ingrese númerp para el m: "))
c = n // m
r = n % m

print("El resultado de la división entre ",n, "y ", m, "da como c ", c, "y deja un r de ", r )