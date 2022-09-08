# Ejercicio 4: Determinar si el ultimo numero es par 

print("------------------------")
print("--- ULTIMO-NUMERO-PAR ---")
print("------------------------")

# input
n = input("Digite un numero : ")
n = int(n)

#procesing
x= n % 10
if x %2 == 0:
    print("el numero",x,"es par")
else:
    print("el numero",x,"es impar")

#finish