# Ejercicio 8: Ecuacion de segundo nivel 

print("-----------------------------------------")
print("---RESOLVER-LA-ECUACION-CUADRATICA-------") 
print("-----------------------------------------")

#input
from math import sqrt
A = int(input("Ingrese el valor de a: "))
B = int(input("Ingrese el valor de b: "))
C = int(input("Ingrese el valor de c: "))

#procesing
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print("x1= ",x1)
  print("x2= ",x2)
  
  #finish 