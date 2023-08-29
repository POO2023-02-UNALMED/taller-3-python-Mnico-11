class TV:

    numTV = 0
    
    def __init__(self,marca,estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._volumen=1
        self._precio=500
        self._control = None
        TV.numTV +=1

    def setMarca(self, marca):
            self._marca = marca

    def getMarca(self):
            return self._marca

    def setCanal(self, canal):
        if canal>=1 and canal<=120 and self.estado == True:
            self._canal = canal

    def getCanal(self):
            return self._canal

    def setVolumen(self, volumen):
        if volumen >= 0 and volumen <=7 and self.estado == True:
            self._volumen = volumen

    def getVolumen(self):
            return self._volumen


    def setPrecio(self, precio):
            self._precio = precio

    def getPrecio(self):
            return self._precio


    def setControl(self, control):
            self._control = control

    def getControl(self):
            return self._control


    @classmethod
    def getNumTV(cls):
        return cls._numTV
    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV=numTV 


    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False


    def canalUp(self):
        if self.canal >= 1 and self.canal < 120 and self.estado == True:
            self.canal +=1
    def canalDown(self):
        if self.canal > 1 and self.canal <= 120 and self.estado == True:
            self.canal -=1
    def volumenUp(self):
        if self.volumen >= 0 and self.volumen < 7 and self.estado== True:
            self.volumen +=1
    def volumenDown(self):
        if self.volumen > 0 and self.volumen <= 7 and self.estado == True:
            self.volumen -=1

    def getEstado(self):
        return self._estado