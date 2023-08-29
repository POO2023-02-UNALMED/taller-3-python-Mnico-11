class TV:

    numTV=0

    def __init__(self,marca,estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._volumen=1
        self._precio=500
        self._control = None
        TV.numTV +=1

    
    def getMarca(self):
        return self._marca
    
    def setMarca(self,s):
        self._marca=s

    def getControl(self):
        return self._control
    
    def setControl(self,s):
        self._control=s

    def getCanal(self):
        return self._canal
    
    def setCanal(self,s):
        if(self.getEstado() and 121> s and s>0):
            self._canal=s

    def getVolumen(self):
        return self._volumen
    
    def setVolumen(self,s):
        if(self.getEstado() and 8>s and s>-1):
            self._volumen=s

    def getPrecio(self):
        return self._precio
    
    def setPrecio(self,s):
        self._precio=s

    def getNumTV():
        return TV.numTV
    
    def setNumTV(num):
        TV.numTV=num

    def turnOn(self):
        self._estado=True
    
    def turnOff(self):
        self._estado=False
    
    def getEstado(self):
        return self._estado
    


    def volumenUp(self):
        if(self._estado and self.getVolumen()<8):
            self.setVolumen(self.getVolumen()+1)

    def volumenDown(self):
        if(self._estado and self.getVolumen()>-1):
            self.setVolumen(self.getVolumen()-1)

    def canalUp(self):
        if( self._estado and self.getCanal()<121 ):
            self.setCanal(self.getCanal()+1)

    def canalDown(self):
        if(self._estado and self.getCanal()>-1 ):
            self.setCanal(self.getCanal()-1)