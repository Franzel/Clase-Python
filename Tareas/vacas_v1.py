#Curso Python UDD 2020
#Francisco Zamorano

def ingresoInfoVaca(id):
    i = id
    while True:
        try:
            p = int(input("Ingrese peso vaca " + str(i) +": "))
            if (p < 0):
                print("Ingreso no valido!")
            else:
                break
        except ValueError:
            print("Ingreso no valido!")
    while True:
        try:
            l = int(input("Lts. leche   :"))
            if (l < 0):
                print("Ingreso no valido!")
            else:
                break
        except ValueError:
            print("Ingreso no valido!")
    e = round(l/p, 3) #eficiencia
    return (i,p,l,e)

def sortList(lista, criterio):
    lista.sort(key=lambda lista:lista[criterio], reverse=True)
    return lista


while True:
    try:
        vacas_total = int(input("Ingrese cantidad de vacas a la venta: "))
        if (vacas_total<0):
            print("Ingreso no valido!")
        else:
            break
    except ValueError:
        print("Ingreso no valido!")
while True:
    try:
        capacidad_camion = int(input("Ingrese peso de carga del su camion: "))
        if (capacidad_camion < 0):
            print("Ingreso no valido!")
        else:
            break
    except ValueError:
        print("Ingreso no valido!")


print("VACAS A LA VENTA:", str(vacas_total))
lista_vacas = []

#Ingresar info de vaca, via funcion. ingresar info entrada a lista por orden de ingreso
for i in range(vacas_total):
    info_esta_vaca = ingresoInfoVaca(i+1)
    # print(info_esta_vaca)
    lista_vacas.append(info_esta_vaca)
# print(lista_vacas) #para debug

#Ordenar lista segun productividad lts/kg
vacas_sorted = sortList(lista_vacas, 3)
# print(vacas_sorted) #para debug

#inicializar variables
carga_utilizada = 0
capacidad_restante = 0
cant_vacas_en_camion = 0
lista_vacas_en_camion = []
productividad = 0

#computar cantidades, agragar vacas a lista, privilegiando priero las mas productivas x kilo de peso
for i in range(len(vacas_sorted)):
    if (carga_utilizada + vacas_sorted[i][1]>capacidad_camion or cant_vacas_en_camion>vacas_total):
        continue
    else:
        carga_utilizada += vacas_sorted[i][1]
        capacidad_restante = capacidad_camion - carga_utilizada
        cant_vacas_en_camion += 1
        productividad += vacas_sorted[i][2]
        lista_vacas_en_camion.append(vacas_sorted[i])

#Imprimir reporte final
print("")
print("--------------")
print("REPORTE FINAL")
print("--------------")
print("LISTA DE VACAS ESCOGIDAS")
print("num\t\tpeso\tlts\t\tlts/kg")
for i in range(len(lista_vacas_en_camion)):
    for j in range(len(lista_vacas_en_camion[i])):
        print(lista_vacas_en_camion[i][j], end="\t\t")
    print("")

print("-------")
print("TRANSPORTE Y PRODUCCION")
print("carga utilizada      :", carga_utilizada, "kg. (", (carga_utilizada/capacidad_camion)*100, "% )")
print("Carga restante       :", capacidad_restante, "kg. (", 100-(carga_utilizada/capacidad_camion)*100, "% )")
print("Cant de vacas        :", str(len(lista_vacas_en_camion)))
print("Total lts leche/dia  :", productividad)




