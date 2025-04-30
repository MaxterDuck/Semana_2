#Encontrar la letra más frecuente:

palabra = input("Dame una palabra: ")
num_letras ={}

for i in palabra: 
    if i in num_letras:
        num_letras[i]+=1
    else: 
        num_letras[i]=1 
letra_mas_frecuente = max(num_letras,key=lambda k: num_letras[k])
print("La letra más frecuente es:", letra_mas_frecuente)
print("Aparece", num_letras[letra_mas_frecuente], "veces.")