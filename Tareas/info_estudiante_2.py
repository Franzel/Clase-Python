#Curso Python
#Francisco Zamorano 2020

cursos = []
cantCursos = 6
cantNotas = 6

def ingresoInfoAlumno():
    # nombre = "Francisco"
    # apellido = "Zamorano"
    # carrera = "Arte"
    n = input("ingrese su Nombre    :")
    a = input("ingrese su Apellido  :")
    c = input("ingrese su Carrera   :")
    return (n,a,c)

#funcion de calculo de promedio, su parametro es una lista
def promedio(listaNums):
    suma = 0
    cantNums = len(listaNums)
    for i in range(cantNums):
        suma += listaNums[i]
    return round(suma/cantNums, 1)

def sortList(lista):
    lista.sort(key=lambda lista:lista[0])
    return lista

def cursoActivo():
    print(" ")
    print("LISTADO DE SUS CURSOS")
    for i in range(cantCursos):
        print(str(i + 1) + ". " + cursos[i])
    print(" ")
    entrada = input("Seleccione un curso para ingresar sus notas (para salir ingrese 'Q'):")
    if entrada == "Q" or entrada == "q":
        return (entrada)
    while True:
        try:
            cursoSeleccionado = int(entrada)
            while cursoSeleccionado > cantCursos or cursoSeleccionado < 1:
                # print("Seleccion no válida, intente de nuevo:")
                cursoSeleccionado = int(input("Seleccion no válida, intente de nuevo: "))
            else:
                return (cursoSeleccionado)
            break
        except ValueError:
            print("Seleccion no válida, ", end="")
            break

def ingresoNotas(index_curso):
    index_curso -= 1
    print("")
    print("-------- Curso", cursos[index_curso].upper(), "--------", "(ingrese 'Q' para salir)" )
    if len(todasLasNotas[index_curso])>0:
        print("Ya ha ingresado " + str(len(todasLasNotas[index_curso])) + "/"+str(cantNotas) + " notas:", todasLasNotas[index_curso])

    notasEsteCurso = [] #creamos una lista vacia para recibir las notas

    while len(todasLasNotas[index_curso])<cantNotas:
        entrada = input("   ingrese nota: ")
        if entrada == "Q" or entrada == "q":
            break
        while True:
            try:
                nota = float(entrada)
                if nota<1 or nota>7:
                    print("nota no válida")
                    break
                notasEsteCurso.append(nota)
                todasLasNotas[index_curso].append(nota)
                break
            except ValueError:
                print("ingreso no válido!")
                break

def imprimirInfoCurso(index_curso):
    index_curso -= 1
    print("---")
    print("CARRERA  :", datosAlumno[2])
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

#------------------- PRINCIPAL ---------------------------
#---------------------------------------------------------

#Crear un repositorio vacio que guardara todas las notas de todos los cursos
todasLasNotas = []
todosLosPromedios = []
todosLosEstados = []
for i in range(cantCursos):
    todasLasNotas.append([])
    todosLosPromedios.append(0)
    todosLosEstados.append(False)

#ingresar info alumno
datosAlumno = ingresoInfoAlumno()

#Ingresar Cursos
for i in range(cantCursos):
    cursos.append(input("ingrese curso " + str(i+1) + ": ")) #Rellenado via input
    # cursos.append("CursoTest " + str(i+1)) #Rellenado auto para debug

#Ingreso de notas hasta que todos los cursos hayan ingresado todas las notas
while not all(todosLosEstados):
    seleccion = cursoActivo()
    while True:
        try:
            ingresoNotas(seleccion)
            for i in range(len(todasLasNotas)):
                if len(todasLasNotas[i]) == cantNotas: #se ingresaron todas las notas de este curso?
                    todosLosEstados[i] = True
            imprimirInfoCurso(seleccion) #imprimir reporte de cada curso individual
            break
        except TypeError:
            if seleccion==None:
                seleccion = cursoActivo()# si hay entrada no valida
            if seleccion=="q":
                ingresoInfoAlumno() #volver a ingresar
            break

#Ordenar los cursos. Guradamos cada curso en una lista, y cada lista en una lista mayor
infoCursos = []
for i in range(len(cursos)):
    esteCurso = []
    esteCurso.append(cursos[i])
    esteCurso.append(todasLasNotas[i])
    esteCurso.append(promedio(todasLasNotas[i]))
    # print(esteCurso)
    infoCursos.append(esteCurso)

infoCursosOrdenados = sortList(infoCursos) #ordenar segun el primer item de las listas (nombre curso)

#Calcular promedio general
for i in range(len(todasLasNotas)):
    todosLosPromedios[i] = promedio(todasLasNotas[i])
promedioGeneral = round(promedio(todosLosPromedios),1)

#Imprimir la informacion final
print("")
print("------------------------------------------")
print("REPORTE FINAL")
print("------------------------------------------")

print("NOMBRE ALUMNO    :", datosAlumno[0], datosAlumno[1])
print("CARRERA          :", datosAlumno[2])
print("PROMEDIO GENERAL :", promedioGeneral)
print("")

for i in range(len(infoCursosOrdenados)):
    print("---")
    print("CURSO            :", infoCursosOrdenados[i][0]) #nombre
    print("Notas            : ", end="")

    for j in range (len(infoCursosOrdenados[i][1])): #notas
        if j>0:
            print(",", end=" ")
        print(infoCursosOrdenados[i][1][j], end="")
    print("")
    print("Promedio Curso   :",round(infoCursosOrdenados[i][2],1)) #promedio

