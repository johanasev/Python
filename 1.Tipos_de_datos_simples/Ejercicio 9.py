#Ejercicios de Tipos de Datos Simples

#9:Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión. 

inversion = float(input("Ingrese la cantiddad a invertir $ "))
interes = float(input("Ingrese el interes anual: "))   
años = int(input("Ingrese el número de años: "))

total_inv = round(inversion * (interes / 100 + 1) ** años, 2)

print("Con una inversión de $ ",inversion, "por un intres anual de ", interes, "%" " a ",años, "años, "'\n' "obtienes un capital final de $ ", total_inv)
