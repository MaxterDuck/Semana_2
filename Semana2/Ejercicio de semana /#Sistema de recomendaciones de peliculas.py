#Sistema de recomendaciones de peliculas
edad= int (input("¿Que edad tienes?: "))

if edad <13: 
    print("Eres menor de 13 años, te recomendamos películas aptas para tu edad.")
    peli = input("¿Qué tipo de películas te gusta? (Acción, Comedia, Terror, Fantasía): ").strip().lower()
    
    if peli == "accion":
        print("Te recomendamos las siguientes películas:\n- Toy Story\n- Spider-Man: Un nuevo universo\n- Los Increíbles\n- Como entrenar a tu dragón")
    elif peli == "comedia":
        print("Te recomendamos las siguientes películas:\n- El libro de la vida\n- Zombieland\n- La máscara\n- Paddington")
    elif peli == "terror":
        print("Te recomendamos las siguientes películas:\n- Hotel Transylvania\n- La casa de los sustos\n- Scooby-Doo\n- Los cazafantasmas")
    elif peli == "fantasia":
        print("Te recomendamos las siguientes películas:\n- El rey león\n- Aladdin\n- Encanto\n- El viaje de Chihiro")
    else:
        print("Lo siento, esa categoría no está disponible.")
else:
    peli = input("¿Que tipo de peliculas te gusta? (Accion,Comedia,Terror,Fantasia): ").strip().lower()

    if peli == "accion":
        print ("Eso esta muy bien las recomendaciones de peliculas son las siguientes:\n Rapidos y furiosos \n Uncharted \n Eternals \n Creed III ")
    elif peli == "comedia":
        print ("Eso esta muy bien las recomendaciones de peliculas son las siguientes: \n El paseo 1 \n La vida es bella \n La mascara \n Zombieland ")
    elif peli == "terror":
        print ("Eso esta muy bien las recomendaciones de peliculas son las siguientes: \n El exorcista 2 \n Chucky \n Anabelle \n SAW III")
    elif peli == ("fantasia"):
        print ("Eso esta muy bien las recomendaciones de peliculas son las siguientes: \n El libro de la vida \n Dracula \n Encanto \n Aladin ")
    else: 
        print ("Lo siento, Esa categoria no esta disponible :( )")

