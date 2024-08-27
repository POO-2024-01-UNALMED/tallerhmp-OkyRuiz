class Deportista():

    def __init__(self, añosPracticando):

        self._deporte = "Futbol"
        self._añosPracticando = añosPracticando
    
    def getDeporte(self):
        return self._deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando
    
    def setDeporte(self, deporte):
        self._deporte = deporte

    def setAñosPracticando(self, añosPracticando):
        self._añosPracticando = añosPracticando

    