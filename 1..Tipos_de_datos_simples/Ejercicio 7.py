#Ejercicios de Tipos de Datos Simples

#7: Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable,
# y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))
imc = peso / estatura**2

if imc > 18.5 and imc < 24.9:
    print("Tu indice de masa corporal es: ", imc, " --SALUDABLE--")
elif imc >25.0 and imc < 29.0:
    print("Tu indice de masa corporal es: ", imc, " --SOBREPESO--")
else:
    print("Tu indice de masa corporal es: ", imc, " --OBESIDAD--")
