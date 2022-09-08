# Ejercicio 6: Determinar si la suma de sus ultimas 2 cifras es es un numero de 1 digito 

print("---------------------------------")
print("--- SUMA-ULTIMOS-2-DIGITOS--- ---")
print("---------------------------------")

# input
n=int(input("ingrese un valor"))
#procesing
n2= n % 10
n1= (n % 100) // 10

suma = n1+n2

if suma>=1 and suma<=9:
    print("La suma de" ,n1, "y" ,n2,  " da: " + str(suma)+ " que es un numero de 1 digito")
else:
    print("La suma de" ,n1,"y", n2," da: " +str(suma)+ " que no es un numero de 1 digito")

#finish