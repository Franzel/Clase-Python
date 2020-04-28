'''
# WHILE
condicion = 1
while condicion<10:
    condicion += 1
    if condicion == 5:
        print("continue")
        continue
    print("estamos dentro de la condicion")
print("fin de progama")
'''

'''
# FOR
lista = [100,200,300,400,500,600,700,800,900]
i=0
for x in lista:
    i+=1
    print(i, ">>>")
    if(x>300):
        print(x," BREAK")
        break
    print(x)
'''
'''
for i in "lista":
    print(i)
'''

colores = ["rojo", "blnco", "cafe", "azul", "negro"]
colores.append("amarillo")
for i in colores:
    print(len(colores), i)
    #esto elimina de la lista a "cafe", reduciendo la lista
    if(i=="cafe"):
        colores.remove(i)
        print(i, "eliminado!")
        colores.append("Nuevo Color de reemplazo")


