#   Determinar la cantidad a pagar

print("--------------------------")
print("------TOTAL - A - PAGAR-------")
print("--------------------------")

# input
m=int(input("Digite el tiempo de la llamada en minutos:"))

# procesing 
if m>3:
    mayor=300+50*(m-3)
else:
    mayor=300

# output

print("-----------------------")
print("--------RESULTADOS-----")
print("Total a pagar: $"+str(mayor))

#finish