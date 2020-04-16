Algoritmo modulo_expresiones
	
	// Esta clase introdujo PSeInt, su interfaz y funcionalidades
	// Se introducen el uso de condicionales, y la condicional SI-NO en particular
	// Abajo un ejemplo de como funciona
	
	Escribir "Bienvenido al juego"
	Escribir "Usted necesita al menos 4 puntos para ganar un premio"
	Escribir "Presione enter para tirar el dado" Sin Saltar
	
	Leer tiro //guardamos el input del teclado en esta variable
	
	Mientras tiro <> "" Hacer //Esto es para asegurar que se apreto ENTER y no otra tecla
		//Mientras el input de ENTER sea falso, pedir el input 
		Escribir "use ENTER para tirar el dado, intente otra vez: " Sin Saltar
		Leer tiro
	Fin Mientras
	
	puntos<-puntos + Aleatorio(1, 6) //esto genera un numero aleatorio entre 1 y 6 y asigna ese valor a variable puntos
	Escribir "------"
	Escribir "Su dado cayo en :" Sin Saltar 
	Escribir puntos //Escribir el resultado 
	
	Si puntos>4 Entonces //si es mayor a 4
		Escribir "GANADOR!!!!! Puede retirar su premio" //escribe mensaje de ganador
	SiNo
		Escribir "LO SIENTO, NO GANA NADA ESTA VEZ" //escribe mensaje de perdedor
	Fin Si
		
FinAlgoritmo
