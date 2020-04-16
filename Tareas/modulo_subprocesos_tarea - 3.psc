Algoritmo modulo_subprocesos
	//--- Nombre y Apellido
	Escribir "Escriba su nombre"
	Leer nombre
	Escribir "Escriba su apellido"
	Leer apellido
	
	//--- Cursos
	Escribir "Cuantos cursos quiere ingresar?"
	Leer cant_cursos
	Dimension asignaturas[cant_cursos] //Tres asignaturas
	Para i<-1 Hasta cant_cursos Con Paso 1 Hacer //Recoger los nombres de los tres cursos
		Escribir "Nombre Curso " + ConvertirATexto(i) Sin Saltar
		Leer asignaturas[i]
	FinPara
	

	//--- Cantidad de notas
	Escribir "Cuantas calificaciones quiere ingresar?"
	Leer cant_notas //definir cantidad de notas
	Dimension mis_notas[cant_cursos,cant_notas]
	
	Para i<-1 Hasta cant_cursos Con Paso 1 Hacer
		Escribir " "
		Escribir "Ingrese notas para Curso " + ConvertirATexto(i) + ": " +  asignaturas[i]
		Para j<-1 Hasta cant_notas Con Paso 1 Hacer
			Escribir "Nota " + ConvertirATexto(j) Sin Saltar
			Leer mis_notas[i,j]
		Fin Para
	Fin Para
	
	//--- Generar un reporte
	Escribir "****************************"
	Escribir "******** MI REPORTE ********"
	Escribir "****************************"
	Escribir "NOMBRE ALUMNO: " + nombre
	Escribir "---"
	Para i<-1 Hasta cant_cursos Con Paso 1 Hacer
		Escribir "CURSO " + ConvertirATexto(i) + ": " + asignaturas[i]
		Escribir "Notas: " Sin Saltar
		Para j<-1 Hasta cant_notas Con Paso 1 Hacer
			Escribir ConvertirATexto(mis_notas[i,j]) Sin Saltar
			suma<-suma + mis_notas[i,j]
			Si j<cant_notas Entonces
				Escribir ", " Sin Saltar
			SiNo
				Escribir " "
				promedio_este_curso <- suma/cant_notas
				Escribir "Promedio: " + ConvertirATexto(promedio_este_curso)
				Escribir"-"
				suma<-0
			Fin Si
		Fin Para
	Fin Para
	
FinAlgoritmo




