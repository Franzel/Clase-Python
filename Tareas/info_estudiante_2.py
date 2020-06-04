#https://pynative.com/python-check-user-input-is-number-or-string

identidad = []
cursos = []
cantCursos = 4
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

def ingresoNotas(index_curso):
    index_curso -= 1
    print("")
    print("Ha seleccionado el curso", cursos[index_curso])
    notasEsteCurso = [] #creamos una lista vacia para recibir las notas
    for j in range(cantNotas):
        # print("Curso", cursos[index_curso], "- ingrese nota")
        entrada = input("  ingrese nota: ")
        nota = float(entrada)
        notasEsteCurso.append(nota)
    todasLasNotas[index_curso] = notasEsteCurso
    # print(todasLasNotas) #imprimir lista final - Solo Debug

def imprimirInfoCurso(index_curso):
    index_curso -= 1
    print("---")
    print("CARRERA  :", carrera)
    print("CURSO    :", cursos[index_curso])
    print("NOTAS    :", end=" ")
    for i in range(len(todasLasNotas[index_curso])):
        if i<len(todasLasNotas[index_curso])-1:
            print(todasLasNotas[index_curso][i], end=", ")
        else:
            print(todasLasNotas[index_curso][i])
    print("PROMEDIO :",promedio(todasLasNotas[index_curso]))
    print("-")
    print("")


#Crear un repositorio vacio que guardara todas las notas de todos los cursos
todasLasNotas = []
todosLosPromedios = []
todosLosEstados = []
for i in range(cantCursos):
    todasLasNotas.append([])
    todosLosPromedios.append(0)
    todosLosEstados.append(False)

#Ingresar los nombres de los cursos
for i in range(cantCursos):
    #cursos.append(input("ingrese curso " + str(i+1) + ": ")) #Rellenado via input
    cursos.append("CursoTest " + str(i)) #Rellenado auto para debug
# Imprimir listado de cursos ingresados
print("LISTADO DE SUS CURSOS")
for i in range(cantCursos):
    print(str(i + 1) + ". " + cursos[i])

def cursoActivo():
    while True:
        try:
            cursoSeleccionado = int(input("Seleccione un curso para ingresar sus notas: "))
            while cursoSeleccionado > cantCursos or cursoSeleccionado < 1:
                # print("Seleccion no válida, intente de nuevo:")
                cursoSeleccionado = int(input("Seleccion no válida, intente de nuevo: "))
            else:
                break
        except ValueError:
            print("Seleccion no válida, ", end="")
            continue
    return (cursoSeleccionado)



#solicitar ingreso de notas hasta que todos los cursos hayan ingresado todas las notas
while not all(todosLosEstados):
    seleccion = cursoActivo()
    ingresoNotas(seleccion)
    imprimirInfoCurso(seleccion)
    for i in range(len(todasLasNotas)):
        if len(todasLasNotas[i]) == cantNotas:
            todosLosEstados[i] = True


#Calcular promedio general y generar reporte final
for i in range(len(todasLasNotas)):
    todosLosPromedios[i] = promedio(todasLasNotas[i])
promedioGeneral = round(promedio(todosLosPromedios),1)

print("")
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
