import numpy as np #PARA TRABAJAR CON LOS ARRAYS DE NUMPY
from funciones_flota import barco, choice_opcion  #IMPORTO LAS FUNCIONES CREADAS EN EL ARCHIVO FUNCIONES FLOTA
import time #ESTA LIBRERÍA ME DEJARÁ ESTABLECER TIEMPOS DE EJECUCIÓN ENTRE DIFERENTES PARTES DEL JUEGO
import os   #ESTA LIBRERÍA ME PERMITIRÁ BORRAR TEXTO DE LA TERMINAL EN FUNCIÓN DE MIS NECESIDADES

class Barco:

	#CLASE BARCO PARA CREAR LOS BARCOS DE LOS JUGADORES

	def __init__(self,posicion,veces_dañado = 0, operatividad = True):

		self.posicion = posicion #RECIBIRA LA POSICIÓN, ES DECIR, UNA DE LAS OPCIONES ELEGIDAS DE LA FUNCIÓN CHOICE_OPCION
		self.veces_dañado = veces_dañado #OTRO DE SUS ATRIBUTOS QUE SE INICIALIZARÁ EN 0, YA QUE AL EMPEZAR AUN NO HABRÁN SIDO ATACADOS
		self.operatividad = operatividad #EL ATRIBUTO DE OPERATIVIDAD SE INICIALIZARÁ EN TRUE PORQUE AL EMPEZAR EL JUEGO TODOS LOS BARCOS ESTÁN OPERATIVOS


	def mostrar_barco(self):

		#MÉTODO QUE MOSTRARÁ EL ESTADO DEL BARCO. ES DECIR, LAS VECES QUE HA SIDO DAÑADO Y SI SIGUE OPERATIVO O NO. SI EL BARCO ESTÁ OPERATIVO
		#DIRA LÁS VECES QUE A SIDO DAÑADO Y QUE SIGUE CON VIDA, Y SI NO, QUE SE HABRÁ DAÑADO LÓGICAMENTE 3 VECES QUE SON EL NÚMERO DE POSICIONES QUE
		#TIENE EL BARCO Y QUE ADEMÁS ESTÁ HUNDIDO

		if self.operatividad:
			print(f"VECES DAÑADO --> {self.veces_dañado} | ESTADO --> VIVO")
		else:
			print(f"VECES DAÑADO --> {self.veces_dañado} | ESTADO --> HUNDIDO")




	
class Tablero:

	#CLASE TABLERO QUE CONTENDRÁ EL MARCO DEL JUGADOR Y SUS BARCOS

	def __init__(self,marco, barcos= []):

		self.marco = marco #RECIBE MARCO DE 5X5 COMPUESTO DE 0's QUE SERÁN LAS PARTES DE AGUA, TRES 1'S QUE SERÁN DE UN BARCO, Y TRES 2'S QUE SERÁN DE OTROS
		self.barcos = barcos #UNA LISTA QUE RECIBIRÁ LOS BARCOS OBJETO CREADOS DE LOS JUGADORES CON SUS RESPECTIVOS ESTADOS


	def mostrar_tablero(self):

		#MÉTODO PARA MOSTRAR EL TABLERO DEL RESPECTIVO JUGADOR

		print(self.marco)

	def mostrar_barcos(self):

		#MÉTODO QUE RECORRERA LA LISTA DE BARCOS QUE TIENE EL TABLERO Y LOS MOSTRARÁ TODOS

		for i in self.barcos:

			i.mostrar_barco()
			print(" ")
 

class Juego:

	#ESTA CLASE CONTENDRÁ LOS MARCOS DE LOS JUGADORES, QUE A SU VEZ ESTOS YA CONTIENEN TODOS LOS BARCOS

	#ESTOS ARRAYS LUEGO SERVIRÁN PARA QUE EL JUGADOR PUEDA VER LO QUE LLEVA DE DAÑO HACIA SU RIVAL 

	quedan_contrario1 = np.zeros((5,5))
	quedan_contrario2 = np.zeros((5,5))

	#TÍTULO Y DESCRIPCIÓN DEL JUEGO

	print("\n\t\t\t\tBienvenido al juego de ¡HUNDIR LA FLOTA!\n")

	print("""
El juego empieza con un tablero por jugador con dos barcos de tres filas consecutivas.\n
A lo largo de cada ronda aparecerá el marco de tu rival con las posiciones que le hayas tocado representadas 
por el número 3. También aparecerá tu tablero donde aparecerán tus barcos, representados por el 1 y por el 2, 
donde a medida que sean tocados se iran representando con el 3.\n
En cada ronda se le pregunta a un jugador por una posición.
Si el jugador da con una posición donde se encuentre alguno de los barcos del rival contrario,
se mostrará un mensaje avisando de que le ha tocado.\n
Si le toca tres veces significará que el barco está hundido.\n
Gana el primero que consiga hundir los dos barcos del enemigo.\n 
**Aviso**: Aunque el jugador toque un barco, el turno será para el otro jugador. No se puede repetir turno.
**Aviso**: Tampoco habrá movimientos en diagonal. Solo vertical e horizontal
**Aviso**: Si se responden mal a las preguntas se perderá turno.""")
	


	def __init__(self,marcos = []):

		#MÉTODO CONSTRUCTOR QUE SE INICIALIZA EN UNA LISTA DONDE SE IRÁN AÑADIENDO LOS TABLEROS DE CADA JUGADOR

		self.marcos = marcos


	def inicializar_barcos(self):

		#ESTE MÉTODO SE ENCARGA DE QUE, AL SER LLAMADO, SE POSICIONEN ALEATORIAMENTE LOS BARCOS EN EL TABLERO DE CADA JUGADOR

		marco = np.zeros((5,5)) #INICIALIZO EL MARCO DEL JUGADOR EN TODO 0's
		
		barcos_jugador = []	#LISTA DONDE IRÉ AÑADIENDO LAS POSICIONES O OPCIONES QUE SACA LA FUNCIÓN CHOICE OPCION	


		while True:
		
			for i in range(2):
				barco_aleatorio = choice_opcion() #SACO LA OPCIÓN/POSICIÓN ALEATORIA
				
				barcos_jugador.append(barco_aleatorio) #LA AÑADO A LA LISTA

				barco(barco_aleatorio, marco,i+1) #ESTA FUNCÍON ES LA POSICIONA LOS BARCOS EN EL TABLERO INICIALIZADO ARRIBA COMPONIENDOSE LOS BARCOS DE 1's y 2's

			if np.sum(marco) == 9: #SI LA SUMA DE LOS NÚMEROS 1 Y 2 QUE TIENEN LOS DOS BARCOS SUMAN 9, QUERRÁ DECIR QUE NO SE HAN SOLAPADO EN CUANTO A POSICIÓN SE REFIERE 
				break
		
			else:
				#EN CASO DE SOLAPARSE LOS BARCOS, VUELVO A INICIALIZAR EL MARCO Y LIMPIO LA LISTA DE POSICIONES PARA EMPEZAR DE NUEVO
				marco = np.zeros((5,5))
				barcos_jugador.clear()

		return marco, barcos_jugador #FINALMENTE RETORNO EL MARCO Y LAS POSICIONES. ÉSTAS ÚLTIMAS  PARA CREAR LOS OBJETOS DE LA CLASE BARCO


	def añadir_tablero(self, tablero):

		#MÉTODO QUE ME SERVIRÁ PARA AÑADIR LOS TABLEROS A LA CLASE JUEGO 

		self.marcos.append(tablero)

	def mostrar_tableros(self):

		#METODO QUE RECORRERÁ LA LISTA DE TABLEROS DEL JUEGO Y LOS MOSTRARÁ

		for i in self.marcos:
			i.mostrar_tablero()

	def preguntar_posicion_a_j1(self):

		#MÉTODO QUE PREGUNTARÁ POR LA POSICIÓN DE LOS BARCOS DEL RIVAL, EL JUGADOR 2

		print("\n¡Adivina posicion de tu contrario! \n")

		try:
			
			fila = int(input("Diga una fila del 0 al 4: ")) #LE PEDIRÁ EL NÚMERO DE UNA FILA
			columna = int(input("Diga una columna del 0 al 4: ")) #LE PEDIRÁ EL NÚMERO DE UNA COLUMNA



			if self.marcos[1].marco[fila,columna] == 1: #SI COINDICEN FILA Y COLUMNA CON UN 1 EN EL MARCO DEL RIVAL...
					
				self.marcos[1].marco[fila,columna] = 3 #AL MARCO DEL RIVAL LE PONDRÉMOS UN 3 EN ESA POSICIÓN PARA QUE VEA QUE POSICIÓN TIENE TOCADA
				self.marcos[1].barcos[0].veces_dañado += 1 #LE SUMAREMOS 1 A LOS DAÑOS DE ESE BARCO NÚMERO 1

				Juego.quedan_contrario2[fila,columna] = 3 #A SU VEZ EN ESTE MARCO TAMBIÉN LE PONEMOS UN 3 EN ESA POSICIÓN QUE HA ACERTADO PARA QUE VEA LAS TOCADAS QUE LLEVA DEL CONTRARIO

				if self.marcos[1].barcos[0].veces_dañado == 3: #SI EL BARCO 1 HA SIDO DAÑADO 3 VECES IMPRIMIREMOS UN MENSAJE DE TOCADO Y HUNDIDO
					print("\n¡TOCADO Y HUNDIDO!\n")
					
				else:
					print("\n¡TOCADO!\n") #SI NO A SIDO DAÑADO 3 VECES SOLO SE PONDRÁ TOCADO
					

				
			#LO MISMO PARA EL BARCO NÚMERO 2

			elif self.marcos[1].marco[fila,columna] == 2:
					
				self.marcos[1].marco[fila,columna] = 3
				self.marcos[1].barcos[1].veces_dañado += 1

				Juego.quedan_contrario2[fila,columna] = 3

				if self.marcos[1].barcos[1].veces_dañado == 3:
					print("\n¡TOCADO Y HUNDIDO!\n")
					
				else:
					print("\n¡TOCADO!\n")
					


			elif Juego.quedan_contrario2[fila,columna] == 3: #ESTA CONDICIÓN DICE QUE SI REPITE EN UNA CASILLA QUE YA HA DADO, LE AVISARÁ PERDIENDO EL TURNO
				print("\nYa habías dado a esa posición. Pierdes turno.\n")

			else:
				print("\n¡AGUA!\n") #EN CASO DE NO DARLE A ALGUNO DE LOS BARCOS, AVISAR QUE HA DADO AL AGUA

		except ValueError:
			print("\n¿Y si metemos numeros que tal?. Pierdes tu turno.\n") #MANEJO DE ERRORES SI METE ALGO QUE NO SEA UN NÚMERO
			

		except IndexError:
			print("\n¡Numeros del 0 al 4 inclusives!!. Pierdes turno.") #MANEJO DE ERRORES SI METE NUMEROS FUERA DEL RANGO DEL MARCO
			

			
	#MISMO MÉTODO PERO CON PREGUNTAS AL JUGADOR 2

	def preguntar_posicion_a_j2(self):

		

		print("\n¡Adivina posicion de tu contrario! \n")
		
		try:
			
			fila = int(input("Diga una fila del 0 al 4: "))
			columna = int(input("Diga una columna del 0 al 4: "))


	
			if self.marcos[0].marco[fila,columna] == 1:
							
				self.marcos[0].marco[fila,columna] = 3
				self.marcos[0].barcos[0].veces_dañado += 1

				Juego.quedan_contrario1[fila,columna] = 3

				if self.marcos[0].barcos[0].veces_dañado == 3:
					print("\n¡TOCADO Y HUNDIDO!\n")
					
				else:
					print("\n¡TOCADO!\n")
					


			elif self.marcos[0].marco[fila,columna] == 2:

				self.marcos[0].marco[fila,columna] = 3
				self.marcos[0].barcos[1].veces_dañado += 1

				Juego.quedan_contrario1[fila,columna] = 3

				if self.marcos[0].barcos[1].veces_dañado == 3:
					print("\n¡TOCADO Y HUNDIDO!\n")
					
				else:
					print("\n¡TOCADO!\n")
			
				

			elif Juego.quedan_contrario1[fila,columna] == 3:
				print("\nYa habías dado a esa posición. Pierdes turno.\n")

			else:
				print("\n¡AGUA!\n")


		except ValueError:
			print("\n¿Y si metemos numeros que tal?. Pierdes tu turno.\n")
			

		except IndexError:
			print("\n¡Numeros del 0 al 4 inclusives!!. Pierdes turno.")
			
	

	def estado_barcos_j1(self):

		#METODO QUE COMPROBARÁ LOS ESTADOS DE LOS BARCOS DEL RIVAL EN CADA RONDA Y LOS MOSTRARÁ. SI SE COMPRUEBA QUE UNO DE LOS BARCOS HA SIDO DAÑADO TRES VECES
		#LA OPERATIVIDAD SERÁ IGUAL A FALSE

		print("\n*** BARCOS DEL RIVAL ***\n")

		for i, bar in enumerate(self.marcos[0].barcos):
			if bar.veces_dañado == 3:
				time.sleep(1) #UN SEGUNDO DE ESPERA PARA LAS SIGUIENTES LINEAS DE CODIGO
				bar.operatividad = False
				bar.mostrar_barco()
				
			else:
				print(f"\nBarco {i+1}\n")
				bar.mostrar_barco()

	#MISMO MÉTODO DE ANTES PERO CON EL OTRO RIVAL

	def estado_barcos_j2(self):
		print("\n*** BARCOS DEL RIVAL ***\n")

		for i,bar in enumerate(self.marcos[1].barcos):
			if bar.veces_dañado == 3:
				time.sleep(1)
				bar.operatividad = False
				bar.mostrar_barco()
				
			else:
				print(f"\nBarco {i+1}\n")
				bar.mostrar_barco()

	def estado_tablero_j1(self):

		#MÉTODO QUE COMPROBARA EL ESTADO DEL TABLERO RIVAL. DERRIBAR TODOS LOS BARCOS IMPLICA QUE LA SUMA DEL MARCO SERA DE 18. (3+3+3) + (3+3+3)
		#IMPLICARÁ QUE EL JUGADOR HA GANADO Y RETORNARÁ UNA CADENA DE TEXTO QUE SE USARÁ PARA FINALIZAR EL JUEGO

		if np.sum(self.marcos[0].marco)== 18:
			
			print("\n\n\n\t\t\t¡¡FELICIDADES!! ¡¡TODOS LOS BARCOS HUNDIDOS!!!! ¡¡GANASTE!!\n")
			return "¡GANASTE!"
	
	def estado_tablero_j2(self):

		#MISMO MÉTODO QUE ANTES PERO PARA EL OTRO JUGADOR

		if np.sum(self.marcos[1].marco) == 18:
			
			print("\n\n\n\t\t\t¡¡FELICIDADES!! ¡¡TODOS LOS BARCOS HUNDIDOS!!!! ¡¡GANASTE!!\n")
			return "¡GANASTE!"

	def repetir(self):
		
		#MÉTODO QUE SERVIRÁ PARA REPETIR EL JUEGO. SI SE REPITE, HAY QUE INICIALIZAR LOS MARCOS DONDE EL JUGADOR VE LO QUE LE QUEDA PARA HUNDIR AL RIVAL
		#TAMBIÉN SE LIMPIARÁ LA LISTA QUE CONTIENE LOS MARCOS DE LOS JUGADORES PARA PODER EMPEZAR DE CERO Y QUE NO HAYA PROBLEMAS. SI DICE QUE NO, TERMINARÁ EL BUCLE DEL JUEGO.

		repetir = True
		
		while repetir:
			repetir = input("Queréis repetir: S/N: ")

			if repetir.lower() == "s":
				self.marcos.clear()
				Juego.quedan_contrario1 = np.zeros((5,5))
				Juego.quedan_contrario2 = np.zeros((5,5))

				repetir = False
				
			elif repetir.lower() == "n":
				print("Gracias por haber jugado.")
				repetir = False
				return "NO"
				
			else:
				print("Lo siento. No te entendido.")





while True:
#empieza el juego y meto todo en su sitio:

#creo un objeto juego para poder jugar
	juego = Juego()

	#inicializar juegos retorna un marco con las posiciones aleatorias de los barcos y una lista de las posiciones de los barcos. Lo hacemos para los dos jugadores.
	j1_marco, j1_barcos1 = juego.inicializar_barcos()
	j2_marco, j2_barcos2 = juego.inicializar_barcos()

	#se crea para el jugador 1 los dos barcos, como parametro obligatorio una posicion, opcional tendra la operatividad que por defecto es True y las veces dañado que sera 0 por defecto
	j1_barco1 = Barco(j1_barcos1[0])
	j1_barco2 = Barco(j1_barcos1[1])

	#se crea para el jugador 2 los dos barcos, como parametro obligatorio una posicion, opcional tendra la operatividad que por defecto es True y las veces dañado que sera 0 por defecto
	j2_barco1 = Barco(j2_barcos2[0])
	j2_barco2 = Barco(j2_barcos2[1])

	#El marco inicial del jugador 1 se agrega a su tablero junto con los objetos barcos que contienen toda su info. Parametros obligatorios.
	j1_tablero = Tablero(j1_marco,[j1_barco1,j1_barco2])

	#El marco inicial del jugador 2 se agrega a su tablero junto con los objetos barcos que contienen toda su info. Parametros obligatorios.
	j2_tablero = Tablero(j2_marco,[j2_barco1,j2_barco2])

	#El objeto juego tiene un metodo para añadir tableros, y en este caso añadiremos los de los dos jugadores que contienen ya el propio tablero y los barcos de cada uno.
	juego.añadir_tablero(j1_tablero)
	juego.añadir_tablero(j2_tablero)

	#hasta aqui añado todo lo que necesito

	
	
	preparados = input("\n\n\t\t\t\t\tPULSA CUALQUIER TECLA PARA COMENZAR: ") #PULSANDO CUALQUIER TECLA SE DA COMIENZO AL JUEGO



	os.system ("cls") #PARA LIMPIAR LA TERMINAL A SU PASO. CUESTIÓN DE ESTÉTICA.

	
	while True:
		
		time.sleep(0.8)
		print("\n\n\n\n\t\t\t***************************** JUGADOR 1 *************************************\n")
		
		time.sleep(2)
		print("### TU RIVAL ###\n")
		print(Juego.quedan_contrario2)
		
		
		print("\n### TU TABLERO ###\n")
		
		j1_tablero.mostrar_tablero()
		
		print(" ")
		
		time.sleep(1)
		juego.preguntar_posicion_a_j1()
		
		time.sleep(1.2)

		juego.estado_barcos_j2()
		time.sleep(3.5)
		os.system("cls")
		gana_j1 = juego.estado_tablero_j2()
		time.sleep(1)

		if gana_j1 == "¡GANASTE!": #SI EL METODO ESTADO_TABLERO DEVUELVE GANASTE SE ROMPE CON EL BUCLE DE LAS PREGUNTAS
			break


		
		time.sleep(0.8)
		print("\n\n\n\n\t\t\t***************************** JUGADOR 2 *************************************\n")
		
		time.sleep(2)
		
		print("### TU RIVAL ###\n")
		print(Juego.quedan_contrario1)
		
		
		
		print("\n### TU TABLERO ###\n")
		j2_tablero.mostrar_tablero()
		time.sleep(1)
		juego.preguntar_posicion_a_j2()
		
		time.sleep(1.2)
		
		juego.estado_barcos_j1()
		time.sleep(3.5)
		os.system("cls")
		

		gana_j2 = juego.estado_tablero_j1()
		time.sleep(1)
		

		if gana_j2 == "¡GANASTE!":
			break

		
		print(" ")


	resp = juego.repetir()

	if resp == "NO": #SI EL MÉTODO REPETIR DE LA CLASE JUEGO DEVUELVE "NO", SE ROMPERÁ CON EL BUCLE PRINCIPAL
		break


	
			



