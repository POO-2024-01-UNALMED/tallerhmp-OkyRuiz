class Persona():
    
    #INICIALIZADOR
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo

    
    # MÉTODOS GET Y SET
    def getNombre(self):
        return self._nombre
    
    def getEdad(self):
        return self._edad
    
    def getAltura(self):
        return self._altura
    
    def getSexo(self):
        return self._sexo

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self,edad):
        self._edad = edad

    def setAltura(self, altura):
        self._altura = altura
    
    def setSexo(self, sexo):
        self._sexo = sexo