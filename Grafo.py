
from Estado import ESTADO_FINAL

import time


class Grafo:

	def __init__(self):

		self.bfs_parent = {}
		self.dfs_parent = {}

		self.expandedBFS = 0
		self.expandedDFS = 0

	def BFS(self, s):
		self.expandedBFS = 0
		self.bfs_parent[s] = None
		visited = {(s.misioneros, s.canivales, s.dir): True}
		s.level = 0

		start_time = time.time()
		queue = [s]
		while queue:
			self.expandedBFS += 1

			u = queue.pop(0)

			if u.isGoalState():
				print("Nro de Nodos Expandidos: " + str(self.expandedBFS))
				print("Nro de Nodos Explorados: " + str(visited.__len__()))
				queue.clear()
				self.bfs_parent[ESTADO_FINAL] = u
				return self.bfs_parent

			# Detiene la búsqueda después de alcanzar un cierto límite de tiempo/nodos.
			t = time.time() - start_time
			if t > u.CONSTANTES.MAX_TIME or self.expandedBFS > u.CONSTANTES.MAX_NODES:
				if t > u.CONSTANTES.MAX_TIME:
					print("%.2fs SE HA EXCEDIDO EL LÍMITE DE TIEMPO de %.2fs" % (t, u.CONSTANTES.MAX_TIME))
				else:
					print("SE HA EXCEDIDO EL LÍMITE DE NODOS de %d" % u.CONSTANTES.MAX_NODES)
				print("Nro de Nodos Expandidos: " + str(self.expandedBFS))
				print("Nro de Nodos Explorados: " + str(visited.__len__()))
				queue.clear()
				return {}

			for v in reversed(u.successors()):
				if (v.misioneros, v.canivales, v.dir) not in visited.keys():
					self.bfs_parent[v] = u
					v.level = u.level + 1
					queue.append(v)
					visited[(v.misioneros, v.canivales, v.dir)] = True

		return {}

	def DFS(self, s):
		self.expandedDFS = 0
		self.dfs_parent[s] = None
		visited = {(s.misioneros, s.canivales, s.dir): True}

		start_time = time.time()
		stack = [s]
		while stack:
			u = stack.pop()
			self.expandedDFS += 1

			if u.isGoalState():
				print("Nro de Nodos Expandidos: " + str(self.expandedDFS))
				print("Nro de Nodos Explorados: " + str(visited.__len__()))
				self.dfs_parent[ESTADO_FINAL] = u
				stack.clear()
				return self.dfs_parent

			t = time.time() - start_time
			# Detiene la búsqueda después de alcanzar un límite de tiempo o de nodos determinado.
			if t > u.CONSTANTES.MAX_TIME or self.expandedDFS > u.CONSTANTES.MAX_NODES:
				if t > u.CONSTANTES.MAX_TIME:
					print("%.2fs SE HA EXCEDIDO EL LÍMITE DE TIEMPO de %.2fs" % (t, u.CONSTANTES.MAX_TIME))
				else:
					print("SE HA EXCEDIDO EL LÍMITE DE NODOS de %d" % u.CONSTANTES.MAX_NODES)
				print("Nro de Nodos Expandidos: " + str(self.expandedDFS))
				print("Nro de Nodos Explorados: " + str(visited.__len__()))
				stack.clear()
				return {}

			for v in u.successors():
				if (v.misioneros, v.canivales, v.dir) not in visited.keys():
					visited[(v.misioneros, v.canivales, v.dir)] = True
					self.dfs_parent[v] = u
					stack.append(v)
		return {}

	# Imprime el camino devuelto por BFS/DFS.
	def printPath(self, parentList, tail):
		if tail is None:
			return
		if parentList == {} or parentList is None:  # Si no está en parentList.keys():
			return
		if tail == ESTADO_FINAL: tail = parentList[tail]

		stack = []

		while tail is not None:
			stack.append(tail)
			tail = parentList[tail]

		while stack:
			print(stack.pop())
