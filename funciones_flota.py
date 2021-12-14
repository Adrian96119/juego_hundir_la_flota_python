
from random import choice

def choice_opcion():
    
	#FUNCIÓN QUE DEVUELVE UNA POSICIÓN PARA EL BARCO ALEATORIA DE UNA LISTA DE OPCIONES

	opciones = [
	'F00', 'F01', 'F02', 'F10', 'F11', 'F12', 'F20', 'F21', 'F22', 'F30', 'F31', 'F32', 'F40', 'F41', 'F42', 
	'C00', 'C01', 'C02', 'C10', 'C11', 'C12', 'C20', 'C21', 'C22', 'C30', 'C31', 'C32', 'C40', 'C41', 'C42'
	]

	return choice(opciones)



def barco(opcion,array,n_barco):

	#FUNCION COMPLEMENTARIA DE LA OTRA. RECIBIRÁ TRES PARÁMETROS. LA POSICIÓN, UN TABLERO 5X5 DE NUMPY, Y EL NÚMERO DE BARCO PARA DISTINGUIR A UNO DE OTRO.
	#DEPENDIENDO DE LA OPCIÓN QUE SALGA, SE AÑADIRÁ EL NÚMERO QUE ENTRE POR PARÁMETRO QUE PERTENECERÁ A UNO DE LOS BARCOS PARA DISTINGUIRLOS.

	if opcion == "F00":
		array[0,0:3] = n_barco

	if opcion == "F01":
		array[0,1:4] = n_barco

	if opcion == "F02":
		array[0,2:] = n_barco

	if opcion == "F10":
		array[1,0:3] = n_barco

	if opcion == "F11":
		array[1,1:4] = n_barco

	if opcion == "F12":
		array[1,2:] = n_barco

	if opcion == "F20":
		array[2,0:3] = n_barco

	if opcion == "F21":
		array[2,1:4] = n_barco

	if opcion == "F22":
		array[2,2:] = n_barco

	if opcion == "F30":
		array[3,0:3] = n_barco

	if opcion == "F31":
		array[3,1:4] = n_barco

	if opcion == "F32":
		array[3,2:] = n_barco

	if opcion == "F40":
		array[4,0:3] = n_barco

	if opcion == "F41":
		array[4,1:4] = n_barco

	if opcion == "F42":
		array[4,2:] = n_barco

	if opcion == "C00":
		array[[0,1,2],[0]] = n_barco

	if opcion == "C01":
		array[[1,2,3],[0]] = n_barco

	if opcion == "C02":
		array[[2,3,4],[0]] = n_barco

	if opcion == "C10":
		array[[0,1,2],[1]] = n_barco

	if opcion == "C11":
		array[[1,2,3],[1]] = n_barco

	if opcion == "C12":
		array[[2,3,4],[1]] = n_barco

	if opcion == "C20":
		array[[0,1,2],[2]] = n_barco

	if opcion == "C21":
		array[[1,2,3],[2]] = n_barco

	if opcion == "C22":
		array[[2,3,4],[2]] = n_barco

	if opcion == "C30":
		array[[0,1,2],[3]] = n_barco

	if opcion == "C31":
		array[[1,2,3],[3]] = n_barco

	if opcion == "C32":
		array[[2,3,4],[3]] = n_barco

	if opcion == "C40":
		array[[0,1,2],[4]] = n_barco

	if opcion == "C41":
		array[[1,2,3],[4]] = n_barco

	if opcion == "C42":
		array[[2,3,4],[4]] = n_barco

	