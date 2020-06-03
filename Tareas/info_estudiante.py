#https://pynative.com/python-check-user-input-is-number-or-string

identidad = []
cursos = []
cantCursos = 2
cantNotas = 3

nombre = "Francisco"
apellido = "Zamorano"
carrera = "Arte"

#funcion de calculo de promedio, su parametro es una lista
def promedio (listaNums):
    suma = 0
    cantNums = len(listaNums)
    for i in range(cantNums):
        suma += listaNums[i]
    return round(suma/cantNums, 2)

def cursoActivo():
    # Imprimir listado de cursos ingresados
    print("LISTADO DE SUS CURSOS")
    for i in range(cantCursos):
        print(str(i + 1) + ". " + cursos[i])
    print("seleccione un curso para ingresar sus notas")
    cursoSeleccionado = int(input())
    # print(cursos[cursoSeleccionado - 1])
    return (cursos[cursoSeleccionado - 1], cursoSeleccionado-1)

for i in range(cantCursos):
    cursos.append(input("ingrese curso " + str(i+1) + ": "))
# print(cursos)

#Crear un repositorio vacio que guardara todas las notas
todasLasNotas = [] #guarda todas las notas ingresadas, en un tuple
todosLosPromedios = []
for i in range(cantCursos):
    todasLasNotas.append([])
    todosLosPromedios.append(0)

for i in range(cantCursos): #esto debe ser un while
    cursoSeleccionado = cursoActivo()
    notasEsteCurso = []
    for j in range(cantNotas):
        print("Curso", cursoSeleccionado[0], "- ingrese nota")
        entrada = input()
        nota = float(entrada)
        notasEsteCurso.append(nota)
    todosLosPromedios
    print("---")
    print("CARRERA:", carrera)
    print("CURSO:", cursoSeleccionado[0])
    print("notas de este curso", notasEsteCurso)
    print("PROMEDIO: ", promedio(notasEsteCurso))
    print("---")
    todasLasNotas[cursoSeleccionado[1]]=notasEsteCurso
    # print(todasLasNotas)


for i in range(len(todasLasNotas)):
    todosLosPromedios[i] = promedio(todasLasNotas[i])
# print("TODOS:", todosLosPromedios)
promedioGeneral = round(promedio(todosLosPromedios),1)


print("------------------------------------------")
print("REPORTE FINAL")
print("------------------------------------------")

print("NOMBRE ALUMNO    :", nombre, apellido)
print("CARRERA          :", carrera)
print("PROMEDIO GENERAL :", promedioGeneral)
print("")
for i in range(len(cursos)):
    print("---")
    print("CURSO            :", cursos[i])
    print("Notas Curso      :",end=" ")
    for j in range (len(todasLasNotas[i])):
        if j>0:
            print(",", end=" ")
        print(todasLasNotas[i][j], end="")
    print(" ")
    print("Promedio Curso   :", promedio(todasLasNotas[i]))