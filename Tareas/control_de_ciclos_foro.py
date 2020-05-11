#Este ejemplo es un pseudo Black Jack
#El jugador puede sacar cuantas cartas quiera, mientras sumen menos de 21
#La Casa sacará solo 3 cartas


import random
total_jugador=0
total_casa=0
casa_gana = False

print("Instrucciones: presione ENTER para sacar carta, y 'n' para pasar")

while(input()!='p'):
    esta_carta = random.randint(1,10)
    total_jugador += esta_carta
    if(total_jugador<22):
        print("Esta carta:", esta_carta, ", total:", total_jugador)
    else:
        print("Esta carta:", esta_carta, ", total:", total_jugador)
        print("Se pasó de 21, La casa gana")
        casa_gana=True
        print("Gracias por jugar")

if(casa_gana==False):
    print("ok, turno de la casa. Vemos la carta?")

    for x in range(3):
        input()
        esta_carta = random.randint(1,10)
        total_casa += esta_carta
        print("Esta carta:", esta_carta, ", total:", total_casa)
        if(total_casa>22):
            print("Usted tiene", total_jugador, ". La casa tiene", total_casa)
            print("Usted gana")
    print(" ")
    print("Usted tiene", total_jugador, ". La casa tiene", total_casa)

    if(total_jugador>total_casa):
        print("Usted gana!!!")
    else:
        print("La casa gana!!!")
