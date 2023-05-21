
from Estado import ESTADO_FINAL

import time


class Grafo:

	def __init__(self):

		self.bfs_padre = {}
		self.dfs_padre = {}

		self.expandedBFS = 0
		self.expandedDFS = 0

	def BFS(self, inicio):
		self.expandedBFS = 0	#Contador en 0
		self.bfs_padre[inicio] = None			#Nodo inicial
		visitado = {(inicio.misioneros, inicio.canivales, inicio.dir): True}
		inicio.level = 0

		start_time = time.time()
		cola = [inicio]
		while cola:
			self.expandedBFS += 1

			primero = cola.pop(0)

			if primero.isGoalState():
				print("Nro de Nodos Expandidos: " + str(self.expandedBFS))
				print("Nro de Nodos Explorados: " + str(visitado.__len__()))
				cola.clear()
				self.bfs_padre[ESTADO_FINAL] = primero
				return self.bfs_padre

			# Detiene la búsqueda después de alcanzar un cierto límite de tiempo/nodos.
			t = time.time() - start_time
			if t > primero.CONSTANTES.MAX_TIME or self.expandedBFS > primero.CONSTANTES.MAX_NODES:
				if t > primero.CONSTANTES.MAX_TIME:
					print("%.2fs SE HA EXCEDIDO EL LÍMITE DE TIEMPO de %.2fs" % (t, u.CONSTANTES.MAX_TIME))
				else:
					print("SE HA EXCEDIDO EL LÍMITE DE NODOS de %d" % primero.CONSTANTES.MAX_NODES)
				print("Nro de Nodos Expandidos: " + str(self.expandedBFS))
				print("Nro de Nodos Explorados: " + str(visitado.__len__()))
				cola.clear()
				return {}

			for vecino in reversed(primero.sucesores()):
				if (vecino.misioneros, vecino.canivales, vecino.dir) not in visitado.keys():	#si no es visitado
					self.bfs_padre[vecino] = primero
					vecino.level = primero.level + 1
					cola.append(vecino)			#Vecino del vecino actual XD
					visitado[(vecino.misioneros, vecino.canivales, vecino.dir)] = True		#Marcamos el vecinoo actual como visitado

		return {}

	def DFS(self, inicio):
		self.expandedDFS = 0
		self.dfs_padre[inicio] = None
		visitado = {(inicio.misioneros, inicio.canivales, inicio.dir): True}

		start_time = time.time()
		pila = [inicio]
		while pila:
			ultimo = pila.pop()
			self.expandedDFS += 1

			if ultimo.isGoalState():
				print("Nro de Nodos Expandidos: " + str(self.expandedDFS))
				print("Nro de Nodos Explorados: " + str(visitado.__len__()))
				self.dfs_padre[ESTADO_FINAL] = ultimo
				pila.clear()
				return self.dfs_padre

			t = time.time() - start_time
			# Detiene la búsqueda después de alcanzar un límite de tiempo o de nodos determinado.
			if t > ultimo.CONSTANTES.MAX_TIME or self.expandedDFS > ultimo.CONSTANTES.MAX_NODES:
				if t > ultimo.CONSTANTES.MAX_TIME:
					print("%.2fs SE HA EXCEDIDO EL LÍMITE DE TIEMPO de %.2fs" % (t, ultimo.CONSTANTES.MAX_TIME))
				else:
					print("SE HA EXCEDIDO EL LÍMITE DE NODOS de %d" % ultimo.CONSTANTES.MAX_NODES)
				print("Nro de Nodos Expandidos: " + str(self.expandedDFS))
				print("Nro de Nodos Explorados: " + str(visitado.__len__()))
				pila.clear()
				return {}

			for vecino in ultimo.sucesores():
				if (vecino.misioneros, vecino.canivales, vecino.dir) not in visitado.keys():
					visitado[(vecino.misioneros, vecino.canivales, vecino.dir)] = True			#Se marca como visitado 
					self.dfs_padre[vecino] = ultimo					
					pila.append(vecino)			
		return {}

	# Imprime el camino devuelto por BFS/DFS.
	def printPath(self, ListPadres, ultimo):
		if ultimo is None:
			return
		if ListPadres == {} or ListPadres is None:  # Si no está en ListPadres.keys():
			return
		if ultimo == ESTADO_FINAL: ultimo = ListPadres[ultimo]

		pila = []

		while ultimo is not None:
			pila.append(ultimo)
			ultimo = ListPadres[ultimo]

		while pila:
			print(pila.pop())
