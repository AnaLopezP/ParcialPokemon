import funciones

if __name__ == '__main__':
    Eevee = funciones.Pokemon(1234, "Eevee", "Cabezazo", 59, 8, 4)
    print(Eevee.cadena())
    Charmander = funciones.Pokemon(2345, "Charmander", "Puñetazo", 76, 5, 6)
    print(Charmander.cadena())
    funciones.Pokemon.defensa(Charmander, 5)
    funciones.Pokemon.ataque(Eevee, Charmander)
    
