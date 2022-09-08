# Ejercicio 3: numero positivo de 4 cifras 

print("------------------------------------")
print("------NUMERO-POSITIVO-DE-4-CIFRAS---")
print("------------------------------------")

#input
n=int(input("Digite un numero:"))

#procesing
if (n>=1000 and n<=9999):
    print("El dato ingresado es un numero positivo de 4 cifras")
else:
     print("El dato ingresado no es numero positivo de 4 cifras")

#finish