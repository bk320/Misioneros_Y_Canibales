from Constantes import Direccion

MAX_M = 30
MAX_C = 30
CAPAC_BOTE = 20
CNST = None


class Estado(object):

	def __init__(self, misioneros, canivales, dir, misionerosPassed, canivalesPassed, level, CONSTS,movimientos):
		self.misioneros = misioneros
		self.canivales = canivales
		self.dir = dir
		self.action = ""
		self.level = level
		self.misionerosPassed = misionerosPassed
		self.canivalesPassed = canivalesPassed
		self.CONSTANTES = CONSTS
		self.movimientos = movimientos

		global MAX_M
		global MAX_C
		global CAPAC_BOTE
		global CNST

		if not CONSTS is None:
			CNST = CONSTS

			MAX_M = CONSTS.MAX_M
			MAX_C = CONSTS.MAX_C
			CAPAC_BOTE = CONSTS.CAPAC_BOTE

	# True para continuar el primer if
	def sucesores(self):
		listChild = []
		if not self.isValid() or self.isGoalState():
			#print("Estado: No se generaron Sucesores")
			return listChild
		if self.dir == Direccion.DE_ANTIGUO_A_NUEVO:
			sgn = -1
			direction = "desde la orilla original hasta la nueva orilla."
		else:
			sgn = 1
			direction = "regresar desde la nueva orilla hasta la orilla original."
		for i in self.movimientos:
			(m, c) = i
			self.addValidSucesores(listChild, m, c, sgn, direction)
			
		return listChild

	def addValidSucesores(self, listChild, m, c, sgn, direction):
		newEstado = Estado(self.misioneros + sgn * m, self.canivales + sgn * c, self.dir + sgn * 1,
							self.misionerosPassed - sgn * m, self.canivalesPassed - sgn * c, self.level + 1,
							self.CONSTANTES,self.movimientos)
		
		if newEstado.isValid():
			newEstado.action = " lleva a %d misionero(s) y %d canibal(s) %s." % (m, c, direction)
			listChild.append(newEstado)

	def isValid(self):
		# Verificar si los valores tienen concordancia
		if self.misioneros < 0 or self.canivales < 0 or self.misioneros > MAX_M or self.canivales > MAX_C or (
				self.dir != 0 and self.dir != 1):
			#print("Estado no valido")
			return False

		# luego verifica si los misioneros son superados en número por los caníbales en alguna orilla.
		if (self.canivales > self.misioneros > 0) or (			# más caníbales que misioneros en la orilla original.
				self.canivalesPassed > self.misionerosPassed > 0):  # ambos son mayores a 0 ?
			#print("Numero incoherente de canibales o misioneros")
			return False
		#print("Estado valido")
		return True

	#veirfica si no hay canibales, ni misioneros en la orilla y la direcion sea igual a DE_NUEVO_A_ANTIGUO entonces devuelve true
	def isGoalState(self):
		return self.canivales == 0 and self.misioneros == 0 and self.dir == Direccion.DE_NUEVO_A_ANTIGUO
	#Cadena legible
	def __repr__(self):
		return "\n%s\n\n< Step %d Estado (%d, %d, %d, %d, %d) >" % (
			self.action, self.level, self.misioneros, self.canivales, self.dir, self.misionerosPassed,
			self.canivalesPassed)
	#comparacion se son iguales true si son iguales
	def __eq__(self, otro):
		return self.misioneros == otro.misioneros and self.canivales == otro.canivales and self.dir == otro.dir
	#devuelve su clave en diccionario y elemneto 
	def __hash__(self):
		return hash((self.misioneros, self.canivales, self.dir))
	#compara si son deferentes true si son diferentes
	def __ne__(self, otro):
		return not (self == otro)


ESTADO_FINAL = Estado(-1, -1, Direccion.DE_NUEVO_A_ANTIGUO, -1, -1, 0, CNST,None)

