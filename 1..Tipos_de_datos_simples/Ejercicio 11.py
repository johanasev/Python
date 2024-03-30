#Ejercicios de Tipos de Datos Simples

#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, 
# se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida 
# por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

ahorro = float(input("Ingrese el monto del ahorro $"))
interes = 0.04
año1 = round(ahorro * (1 + interes)**1,2)
año2 = round(ahorro * (1 + interes)**2,2)
año3 = round(ahorro * (1 + interes)**3,2)

print("El monto ahorrado con el interes es:"'\n'"Promer año: $",año1,'\n',"Segundo año: $",año2,'\n', "Tercer año: $",año3,'\n')