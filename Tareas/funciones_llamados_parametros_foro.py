#este ejemplo calcula el promedio de una cantidad de numeros arbitraria

#funcion de calculo de promedio, su parametro es una lista
def promedio (listaNums):
    suma = 0
    cantNums = len(listaNums)
    for i in range(cantNums):
        suma += listaNums[i]
    return suma/cantNums

numeros = [] #lista vacia

while True:
    try:
        cant_numeros_total = int(input("Cuántos números quiere ingresar?"))
        break
    except ValueError:
        print("No ingresaste un numero válido")

cant_ingresos = 0 #este nos ayuda a contar cuantos ingresos se han hecho, partimos en 0
while cant_ingresos < cant_numeros_total:
    while True:
        try:
            x = int(input("ingrese un numero: "))
            break
        except ValueError:
            print("No ingresaste un numero válido")

    cant_ingresos += 1
    numeros.append(x) #agregamos el input a nuestra lista

print("el promedio es:", promedio(numeros)) #calculamos e imprimimos el resultado