class Control:

    def __init__(self):
        self._tv = None

    def turnOn(self):
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()
    

    
    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()


    
    def volumenUp(self):
        self._tv.volumenUp()
    
    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self,c):
        self._tv.setCanal(c)

    def setVolumen(self,v):
        self._tv.setVolumen(v)


    def enlazar(self,tv1):
        tv1.setControl(self)
        self.setTv(tv1)

    
    def getTv(self):
        return self._tv

    def setTv(self,t):
        self._tv=t