# Ejercicio 9 Descuentos en un negocio 


print("------------------------------")
print("---DESCUENTO EN UN NEGOCIO:---")
print("------------------------------")

#INPUT
n=input("Digite el tipo de cliente: General(G) o Afiliado(A)  : ")
v=input("Digite el monto de la compra : ")
p=input("Digite el modo de pago : contado(C) o plazos(P) : ")
v=int(v)

#procesing
if n == 'G' and p=='C':
    total=v-((v*15)/100)
    print("El total a pagar es : "  +str(total))

if n == 'G' and p=='P':
    total=v-((v*10)/100)
    print("El total a pagar es : "  +str(total))

if n == 'A' and p=='C':
    total=v-((v*20)/100)
    print("El total a pagar es : "  +str(total))

if n == 'A' and p=='P':
    total=v-((v*5)/100)
    print("El total a pagar es : "  +str(total))

#finish