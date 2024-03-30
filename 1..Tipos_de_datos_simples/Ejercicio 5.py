#Ejercicios tipos de datos simples

#5: Escribir un programa que pregunte al usuario por el número de 
# horas trabajadas y el coste por hora. Después debe mostrar por 
# pantalla la paga que le corresponde.
h_trabajadas = int(input("Ingrese el número de horas trabajadas: "))
v_hora = int(input("Ingrese el valor de una hora trabajada: "))
pago = h_trabajadas * v_hora
print("El valor de la hora es: " , pago)
