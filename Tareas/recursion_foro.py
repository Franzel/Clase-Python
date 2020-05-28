# def recursion(numero):
#     if (numero==1):
#         print("caso base alcanzado")
#         return 1
#     else:
#         # suma = 0
#
#         # print("suma=", suma, end=" - ")
#         suma = numero + recursion(numero-1)
#         print("suma:",str(suma), "+", "numero:", str(numero), "recursion:", numero-1)
#         # print("suma mas numero=", suma + numero)
#     return suma
#
# recursion(10)

def recursion(numero, letra):
    if(numero>1):
        numero-=1
        letra += str(numero)
        letra += recursion(numero, letra)
        print(numero, ":", letra)
    else:
        print("fin")
    return letra

recursion(8, " . ")