#EJERCICIO DE PRACTICA 
palabra = input("Introduce la palabra : " )
contador = 0
vocales = "aeiou"
for letra in palabra:
    if letra.lower () in vocales:
        contador += 1
print (f"En la palabra hay {contador} vocales en la palabra")
