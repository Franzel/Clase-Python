//FUNCION PARA PROMEDIAR
Funcion prom <- Promedio(nota,cantidad)
	suma <-0 //inicializamos variable suma en 0
	Para i<-1 Hasta cantidad Con Paso 1 Hacer
	suma <- suma + nota[i]
	Fin Para
	
	prom <- suma/cantidad
FinFuncion

//ALGORITMO PRINCIPAL
Algoritmo modulo_subprocesos
	
	nombre <- "Francisco"
	apellido <- "Zamorano"
	carrera <- "Diseno"
	asignatura_1 <- "Python"
	asignatura_2 <- "Cocina"
	asignatura_3 <- "Serigrafia"
	
	Dimension asignaturas[3]
	cant_notas <- 10 //definir cantidad de notas
	
	//Crear las 10 notas aleatoriamente
	Dimension mis_notas[cant_notas]

	
	Para a<-1 Hasta 3 Con Paso 1
		
		Para i<-1 Hasta cant_notas Con Paso 1 Hacer
			mis_notas[i]<-0
			
			mis_notas[i]<- Aleatorio(40,70) / 10
		Fin Para

		mi_promedio <- Promedio(mis_notas,cant_notas)
		
		Escribir nombre + " " + apellido + " - " Sin Saltar
		
		Segun a Hacer
			1:
				Escribir asignatura_1 Sin Saltar
			2:
				Escribir asignatura_2 Sin Saltar
			3:
				Escribir asignatura_3 Sin Saltar
				
		Fin Segun
		
		 Escribir " - " + asignatura + " ( " + ConvertirATexto(mi_promedio) + " ) : " Sin Saltar
		//Escribira las notas
		Para i<-1 Hasta cant_notas Con Paso 1 Hacer
			Escribir ConvertirATexto(mis_notas[i])  Sin Saltar
			Si i<cant_notas Entonces
				Escribir ", " Sin Saltar
			SiNo
				Escribir " "
			Fin Si
		Fin Para	

		
		
	FinPara	
FinAlgoritmo




	