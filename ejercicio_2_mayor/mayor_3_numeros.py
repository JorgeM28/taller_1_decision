# Hallar el mayor de 3 num

print("--------------------------")
print("------MAYOR - 3 ENTEROS---")
print("--------------------------")

# input
a=int(input("Digite el primer numero:"))
b=int(input("Digite el segundo numero:"))
c=int(input("Digite el tercer numero:"))

# procesing 
if a>b:
    if a>c:
        mayor = a
    else:
        mayor = c
else:
    if b>c:
        mayor = b
    else:
        mayor = c

# output
print("-----------------------")
print("--------RESULTADOS-----")
print ( "El mayor entre "  +  str ( a ) +  ", "  +  str ( b ) +  " y "  +  str ( c ) +  " es: "  +  str ( mayor ))
