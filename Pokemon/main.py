import funciones

if __name__ == '__main__':
    pokemons_1_objetos = []
    pokemons_2_objetos = []
    #Ejercicio 1 comprobacion:
    ''' Eevee = funciones.Pokemon(1234, "Eevee", "Cabezazo", 59, 8, 4)
    print(Eevee.__str__())
    Charmander = funciones.Pokemon(2345, "Charmander", "Puñetazo", 76, 5, 6)
    print(Charmander.__str__())
    print(funciones.Pokemon.ataque(Eevee, Charmander))'''

    #Creacion pokemones csv:
    funciones.sacar_pokemon('coach_1_pokemons.csv', funciones.pokemons_1)
    funciones.sacar_pokemon('coach_2_pokemons.csv', funciones.pokemons_2)

    print("------------------------------POKEMONS ENTRENADOR 1------------------------------")
    pokemon1coach1 = funciones.Pokemon(int(funciones.pokemons_1[0][0]), funciones.pokemons_1[0][1], funciones.pokemons_1[0][2], int(funciones.pokemons_1[0][3]), int(funciones.pokemons_1[0][4]), int(funciones.pokemons_1[0][5]))
    print(pokemon1coach1)
    print('\n')
    pokemon2coach1 = funciones.Pokemon(int(funciones.pokemons_1[1][0]), funciones.pokemons_1[1][1], funciones.pokemons_1[1][2], int(funciones.pokemons_1[1][3]), int(funciones.pokemons_1[1][4]), int(funciones.pokemons_1[1][5]))
    print(pokemon2coach1)
    print('\n')
    pokemon3coach1 = funciones.Pokemon(int(funciones.pokemons_1[2][0]), funciones.pokemons_1[2][1], funciones.pokemons_1[2][2], int(funciones.pokemons_1[2][3]), int(funciones.pokemons_1[2][4]), int(funciones.pokemons_1[2][5]))
    print(pokemon3coach1)
    print('\n')
    pokemons_1_objetos.append(pokemon1coach1)
    pokemons_1_objetos.append(pokemon2coach1)
    pokemons_1_objetos.append(pokemon3coach1)
    print("------------------------------POKEMONS ENTRENADOR 2------------------------------")
    pokemon1coach2 = funciones.Pokemon(int(funciones.pokemons_2[0][0]), funciones.pokemons_2[0][1], funciones.pokemons_2[0][2], int(funciones.pokemons_1[0][3]), int(funciones.pokemons_1[0][4]), int(funciones.pokemons_2[0][5]))
    print(pokemon1coach2)
    print('\n')
    pokemon2coach2 = funciones.Pokemon(int(funciones.pokemons_2[1][0]), funciones.pokemons_2[1][1], funciones.pokemons_2[1][2], int(funciones.pokemons_2[1][3]), int(funciones.pokemons_2[1][4]), int(funciones.pokemons_2[1][5]))
    print(pokemon2coach2)
    print('\n')
    pokemon3coach2 = funciones.Pokemon(int(funciones.pokemons_2[2][0]), funciones.pokemons_2[2][1], funciones.pokemons_2[2][2], int(funciones.pokemons_2[2][3]), int(funciones.pokemons_2[2][4]), int(funciones.pokemons_2[2][5]))
    print(pokemon3coach2)
    print('\n')
    pokemons_2_objetos.append(pokemon1coach2)
    pokemons_2_objetos.append(pokemon2coach2)
    pokemons_2_objetos.append(pokemon3coach2)

    print("-----------------------COMIENZA EL COMBATE----------------------")
    #while funciones.entrenador_derrotado == False:
    print("Entrenador 1:")
    funciones.get_pokemon_de_lista(pokemons_1_objetos, "Entrenador 1")
    print("Entrenador 2:")
    funciones.get_pokemon_de_lista(pokemons_2_objetos, "Entrenador 2")
    

    
