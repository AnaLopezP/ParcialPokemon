import random
import csv

lista_id = []
pokemons_2 = []
pokemons_1 = []
class formato_excepcion(BaseException):
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def get_mensaje(self):
        return self.mensaje
class rango_excepcion(BaseException):
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
        if not isinstance(id, int):
            raise formato_excepcion("El ID tiene que ser un número")
        else:
            lista_id.append(id)

        if not isinstance(nombre, str):
            raise formato_excepcion("Ese nombre no es valido.")
        
        if not isinstance(arma, str):
            raise formato_excepcion("Esa arma no es valida.")

        if isinstance(pv, int):
            if pv < 1 or pv > 100:
                raise rango_excepcion("Los PV tienen que estar entre 1 y 100")
        else:
            raise formato_excepcion("Esos puntos de vida no son validos.")

        if isinstance(pa, int):
            if pa < 1 or pa > 10:
                raise rango_excepcion("Los PA tienen que estar entre 1 y 10")
        else:
            raise formato_excepcion("Esos puntos de ataque no son validos.")

        if isinstance(pd, int):
            if pd < 1 or pd > 10:
                raise rango_excepcion("Los PD tienen que estar entre 1 y 10")
        else:
            raise formato_excepcion("Esos puntos de defensa no son validos.")

    def __del__(self):
        lista_id.remove(self.id)
            

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

    def esta_vivo(self):
        if self.pv == 0:
            return True
        else:
            return False

    def defensa(self, pokemon_dañado):
        puntos_daño = int(input())
        if puntos_daño < Pokemon.get_pd(pokemon_dañado):
            return True
        else:
            return False
    
    def ataque(self, pokemon_dañado):
        if Pokemon.defensa(self) == True:
            print("El pokemon " + str(Pokemon.get_nombre(pokemon_dañado)) + " ha sido dañado")
        else:
            print("El ataque no ha tenido efecto.")
    
    def __str__(self):
        cadena = "Tu pokemon se llama " + str(self.nombre) + " , de id " + str(self.id) + ". Su arma es " + str(self.arma) + " , y los puntos de vida, ataque y defensa son: " + str(self.pv) + " " + str(self.pa) + " " +  str(self.pd) + " respectivamente."
        return cadena

class Pokemon_Agua(Pokemon):
    def __init__(self, id, nombre, arma, pv, pa, pd):
        super().__init__(id, nombre, arma, pv, pa, pd)
        if pa < 11 or pa > 20:
            raise rango_excepcion("Los puntos de ataque tienen que estar entre 11 y 20")


class Pokemon_Tierra(Pokemon):
    def __init__(self, id, nombre, arma, pv, pa, pd):
        super().__init__(id, nombre, arma, pv, pa, pd)
        if pd < 11 or pd > 20:
            raise rango_excepcion("Los puntos de defensa tienen que estar entre 11 y 20")

class Pokemon_Aire(Pokemon):
    def __init__(self, id, nombre, arma, pv, pa, pd):
        super().__init__(id, nombre, arma, pv, pa, pd)

    def fight_defense():
        afecta = random.randint(1, 2)
        if afecta == 1:
            print("Ha esquivado el ataque")
            return False
        elif afecta == 2:
            return True

class Pokemon_Electro(Pokemon):
    def __init__(self, id, nombre, arma, pv, pa, pd):
        super().__init__(id, nombre, arma, pv, pa, pd)
    
    def fight_attack(pv):
        doble = random.randint(1, 2)
        if doble == 1:
            pv = 2*pv
            return pv
        elif doble == 2:
            return False


def crear_pokemon():
    id = input()
    nombre = input()
    arma = input()
    pv = input()
    pa = input()
    pd = input()
    pokemon = Pokemon(id, nombre, arma, pv, pa, pd)
    print("Tu pokemon se llama " + str(pokemon.nombre) + " , de id " + str(pokemon.id) + ". Su arma es " + str(pokemon.arma) + " , y los puntos de vida, ataque y defensa son: " + str(pokemon.pv) + str(pokemon.pa) + str(pokemon.pd), + " respectivamente.")


'''def sacar_pokemon(archivo, lista):
    with open (archivo) as file:
        delimitador = ';'
        leer = csv.DictReader(file, delimiter = delimitador)
        for row in leer:
            lista.append(row)
            print(lista)
    return lista


sacar_pokemon('coach_1_pokemons.csv', pokemons_1)
sacar_pokemon('coach_2_pokemons.csv', pokemons_2)

pokemon1 = Pokemon(pokemons_1[0], pokemons_1[1], pokemons_1[2], pokemons_1[3], pokemons_1[4], pokemons_1[5])
pokemon2 = Pokemon(pokemons_2[0], pokemons_2[1], pokemons_2[2], pokemons_2[3], pokemons_2[4], pokemons_2[5])'''