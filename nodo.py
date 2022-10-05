
class nodo():
    def __init__(self,info):
        self.info = info
        self.siguiente = None




    def getsiguiente(self):
        return self.siguiente
    
    def setsiguiente(self,siguiente):
        self.siguiente = siguiente