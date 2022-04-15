import funciones

if __name__ == '__main__':
    Eevee = funciones.Pokemon(1234, "Eevee", "Cabezazo", 59, 8, 4)
    print(Eevee.__str__())
    Charmander = funciones.Pokemon(2345, "Charmander", "Puñetazo", 76, 5, 6)
    print(Charmander.__str__())
    print(funciones.Pokemon.ataque(Eevee, Charmander))
    
    
