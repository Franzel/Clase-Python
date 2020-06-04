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

#funcion para determinar curso seleccionado (activo)
def cursoActivo():
    # Imprimir listado de cursos ingresados
    print("LISTADO DE SUS CURSOS")
    for i in range(cantCursos):
        print(str(i + 1) + ". " + cursos[i])
    while True:
        try:
            cursoSeleccionado = int(input("seleccione un curso para ingresar sus notas: "))
            while cursoSeleccionado > cantCursos or cursoSeleccionado < 1:
                # print("Seleccion no válida, intente de nuevo:")
                cursoSeleccionado = int(input("Seleccion no válida, intente de nuevo: "))
            else:
                break
        except ValueError:
            print("Seleccion no válida, ", end="")
            continue
    # print(cursos[cursoSeleccionado - 1])
    return (cursos[cursoSeleccionado - 1], cursoSeleccionado-1)

#Ingresar los nombres de los cursos
for i in range(cantCursos):
    #cursos.append(input("ingrese curso " + str(i+1) + ": "))
    cursos.append("CursoTest" + str(i))

#Crear un repositorio vacio que guardara todas las notas de todos los cursos
todasLasNotas = []
todosLosPromedios = []
for i in range(cantCursos):
    todasLasNotas.append([])
    todosLosPromedios.append(0)

#ingreso notas curso
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

# WIP: verificar si hay cursos sin ingresos
for i in todasLasNotas:
    print("cant de notas por curso", len(i))
    if len(i)==0:
        print("CURSO SIN NOTAS")
        cursoActivo()



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