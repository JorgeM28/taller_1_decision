# Ejercicio 5: Determinar si sus ultimos 2 digitos son iguales

print("---------------------------------")
print("--- ULTIMOS-2-DIGITOS-IGUALES ---")
print("---------------------------------")

# input
n = input("Digite un numero : ")
n = int(n)

#procesing
n2= n % 10
n1= (n % 100) // 10

if n1==n2:
    print("el numero",n2, "y" ,n1,"son iguales")
else:
    print("el numero",n2, "y" ,n1,"son diferentes")

#finish