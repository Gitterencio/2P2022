#TERENCIO MATAMOROS 20171031886
#
class Vector:
	def __init__(self,elementos):
		if isinstance(elementos,list):
			for elm in elementos:
					if not isinstance(elm,float):
							raise TypeError('No es flotante: {0}'.format(elm))
					else:
						self._elementos = elementos
  
		else:
			raise TypeError('No es una lista')
		pass

	def sumar(self,vector):
		if isinstance(vector,Vector):
			if self.size() == vector.size():
				v = []
				for i in range(self.size()):
					v.append(self._elementos[i]+vector._elementos[i])
				return Vector(v)
			else:
				raise ValueError('el vector ingresado tiene dimenciones incorrectas')
		else:
			raise TypeError('No es un vector')
		pass
    
	def prod_punto(self,vector):
		if isinstance(vector,Vector):
			if self.size() == vector.size():
				res = 0
				for i in range(self.size()):
					res+=(self._elementos[i]*vector._elementos[i])
				return res
			else:
				raise ValueError('el vector ingresado tiene dimenciones incorrectas')
		else:
			raise TypeError('No es un vector')
		pass

	def size(self):
		return len(self._elementos)
		pass
	
	def elementos(self):
		return self._elementos
		pass
	
	def __str__(self):
		return str(self.elementos())
		pass


v1= Vector([4.0,5.0,6.0])
v2 = Vector([1.0,2.0,3.0])
v3 = v1.sumar(v2);
print(v3)
v3 = v2.sumar(v1);
print(v3)
v4 = v1.prod_punto(v2)
print(v4)

print(v1)
print(v2)