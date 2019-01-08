
quiere_helado_input = input("¿Quiéres un helado?   (Si/No)\n").upper()

if quiere_helado_input == "SI":
    quiere_helado = True
elif quiere_helado_input == "NO":
    quiere_helado = False
else:
    print("Responde si o no, no se que has dicho pero lo tomare como un No")
    quiere_helado = False

tiene_dinero_input= input("¿Tienes Dinero ?  (Si/No)\n").upper()
esta_el_heladero_input= input("¿Esta el señor de los helados? (Si/No)\n").upper()
esta_tu_tia_input= input("¿Esta tu tía cerca?(Si/No)\n").upper()



tiene_dinero = tiene_dinero_input == "SI"
esta_tu_tia= esta_tu_tia_input == "SI"
puedes_comprarlo = tiene_dinero or esta_tu_tia
esta_el_heladero = esta_el_heladero_input =="SI"



if quiere_helado and puedes_comprarlo and esta_el_heladero:
    print("Comete el helado")
else:
    print("Pues ya nada")
