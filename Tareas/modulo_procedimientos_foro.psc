Algoritmo modulo_procedimientos
	
	Escribir "MODULO PROCEDIMIENTOS"
	Escribir "En este modulo cubrimos tres maneras de realizar procesos."
	Escribir "Estos procesos los podemos repetir una cierta cantidad de veces segun alguna condicion que definamos."
	Escribir "---------------------"
	
	Escribir "En el codigo de abajo definimos que hay tres opciones donde escoger:"
	Escribir "1. MIENTRAS / 2. REPETIER / 3.PARA"
	Escribir " "
	opciones_total<- 3
	
	Escribir "Para seleccionar, creamos una variable que nos permite elegir segun el numero que anotemos"
	Escribir "Se mostrara la informacion segun la seleccion, junto a un ejemplo"
	seleccion <- 3
	
	Escribir " "
	Escribir "Partamos..."
	cantidad_veces<- 6
	texto_cantidad_veces <- ConvertirATexto(cantidad_veces_a_escribir)
	timer <- 0
	

	Segun seleccion Hacer
		1:
			Escribir "-------------------------- "	
			Escribir "Usted ha seleccionado la opcion: " + ConvertirATexto(seleccion) + ".MIENTRAS"
			Escribir "Esta proceso se ejecuta mientras una condicion sea verdadera"
			Escribir "--"
			Escribir "Vamos a escribir HOLA " + texto_cantidad_veces " veces" + ", porque la variable cantidad_veces es: " + texto_cantidad_veces
			Escribir "--"
			Escribir "Partimos con un timer en 0"
			Escribir "Empezamos el Proceso:"
			Escribir "1. Si el timer es menor a " , + texto_cantidad_veces + ", escribir HOLA (ej. 0 es menor a " + texto_cantidad_veces + " , entonces escribe HOLA)"
			Escribir "2. Le sumamos 1 al timer, asi va creciendo vuelta a vuelta"
			Escribir "3. Cuando el timer llegue a 10, ya no es menor que 10. Entonces podemos decir que la condicion es falsa"
			Escribir "4. Si la condicion es falsa, entonces salimos del Proceso y seguimos leyendo linea a linea para abajo"
			Escribir "--"
			
			Mientras timer<cantidad_veces Hacer 
				Escribir ConvertirATexto(timer) + ". HOLA"
				timer<- timer+1
			Fin Mientras
			
		2:
			Escribir "-------------------------- "	
			Escribir "Usted ha seleccionado la opcion: " + ConvertirATexto(seleccion) + ".REPETIR"
			Escribir "Esta proceso se ejecuta hasta que una condicion deje de ser falsa"
			Escribir "--"
			Escribir "Partimos con un timer en 0"
			Escribir "Empezamos el Proceso:"
			
			Repetir
				Escribir ConvertirATexto(timer) + ". HOLA"
				timer<- timer+1
			Hasta Que timer>=10
			
		3:
			Escribir "-------------------------- "	
			Escribir "Usted ha seleccionado la opcion: " + ConvertirATexto(seleccion) + ".REPETIR"
			Escribir "Esta proceso se repite una cantidad de veces que determinada"
			Escribir "--"
			Escribir "Partimos con un timer en 0"
			Escribir "Empezamos el Proceso:"
			Para timer<-0 Hasta cantidad_veces-1 Con Paso 1 Hacer
				Escribir ConvertirATexto(timer) + ". HOLA"
			Fin Para
			
			
		De Otro Modo:
			Escribir "Por favor seleccione una opcion para escribir:"
	Fin Segun

	Escribir "--"
	Escribir "Acabamos de escribir HOLA " + ConvertirATexto(cantidad_veces) + " veces"
	
FinAlgoritmo


