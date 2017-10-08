class cuenta:

    def __init__(self, cliente, numero,saldo=0):
    	try:
    		self.numero=int(numero)
    		self.cliente=str(cliente)
    		self.saldo=int(saldo)
    	except Exception as e:
    		raise e
    	self.numero=numero
    	self.cliente=cliente
    	self.saldo=saldo

    def depositar(self,saldo):
    	self.saldo=self.saldo+saldo

    def setNumero(self,numero):
    	self.numero=numero

    def getNumero(self):
    	return self.numero

    def setSaldo(self,saldo):
    	self.saldo=saldo

    def getSaldo(self):
    	return self.saldo

    def setCliente(self,cliente):
    	self.cliente=cliente

    def getCliente(self):
        return self.cliente

    def __str__(self):
    	return("Numero de cuenta: "+ str(self.getNumero()) + "Cliente:"+ self.getCliente() + "Saldo:" + str(self.getSaldo()))

    def toString(self):
		return("Numero de cuenta: "+ str(self.getNumero()) + "Cliente:"+ self.getCliente() + "Saldo:" + str(self.getSaldo()))

class repositorio():

	def __init__(self,banco):
		self.banco=banco
		self.lista=[]

	def getBanco():
		return self.banco

	def agregarCuenta(self,cuenta):
		self.lista.append(cuenta)

	def __str__(self):
		cadena=''
		for c in self.lista:
			cadena=cadena+c.toString()
		return cadena

	def verCuentas(self):
		for c in self.lista:
			print(c)

def main():
	banco1=repositorio("santander")

	rta=1

	while rta==1:
		nombre=input("Nombre:")
		numero=input("numero:")
		saldo=input("saldo:")
		cuenta1=cuenta(self.nombre,self.numero,self.saldo)
		banco1.agregarCuenta(cuenta1)
		banco1.verCuentas()
		rta=input("quiere cargar mas? toque 1 para seguir")

if __name__ == '__main__':
	main()
    	
		