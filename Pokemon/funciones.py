import random
from statistics import pvariance
class formato_excepcion(BaseException):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def get_mensaje(self):
        return self.mensaje

class Pokemon:
    def __init__(self, id, nombre, arma, pv, pa, pd):
        self.id = id
        self.nombre = nombre
        self.arma = arma
        self.pv = pv
        self.pa = pa
        self.pd = pd
        if isinstance(id, int):
            pass
        else:
            raise formato_excepcion("El ID tiene que ser un número")

        if isinstance(nombre, str):
            pass
        else:
            raise formato_excepcion("Ese nombre no es valido.")
        
        if isinstance(arma, str):
            pass
        else:
            raise formato_excepcion("Esa arma no es valida.")

        if isinstance(pv, int):
            pass
        else:
            raise formato_excepcion("Esos puntos de vida no son validos.")

        if isinstance(pa, int):
            pass
        else:
            raise formato_excepcion("Esos puntos de ataque no son validos.")

        if isinstance(pd, int):
            pass
        else:
            raise formato_excepcion("Esos puntos de defensa no son validos.")
            

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
        self.pv= pv
        
    def get_pa(self):
        return self.pa
   
    def set_pa(self, pa):
        self.pa = pa
        
    def get_pd(self):
        return self.pd
   
    def set_pd(self, pd):
        self.pd= pd

