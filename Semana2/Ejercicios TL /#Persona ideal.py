#Persona ideal 
print ("Mi persona ideal")
puntaje =0 

pregunta1 = input("¿Es respetuosa? ")
if pregunta1 == "si": 
    print ("Excelente vamos bien")
    puntaje = puntaje + 100 

    pregunta2 =(input("¿Le gustan los videojuegos? "))
    if pregunta2 =="si":
        print ("Biennnn, vamos por buen camino")
        puntaje = puntaje +80
    elif pregunta2 == "no":
        print("Hmmmm, Se puede mejorar")
        puntaje = puntaje -10
       
    pregunta3 =(input("¿Quiere salir adelante en la vida? "))
    if pregunta3 == "si":
            print ("Eso esta muy bien, una persona berraca! ")
            puntaje = puntaje +50
    if pregunta3 =="no":
            print ("Manito alejese de ahi :) ")
            puntaje = puntaje -70

    pregunta4 =(input("¿Es linda? "))
    if pregunta4 == "si":
                print ("Estamos flying in the life bro ")
                puntaje = puntaje +100
    elif pregunta4 == "depende":
        print ("Conocela bro, depronto te sorprende")
    puntaje = puntaje +10
    if pregunta4 == "no":
        print ("Uhhh muy mal")
        puntaje = puntaje -30            
                
    pregunta5 =(input("¿Le gustan los animales? "))
    if pregunta5 =="si":
        print ("Que chevere")
        puntaje = puntaje +20
    if pregunta5 =="no":
            print ("Muy mal, no puedo estar con una persona asi :)")
    print (puntaje)

    if puntaje >= 200 and puntaje <=400:
          print("Conozcamonos")
    elif puntaje <=100 and puntaje >=180:
          print ("Ni loco bro por ahi no pasamos")    

elif pregunta1 == "no":
    puntaje = puntaje -20
    print ("Imposible conmigo no vas a estar")
