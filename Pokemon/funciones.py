import random
class Pokemon:
    def __init__(self, id, nombre, arma, pv, pa, pd):
        self.id = id
        self.nombre = nombre
        self.arma = arma
        self.pv = pv
        self.pa = pa
        self.pd = pd
        

    def get_id(self):
        return self.id
   
    def set_id(self, id):
        self.id = id
    
    def get_nombre(self):
        return self.nombre
   
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_arma(self):
        return self.arma

    def set_arma(self, arma):
        self.arma = arma
        
    def get_pv(self):
        return self.pv
   
    def set_pv(self, pv):
        self.pv= random.randint(1, 100)
        
    def get_pa(self):
        return self.pa
   
    def set_pa(self, pa):
        self.pa= random.randint(1, 100)
        
    def get_pd(self):
        return self.pd
   
    def set_pd(self, pd):
        self.pd= random.randint(1, 100)

