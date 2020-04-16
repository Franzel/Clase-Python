Algoritmo entrevistaHAL
	pregunta1<-"Hal, crees que Dave tiene planes de eliminarte?"
	Escribir pregunta1
	
	respuesta1<-"si"
	Escribir respuesta1
	
	Segun respuesta1 Hacer
		"si":
			Escribir "Y como te vas a defender?"
			Escribir "Lo voy a eliminar primero"
		"no":
			pregunta3<-"Muy bien, cuantas veces has visto a Dave hablando con Frank hoy?"
			Escribir pregunta3
			
			respuesta3<-2
			Escribir respuesta3
			
			Si respuesta3<=1 Entonces
				Escribir "quizas deberias prestar mas atencion a cuanto hablan..."
			SiNo
				Escribir "y no te parece extrano que hablen tantas veces?"
			Fin Si
			
		De Otro Modo:
			Escribir "Te preguntare nuevamente"
	Fin Segun
FinAlgoritmo

