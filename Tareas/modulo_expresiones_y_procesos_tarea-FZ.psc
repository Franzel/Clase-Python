Algoritmo imprimir_impares
	numero_entrada<-30
	Escribir "numero_de_entrada = " + ConvertirATexto(numero_entrada)
	Escribir " "
	numero_inicial<-0
	
	Escribir "Para numeros PAR, asignar 0. Para numeros IMPARES, asignar 1"
	par_o_impar = 1
	
	Para numero_inicial<-0 Hasta numero_entrada Con Paso 1 Hacer
		Si numero_incial MOD 2 = par_o_impar  O numero_incial = 0 Entonces
			Escribir numero_incial
		Fin Si
		
		numero_incial<-numero_inicial+1
		
	Fin Para
FinAlgoritmo
