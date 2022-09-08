# Ejercicio 10: 3 NUMEROS FORMADOS ASCENDENTEMENTE 


print("---------------------------------------")
print("---NUMEROS-ORDENADOS-ASCENDENTEMENTE---")
print("---------------------------------------")

#input
x = int(input("Ingrese el valor 1: "))
y = int(input("Ingrese el valor 2: "))
z = int(input("Ingrese el valor 3: "))

#procesing
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c

#output
print("Los numeros ordenados son: {}, {} y {} ".format(a, b, c) )

#finish