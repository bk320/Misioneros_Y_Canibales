import sys
import time

from Grafo import Grafo
from Estado import Estado, Direccion, ESTADO_FINAL
from Constantes import CONST

CONTENIDO_IN = sys.stdin
CONTENIDO_OUT = sys.stdout

# Generar todos los posibles movimientos en el bote siguientes para cada estado, para reducir el número de iteraciones en cada nodo.
# Yo lo veo como los pasos por que va probando cuantos canivales y misioneros van por viaje, por que si van mas canivales se los comen
# y ese no deberia ser un paso
def genPosiblesmovimientos(CAPAC_BOTE):
	movimientos = []
	for m in range(CAPAC_BOTE + 1):
		for c in range(CAPAC_BOTE + 1):
			if 0 < m < c:
				continue
			if 1 <= m + c <= CAPAC_BOTE:
				movimientos.append((m, c))
	return movimientos

#Busqueda en Anchura(BFS)
def runBFS(g, ESTADO_INICIAL):
	sys.stdout = open("outBFS.txt", "w")
	print("\n\nBusqueda en Anchura(BFS) :: \n")
	start_time = time.time()
	p = g.BFS(ESTADO_INICIAL)
	end_time = time.time()
	if len(p):
		g.printPath(p, ESTADO_FINAL)
	else:
		print("No hay Solucion")
	print("\n Tiempo transcurrido en Busqueda por Anchura: %.2fms" % ((end_time - start_time)*1000))

#Busqueda en Profundidad(DFS)
def runDFS(g, ESTADO_INICIAL):
	sys.stdout = open("outDFS.txt", "w")
	print("\n\nBusqueda en Profundidad(DFS) :: \n")
	start_time = time.time()
	p = g.DFS(ESTADO_INICIAL)
	end_time = time.time()
	if len(p):
		g.printPath(p, ESTADO_FINAL)
	else:
		print("No hay Solucion")
	print("\n Tiempo transcurrido en Busqueda por profundidad: %.2fms" % ((end_time - start_time)*1000))


def main():

	#para realizar cualquier cambio Editar el archivo inicio.txt
	sys.stdin = open("inicio.txt", "r")

	#numero de Misioneros
	m = int(input("Nro misioneros = "))
	print(m, end="\n")
	#Numero de Canivales
	c = int(input("Nro canibales = "))
	print(c, end="\n")
	#Numero de Pasajeros Maximo
	k = int(input("Nro de pasajeros k = "))
	print(k, end="\n")
	#Limite de tiempo en segundos
	t = int(input("Tiempo_Limite_s = "))
	print(t, end="\n")
	#Limite de nodos de Exploracion
	n = int(input("Nodo_Limtes = "))
	print(n, end="\n")

	CNST = CONST(m, c, k, t, n)

	movimientos = genPosiblesmovimientos(CNST.CAPAC_BOTE)
	print(str(movimientos.__len__())+" iteraciones por Nodo.")

	ESTADO_INICIAL = Estado(CNST.MAX_M, CNST.MAX_C, Direccion.DE_ANTIGUO_A_NUEVO, 0, 0, 0, CNST, movimientos)
	

	g = Grafo()
	sys.stdout = CONTENIDO_OUT
	print("\nEjecutando Buqueda en Anchura>")
	runBFS(g, ESTADO_INICIAL)
	sys.stdout = CONTENIDO_OUT
	print("Ejecucion finalizada Busqueda en Anchura(BFS)>")

	print("\nejecutando Busqueda en Profundidad>")
	runDFS(g, ESTADO_INICIAL)
	sys.stdout = CONTENIDO_OUT
	print("Ejecucion finalizada Busqueda en Profundidad(DFS)>")

