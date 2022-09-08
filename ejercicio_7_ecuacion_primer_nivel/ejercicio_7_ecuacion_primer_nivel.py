# Ejercicio 7: Ecuacion de primer nivel 

print("-----------------------------------------")
print("---RESOLVER-LA-SIGUIENTE-ECUACION: mx+b=0") 
print("-----------------------------------------")

#input

m= int(input("ingrese el valor de m: "))
b= int(input("ingrese el valor de b: "))

#procesing
if b>0:
    x=-b/m
    print("x=" +str(x))
else:
    x=b/m
    print("x=" +str(x))

#finish