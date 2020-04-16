Algoritmo sin_titulo
	varPregunta1<-"¿Hal, crees que Dave antes tiene planes de eliminarte?"
	varRespuesta1<-"Si"
	varPregunta2<-"No"
	Segun variable_numerica Hacer
		opcion_1:varPregunta2<-"Y como te vas a defender?"
			Leer varPregunta2
		opcion_2:varPregunta2<-"Quizas deberias prestar mas atencion a lo que habla con Frank"
			Leer varPregunta2
		De Otro Modo:
			varPregunta2<-"Te preguntare nuevamente"
			Leer varPregunta2
	Fin Segun
FinAlgoritmo