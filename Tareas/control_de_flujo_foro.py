#En este modulo vimos 'casting', que es convertir el tipo de data
#por ejemplo, convertir input de texto de str a int
#vimos tambien los operadores aritmeticos y comparaciones

#aca un ejemplo sencillo de un juego de adivinanzas
import random

print("este es un juego de las adivinanzas.")
print("Tengo un numero del 1 al 5 y debes adivinar cuál es")
print("Tienes tres oportunidades, vamos...")
numero_secreto = random.randint(1,5)
print("ingresa un número:")

op1 = int(input())
if(numero_secreto==op1):
    print("que suerte, le achuntaste")
elif(numero_secreto>op1):
    print("prueba con un número mayor")
else:
    print("prueba con un número menor")

op2 = int(input())
if(numero_secreto==op2):
    print("que suerte, le achuntaste")
elif(numero_secreto>op2):
    print("prueba con un número mayor")
else:
    print("prueba con un número menor")

op3 = int(input())
if(numero_secreto==op3):
    print("que suerte, le achuntaste")
else:
    print("Lo siento, no le achuntaste, el numero era", numero_secreto)



# r1 = 10
# r2 = 20
# print ("Cuánto es",str(r1),"mas",str(r2), "?")
# respuesta = int(input())
#
# if respuesta==r1+r2:
#     print("Correcto!")
# else:
#     print("Incorrecto")

# import random
# print("juguemos un black jack")
# print("vamos a sacar 3 cartas")
# print("para robar una carta ingrese 'r' y luego Enter")
#
# total_jugador = 0
# total_casa = 0
#
# turno1 = input()
# if(turno1=='r' or turno1=='R'):
#     esta_carta = random.randint(1,10)
#     total_jugador += esta_carta
#     print("carta 1:", esta_carta," >> total:", total_jugador )
#
# turno2 = input()
# if(turno2=='r' or turno2=='R'):
#     esta_carta = random.randint(1,10)
#     total_jugador += esta_carta
#     print("carta 2:", esta_carta," >> total:", total_jugador )
#
# turno3 = input()
# if(turno3=='r' or turno3=='R'):
#     esta_carta = random.randint(1,10)
#     total_jugador += esta_carta
#     print("carta 3:", esta_carta," >> total:", total_jugador )
#
# turno4 = input()
# if(turno4=='r' or turno4=='R'):
#     d = random.randint(1, 10)
#     total_casa += d
#     print("la casa saca:", d, " >> total:", total_casa)
#
# turno5 = input()
# if(turno5=='r' or turno5=='R'):
#     d = random.randint(1, 10)
#     total_casa += d
#     print("la casa saca:", d," >> total:", total_casa)
#
# turno6 = input()
# if(turno6=='r' or turno6=='R'):
#     d = random.randint(1, 10)
#     total_casa += d
#     print("la casa saca:", d," >> total:", total_casa)
#
# if (total_jugador>total_casa):
#     print("usted tiene:", total_jugador, " La casa tiene:", total_casa)
#     print("usted gana")
# elif (total_jugador==total_casa):
#     print("usted tiene:", total_jugador, " La casa tiene:", total_casa)
#     print("Usted y la La Casa empatan")
# else:
#     print("usted tiene:", total_jugador, " La casa tiene:", total_casa)
#     print("La Casa gana")





