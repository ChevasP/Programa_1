
choose_enemy_pokemon = input("Elije contra quien combatiras (Charmander / Bulbasaur / Squirtle): ")

heal_pikachu = 100
dmage_pikachu_chispazo = 14
dmage_pikachu_BolaV = 15
dmage_Charmander = 10
dmage_Squirtle = 7
dmage_Bulbasaur = 8

healenemy = 0

if choose_enemy_pokemon == "Charmander":
    healenemy = 100
if choose_enemy_pokemon == "Bulbasaur":
    healenemy = 90
if choose_enemy_pokemon == "Squirtle":
    healenemy = 80


while heal_pikachu > 0 and healenemy > 0:

    choosed_atack = input("Que ataque quieres usar? (Chispazo | 14) / Bola Voltio (15)|")
    if choosed_atack == "Chispazo":
        healenemy -= 14
    if choosed_atack == "Bola Voltio":
        healenemy -= 15
    if healenemy ==0:
        print("Vida del enemigo: 0 ")
    print("Vida del enemigo: ", healenemy)
    print("El enemigo te a atacado!!")
    if choose_enemy_pokemon == "Charmander":
        heal_pikachu -= 10
    if choose_enemy_pokemon == "Bulbasaur":
        heal_pikachu -= 8
    if choose_enemy_pokemon == "Squirtle":
        heal_pikachu -= 7
    print("Vida Pikachu: ", heal_pikachu)


print("Combate Finalizado")